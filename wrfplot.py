#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 13:13:27 2021

@author: ghost
"""

"""
TODO List:
    1. Remove the unncessary statics such as lon and lat limits.
    2. Add new fuctions based on NCL and MetPy
"""

import wrf
import proplot as pplt
import cartopy.crs as crs
from netCDF4 import Dataset

def quickplot(ncfile, wrfvar, time=0):
    ncf = Dataset(ncfile)
    var = wrf.getvar(ncf, wrfvar, timeidx=time)

    # Get the latitude and longitude points
    lats, lons = wrf.latlon_coords(var)

    # Get the cartopy mapping object
    cart_proj = wrf.get_cartopy(var)

    # Creating Figures
    fig, axs = pplt.subplots(proj=cart_proj)

    axs.format(
        coast=True, #latlines=10, lonlines=10,
        lonlabels='b', latlabels='l',
    )

    m = axs.contourf(wrf.to_np(lons), wrf.to_np(lats), wrf.to_np(var),          transform=crs.PlateCarree(), cmap='sunset')

    fig.colorbar(m, label=var.description, loc='r')

    axs.set_xlim(wrf.cartopy_xlim(var))
    axs.set_ylim(wrf.cartopy_ylim(var))
