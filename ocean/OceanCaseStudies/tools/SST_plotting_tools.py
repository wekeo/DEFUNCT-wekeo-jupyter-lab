import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import image_tools as img
from matplotlib import gridspec 
import xarray as xr
import os,sys
import xmltodict

def make_SLSTR_composite_plot(nc_files, plot_extents=None, fsz=20,\
                              land_resolution='50m', vmin=10, vmax=28,\
                              xsize=20, ysize=16, dpi=150, QMASK=4,\
                              cmap=plt.cm.RdYlBu_r, grid_factor=None):
    '''
     Plots SLSTR images from n-input files, will overay first to last.
    '''
    
    if not grid_factor:
        grid_factor = 1
    
    # get cartopy land layers
    land_poly = cfeature.NaturalEarthFeature('physical', 'land', land_resolution,
                                             edgecolor='k',
                                             facecolor=cfeature.COLORS['land'])
    
    # setup figure
    fig = plt.figure(figsize=(xsize, ysize), dpi=dpi)
    plt.rc('font', size=fsz)
    
    # setup axes
    gs = gridspec.GridSpec(3, 1, height_ratios=[20,0.5,1])
    gs.update(wspace=0.01, hspace=0.01)

    # setup plot 1
    axes_m = plt.subplot(gs[0,0], projection=ccrs.PlateCarree())
    axes_m.background_patch.set_facecolor('0.5')

    if plot_extents:
        axes_m.set_xlim([plot_extents[0], plot_extents[1]])
        axes_m.set_ylim([plot_extents[2], plot_extents[3]])

    # read data and plot background
    for nc_file in nc_files:
        nc_fid = xr.open_dataset(nc_file)
        LON = nc_fid.lon.data
        LAT = nc_fid.lat.data
                    
        # get subset based on plot extents
        if plot_extents:
            i1, i2, j1, j2 = img.subset_image(LAT, LON, plot_extents, corners=4, mode='global', data_type='swath')
        else:
            i1,i2,j1,j2 = 0,-1,0,-1

        # read in and subset if required
        LON = LON[i1:i2:grid_factor, j1:j2:grid_factor]
        LAT = LAT[i1:i2:grid_factor, j1:j2:grid_factor]

        SST_raw = np.squeeze(nc_fid.sea_surface_temperature.data[0,i1:i2:grid_factor, j1:j2:grid_factor])
        SST_BIAS = np.squeeze(nc_fid.sses_bias.data[0,i1:i2:grid_factor, j1:j2:grid_factor])
        QUALITY_LEVEL = np.squeeze(nc_fid.quality_level.data[0,i1:i2:grid_factor, j1:j2:grid_factor])
        nc_fid.close()

        # correct SST
        SST_C = SST_raw + SST_BIAS - 273.15

        # flag data
        SST_C[QUALITY_LEVEL<=QMASK] = np.nan

        # plot the SST field
        p1 = axes_m.pcolormesh(LON, LAT, SST_C, cmap=cmap,\
                          vmin=vmin, vmax=vmax, zorder=-1)

        # add the plot edges
        xml_file = os.path.dirname(nc_file)+'/xfdumanifest.xml'
        with open(xml_file) as fd:
            doc = xmltodict.parse(fd.read())
            coords = doc['xfdu:XFDU']['metadataSection']['metadataObject'][2]\
                        ['metadataWrap']['xmlData']['sentinel-safe:frameSet']\
                        ['sentinel-safe:footPrint']['gml:posList']

        # split the coords
        lats_lons = coords.split(' ')
        lats = np.asarray(lats_lons[::2]).astype(float)
        lons = np.asarray(lats_lons[1::2]).astype(float)

        if 'S3B' in nc_file:
            plot_col = 'b'
        else:
            plot_col = 'k'

        p2 = axes_m.plot(lons, lats, c=plot_col, linewidth=1,\
                    linestyle='--', zorder=5, alpha=0.5,\
                    transform=ccrs.PlateCarree())
    
    # add some map embelishments
    axes_m.coastlines(resolution=land_resolution, color='black', linewidth=1)
    axes_m.add_feature(land_poly)
    g1 = axes_m.gridlines(draw_labels = True)
    g1.xlabels_top = False
    g1.ylabels_right = False

    g1.xlabel_style = {'size': fsz, 'color': 'gray'}
    g1.ylabel_style = {'size': fsz, 'color': 'gray'}
    
    # setup plot2: colorbar
    axes_c = plt.subplot(gs[2,0])
    cbar = plt.colorbar(p1, cax=axes_c, orientation='horizontal')
    cbar.ax.tick_params(labelsize=fsz) 
    cbar.set_label('SLSTR SST composite [$^{o}$C]',fontsize=fsz)
    
    return gs, axes_m, axes_c