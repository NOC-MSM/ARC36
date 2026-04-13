import xarray as xr

fin = '/work/scratch-pw5/benbar/ARC36/Domain/bathy_arc36.nc'
fout = '/work/scratch-pw5/benbar/ARC36/Domain/pybdy_mask_arc36.nc'

ds = xr.open_dataset(fin)

mask = xr.zeros_like(ds['Bathymetry']).rename('mask')
mask[:] = ds['Bathymetry'] > 0
print(mask)
mask[-5:, :] = 0
mask[0:2, 0:3252] = 0
mask[0:2, 4585:5656] = 0
mask[0:2, 9995:10002] = 0
mask[0:2, 10648:10680] = 0
mask[0:2, 10590:10595] = 0
mask[0:2, 10702:11047] = 0
mask[0:2, 9949:9953] = 0


# Write to file

encoding = {
    "mask": {
        "zlib": True,
        "complevel": 1,
        "dtype": "float32",
        "chunksizes": (1, 544, 3240),  # (deptht, y, x) chunk shape on disk
    }
}

mask.to_netcdf(fout)#, encoding=encoding)


