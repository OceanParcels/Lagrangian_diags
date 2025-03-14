import numpy as np
from scipy.stats import gaussian_kde

def rem_nans(ds):
    """
    This renders lon and lat variables without nans for the last timestep.
    """
    bad_indices = np.isnan(ds['lon'][:,-1]) | np.isnan(ds['lat'][:,-1])
    good_indices = ~bad_indices
    lon_end_nonans = ds['lon'][:,-1][good_indices]
    lat_end_nonans = ds['lat'][:,-1][good_indices]

    return lon_end_nonans, lat_end_nonans

def kde_vals(lon_end_nonans, lat_end_nonans):
    """
    Calculates the KDE values and sorts x (lon) and y (lat) in function of z (KDE)

    Inputs :
    - lon_end_nonans : Longitude values free of nans
    - lat_end_nonans : Latitude values free of nans

    Outputs:
    - x : longitude values
    - y : latitude values
    - z : KDE values
    """
    x = lon_end_nonans.copy()
    y = lat_end_nonans.copy()

    xy = np.vstack([x, y])
    z = gaussian_kde(xy)(xy)

    idx = z.argsort()
    x, y, z = x[idx], y[idx], z[idx]

    return x, y, z

def kde_parcels(ds, nsavedir=None):
    """
    Inputs
    ds : xarray dataset of the parcels output netcdf file
    nsavedir: directory where to save the outputs. By default it is None, and will not save outputs.
    If outputs want to be saved specify directory,
    for example: '/data/oceanparcels/output_data/data_LauraGN/outputs_parcels/kde_calcs/'

    Outputs
    KDE for the las timestep fields of lon and lat
    """

    # Remove nans:
    lon_end_nonans, lat_end_nonans = rem_nans(ds)

    kde_x, kde_y, kde_z = kde_vals(lon_end_nonans, lat_end_nonans)

    if nsavedir:
        savename = savedir + 'KDE_' + nfile.split('/')[-1].split('.nc')[0] + '.npz'
        np.savez(savename, kde_x=kde_x, kde_y=kde_y, kde_z=kde_z)

    return kde_x, kde_y, kde_z
