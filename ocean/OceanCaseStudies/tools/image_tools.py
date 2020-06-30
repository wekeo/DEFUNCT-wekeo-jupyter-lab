import numpy as np
from scipy.ndimage.measurements import label

def spheric_dist(lat1,lat2,lon1,lon2,mode='global'):
    #####################################################################
    #
    # function dist=spheric_dist(lat1,lat2,lon1,lon2)
    #
    # compute distances for a simple spheric earth
    #
    # input:
    #
    # lat1 : latitude of first point (matrix or point)
    # lon1 : longitude of first point (matrix or point)
    # lat2 : latitude of second point (matrix or point)
    # lon2 : longitude of second point (matrix or point)
    #
    # output:
    # dist : distance from first point to second point (matrix)
    ################################################################

    R_earth = 6367442.76
    # Determine proper longitudinal shift.
    ldiff = np.abs(lon2-lon1)
    ldiff[ldiff >= 180] = 360 - ldiff[ldiff >= 180]
    
    # Convert Decimal degrees to radians.
    deg2rad = np.pi/180
    phi1 = (90-lat1)*deg2rad
    phi2 = (90-lat2)*deg2rad
    theta1 = lon1*deg2rad
    theta2 = lon2*deg2rad

    lat1 = lat1*deg2rad
    lat2 = lat2*deg2rad
    ldiff = ldiff*deg2rad

    if mode=='global':
        # Compute the distances across the globe
        cos = (np.sin(phi1)*np.sin(phi2)*np.cos(theta1 - theta2) + 
              np.cos(phi1)*np.cos(phi2))
        arc = np.arccos(cos)
        dist = R_earth*arc
    elif mode=='local':
        # Compute the distances with local approximation
        xdist = [lon2-lon1] * np.cos(0.5*[lat2+lat1])
        ydist = lat2-lat1
        dist = R_earth*[xdist**2+ydist**2]^0.5

    return dist 

def subset_image(grid_lat, grid_lon, plot_extents):
    '''
     Cuts a box out of an image using the grid indices
     for the image corners. BEWARE USING THIS ON HALF-ORBIT,
     FULL-ORBIT or POLAR DATA. Uses spheric distance 
     calculator to find nearest points.
    '''
    # bottom left
    dist = spheric_dist(plot_extents[2], grid_lat, plot_extents[0], grid_lon)
    i0, j0 = np.unravel_index(dist.argmin(), dist.shape)
    
    # bottom right
    dist = spheric_dist(plot_extents[2], grid_lat, plot_extents[1], grid_lon)
    i1, j1 = np.unravel_index(dist.argmin(), dist.shape)    
    
    # top right
    dist = spheric_dist(plot_extents[3], grid_lat, plot_extents[1], grid_lon)
    i2, j2 = np.unravel_index(dist.argmin(), dist.shape)
    
    # top left
    dist = spheric_dist(plot_extents[3], grid_lat, plot_extents[0], grid_lon)
    i3, j3 = np.unravel_index(dist.argmin(), dist.shape)
    
    return min([i0, i1, i2, i3]), max([i0, i1, i2, i3]), min([j0, j1, j2, j3]), max([j0, j1, j2, j3])
    
def reduce_image(grid, grid_factor):
    '''
     Re-sample image on a coarser grid
    '''
    grid = grid[::grid_factor,::grid_factor]
    return grid
    
def truncate_image(channel, min_percentile=5, max_percentile=95):
    '''
     Remove image outliers
    '''
    channel[channel < np.percentile(channel, min_percentile)] \
        = np.percentile(channel, min_percentile)
    channel[channel > np.percentile(channel, max_percentile)] \
        = np.percentile(channel, max_percentile)
    return channel
    
def norm_image(image_array, contrast=[1.0, 1.0, 1.0], unhitch=True):
    '''
     Normalise image with either independant channels (unhitch) or 
     with combined channels
    '''
    if unhitch:
        # normalise with separating channels
        # non-linearity: contrast - note that the range is between 
        # 0 and 1, so no need to renormalise afterwards 
        for ii in range(np.shape(image_array)[-1]):
            image_array[:,:,ii] = \
                (image_array[:,:,ii] - np.nanmin(image_array[:,:,ii]))\
                / (np.nanmax(image_array[:,:,ii]) - np.nanmin(image_array[:,:,ii]))
            # apply contrast
            image_array[:,:,ii] = image_array[:,:,ii]**contrast[ii]
    else:
        # normalise without separating channels
        # non-linearity: contrast - note that the range is not between 
        # 0 and 1, so need to renormalise afterwards
        minval = np.nanmin(image_array)
        maxval = np.nanmax(image_array)
        
        for ii in range(np.shape(image_array)[-1]):
            image_array[:,:,ii] = \
                (image_array[:,:,ii] - minval)\
                / (maxval - minval)
            # apply contrast
            image_array[:,:,ii] = image_array[:,:,ii]**contrast[ii]

        minval = np.nanmin(image_array)
        maxval = np.nanmax(image_array)
        for ii in range(np.shape(image_array)[-1]):
            image_array[:,:,ii] = \
                (image_array[:,:,ii] - minval)\
                / (maxval - minval)
            
    return image_array

def surrounding_mean(xx,yy,array):
   '''
    takes mean of points around given point; fails on borders
   '''
   try:
       sum_vals = np.nanmean([array[xx-1,yy-1],\
                              array[xx,yy-1],\
                              array[xx+1,yy-1],\
                              array[xx-1,yy],\
                              array[xx+1,yy],\
                              array[xx-1,yy+1],\
                              array[xx,yy+1],\
                              array[xx+1,yy+1]])
   except:   
       sum_vals = np.nan

   return sum_vals

def gap_fill(input_array):
    '''
     fills artefact regions (assumed negative) with average of the perimeter
    '''
    # set up blank array
    input_blank = input_array.copy()
    input_array[input_array<0]=np.nan
    # mask boolean array, positive values assumed legitimate
    input_blank[input_blank>=0]=0
    input_blank[input_blank<0]=1
    # set structure
    structure = np.ones((3, 3), dtype=np.int)
    # isolate 'islands'
    labelled, ncomponents = label(input_blank, structure)

    # cycle through labelled islands and get perimeter value
    for the_label in np.unique(labelled):
      sum_value = []
      indices = np.where(labelled==the_label)
      Xs = indices[0]
      if len(Xs) > np.shape(input_array)[0]*np.shape(input_array)[1]*0.5:
          continue
      Ys = indices[1]
      for ii in np.arange(0,len(Xs)):
           sum_value.append(surrounding_mean(Xs[ii],Ys[ii],input_array))
      input_array[labelled == the_label] = np.nanmean(sum_value)

    return input_array