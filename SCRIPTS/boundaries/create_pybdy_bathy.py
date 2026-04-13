import xarray as xr

#fin = '/work/scratch-pw5/benbar/ARC36/Domain/domain_cfg_arc36.nc'
fin = '/gws/ssde/j25a/nemo/vol1/benbar/ARC36/domain_cfg_arc36.nc'
fout = '/work/scratch-pw5/benbar/ARC36/Domain/bathy_arc36.nc'

ds = xr.open_dataset(fin)
varlist = list(ds.variables)
vars_want = ['bathy_metry', 'nav_lon', 'nav_lat', 'glamt', 'gphit']
vars_drop = [v for v in varlist if v not in vars_want]
ds = ds.drop_vars(vars_drop)
print(ds)
ds['Bathymetry'] = ds['bathy_metry'].rename('Bathymetry')
ds['nav_lon'] = ds['glamt'].rename('nav_lon')
ds['nav_lat'] = ds['gphit'].rename('nav_lat')
ds['nav_lon'] = ds['nav_lon'][0, :, :]
ds['nav_lat'] = ds['nav_lat'][0, :, :]
ds['Bathymetry'] = ds['Bathymetry'][0, :, :]
ds = ds.drop_vars('glamt')
ds = ds.drop_vars('gphit')
ds = ds.drop_vars('bathy_metry')
print(ds)

# Write to file

encoding = {
    "Bathymetry": {
        "zlib": True,
        "complevel": 1,
        "dtype": "float32",
        "chunksizes": (1, 544, 3240),  # (deptht, y, x) chunk shape on disk
    }
}

ds.to_netcdf(fout)#, encoding=encoding)


