import numpy as np
from math import sin, cos, sqrt, atan2, radians, pi

def dist_km(lona, lonb, lata, latb):
    """
    Function to calculate the distance between 2 points in km
    Haversine formula used, which assumes the Earth is a sphere.
    source: https://stackoverflow.com/questions/19412462/getting-distance-between-two-points-based-on-latitude-longitude
    """

    R = 6373.0     # approximate radius of earth in km

    lat1 = radians(lata)
    lon1 = radians(lona)
    lat2 = radians(latb)
    lon2 = radians(lonb)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    return distance

def cumulative_distance_01(ds_n, nsavedir=None):

    # Creating the output data array:
    dist_01 = ds_n.lon.copy() * np.nan

    # Calculating the distance traveled by every particle at every timestep:
    for tt in range(0, len(ds_n.traj)):
        lon_t = ds_n.lon[tt, :].dropna(dim='obs')
        lat_t = ds_n.lat[tt, :].dropna(dim='obs')

        for oo in range(1, len(lat_t)): # calculate as distance at x0 = distance at x-x0
            dist_01[tt, oo-1] = dist_km(lon_t[oo-1], lon_t[oo], lat_t[oo-1], lat_t[oo])

    # Calculating the cumulative distance traveled for all particle trajectories at every timestep:
    cum_dist_01 = dist_01.cumsum(dim='obs')

    if nsavedir:
        cum_dist_01.to_netcdf(nsavedir + "cum_dist_01.nc")

    return cum_dist_01
