import numpy as np
from osgeo import osr

def dist_meter(lon_1, lon_2, lat_1, lat_2, radius=None):
    """ calculate the distance between two locations

    Parameters
    ----------
    lon_1, lat_1 : float, unit=degrees
        location of point 1
    lon_2, lat_2 : float, unit=degrees
        location of point 2
    radius : bool, , unit=meters, default=None
        estimate of the radius of the Earth

    Returns
    -------
    float, unit=meters
    """
    Δlon, Δlat = lon_2 - lon_1, lat_2 - lat_1
    lat_mean = (lat_1+lat_2)/2

    distance = haversine(Δlat, Δlon, lat_mean, radius=radius)
    return distance

def haversine(Δlat, Δlon, lat, radius=None):
    """ calculate the distance along a great-circle

    Parameters
    ----------
    Δlat, Δlon : float, unit=degrees
        step size or angle difference
    lat : float, unit=degrees
        (mean) latitude where angles are situated
    radius : float, unit=meters
        estimate of the radius of the earth

    Returns
    -------
    float, unit=meters
    """
    Δlat, Δlon, lat = np.deg2rad(Δlat), np.deg2rad(Δlon), np.deg2rad(lat)

    if radius is None:
        wgs84 = osr.SpatialReference()
        wgs84.ImportFromEPSG(4326)
        a,b = wgs84.GetSemiMajor(), wgs84.GetSemiMinor()
        radius = np.sqrt(np.divide((a**2*np.cos(lat))**2 +
                                   (b**2*np.sin(lat))**2,
                                   (a*np.cos(lat))**2 + (b*np.sin(lat))**2)
                         )

    a = np.sin(Δlat / 2) ** 2 + \
        np.cos(lat) * np.cos(lat+Δlat) * np.sin(Δlon / 2) ** 2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a)) # great circle distance
    d = radius * c
    return d

