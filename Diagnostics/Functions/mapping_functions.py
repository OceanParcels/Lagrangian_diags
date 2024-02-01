import numpy as np
from osgeo import osr

def dist_meter(lon_1, lon_2, lat_1, lat_2, radius=None):
    """ calculate the distance between two locations
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
        distance
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

def Haversine_displacement(inlon1, inlon2, inlat1, inlat2):
    """_summary_

    Parameters
    ----------
    inlon1 : _type_
        _description_
    inlon2 : _type_
        _description_
    inlat1 : _type_
        _description_
    inlat2 : _type_
        _description_

    Returns
    -------
    _type_
        _description_
    """
    
    #Convert decimal degrees to Radians:
    lon1 = np.radians(inlon1)
    lat1 = np.radians(inlat1)
    lon2 = np.radians(inlon2)
    lat2 = np.radians(inlat2)

    # if np.isnan([lon1, lon2, lat1, lat2]).any():
    #     return mask_value
    #Implementing Haversine Formula: 
    dlon = np.subtract(lon2, lon1)
    dlat = np.subtract(lat2, lat1)

    a = np.add(np.power(np.sin(np.divide(dlat, 2)), 2),  
                          np.multiply(np.cos(lat1), 
                                      np.multiply(np.cos(lat2), 
                                                  np.power(np.sin(np.divide(dlon, 2)), 2))))
    c = np.multiply(2, np.arcsin(np.sqrt(a)))
    return c
