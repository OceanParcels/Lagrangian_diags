import numpy as np
import xarray as xr
import scipy
import h3
from h3.unstable import vect


class initGrid:
    """
    Initialize a hexagonal grid for a particle generation on a given domain.
    """

    def __init__(self, polygon, h3_res=5):
        """
        Initialize a hexagonal grid for a particle generation on a given domain.

        Parameters
        ----------
        polygon : dict
            A dictionary with the geoJSON polygon coordinates of the domain.
        h3_res : int
            The Uber H3 resolution of the hexagonal grid.
        """
        self.polygon = polygon
        self.h3_res = h3_res
        self.hexagons = list(h3.polyfill(polygon, h3_res))
        self.process_hexagons()
    
    def process_hexagons(self):
        """
        Process the hexagons to integer labels and their centroids.
        """
        self.hexint = np.array([int(a, 16) for a in self.hexagons])
        self.centroids = [h3.h3_to_geo(hex) for hex in self.hexagons]
        self.centroid_lats = np.array([c[0] for c in self.centroids])
        self.centroid_lons = np.array([c[1] for c in self.centroids])
        
    @property
    def size(self):
        """
        Returns the number of particles/hexagons.
        """
        return len(self.hexagons)

    @property
    def lonlat(self):
        """
        Returns a stacked version of the longitudes and latitudes
        """
        return np.column_stack((self.centroid_lons, self.centroid_lats))

    def mask(self, mask_lons, mask_lats, mask):
        """
        Mask the particles using a given mask, for instance to get rid of particles on land.

        Parameters
        ----------
        mask_lons : xarray.DataArray
            The longitudes of the mask.
        mask_lats : xarray.DataArray
            The latitudes of the mask.

        """

        if type(mask_lons) == xr.DataArray:
            mask_lons = mask_lons.values
        if type(mask_lats) == xr.DataArray:
            mask_lats = mask_lats.values
        if type(mask) == xr.DataArray:
            mask = mask.values

        self.lonlatMask = scipy.interpolate.griddata(np.column_stack((mask_lons.flatten(), mask_lats.flatten())), 
                                                     mask.flatten(), 
                                                     self.lonlat, 
                                                     method='nearest')

        
        self.hexagons = np.array(self.hexagons)[self.lonlatMask].tolist()
        self.process_hexagons()

    @property
    def lonlat_dict(self):
        return {"lon": self.centroid_lons, "lat": self.centroid_lats, "uber_h3_res": self.h3_res}
