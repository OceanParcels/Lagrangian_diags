import numpy as np
from .mapping_functions import dist_meter, haversine

def mediod(X, Y, spherical=False, robust=True):
    """ calculate which trajectory with least disagreement with all others

    Parameters
    ----------
    X,Y: np.ndarray, size=(m,n), unit={degrees,meters}
        m: individual entity, n: time
    spherical: bool
        when True, then spherical coordinates are given
        otherwise metric plane coordinates are assumed
    robust: bool
        when True, robust statistics are used in the form of the median
        otherwise the mean is used instead

    Returns
    -------
    integer, range=0...m
        index of the trajectory with the least sepration distance between
        all other trajectories
    """
    assert len(set({X.size, Y.size})) == 1
    assert len(set({X.ndim, Y.ndim})) == 1

    X, Y = np.atleast_2d(X), np.atleast_2d(Y)
    m,n = X.shape[:2]
    err = np.zeros((m,))
    for i in range(n):
        X_A, X_B = np.meshgrid(X[:, i], X[:, i])
        Y_A, Y_B = np.meshgrid(Y[:, i], Y[:, i])
        if spherical:
            D = dist_meter(X_A, X_B, Y_A, Y_B)
        else:
            D = np.sqrt((X_A - X_B)**2 + (Y_A - Y_B)**2)
        if robust:
            err += np.median(D, axis=1)
        else:
            err += np.mean(D, axis=1)
    id = np.argmin(err)
    return id

def center_of_mass_displacement(X, Y, X0=None, Y0=None):
    """ see equation (1) in [La08]_.

    Parameters
    ----------
    X,Y: numpy.ndarray, size=(m,n), unit={degrees,meters}
        m: id, n: time
    X0,Y0: {float, numpy.ndarray}
        initial coordinate(s) at the start

    Returns
    -------
    M_x,M_y: np.ndarray, size=(n,), unit={degrees,meters}
        displacement of the center of mass over time for the different axis

    See Also
    --------
    center_of_mass_spread

    References
    ----------
    .. [La08] LaCasce, "Statistics from Lagrangian observations", Progress in
              Oceanography, vol.77(1) pp.1-29, 2008.
    """
    assert len(set({X.size, Y.size})) == 1
    assert len(set({X.ndim, Y.ndim})) == 1

    X,Y = np.atleast_2d(X), np.atleast_2d(Y)
    if X0 is None:
        X0,Y0 = X[:,0], Y[:,0]

    M_x,M_y = np.mean(np.transpose(X.T-X0), axis=0), \
              np.mean(np.transpose(Y.T-Y0), axis=0)
    return M_x,M_y

def center_of_mass_spread(X, Y, X0=None, Y0=None, M_x=None, M_y=None):
    """ see equation (2) in [La08]_.

    Parameters
    ----------
    X,Y: numpy.ndarray, size=(m,n), unit={degrees,meters}
        m: id, n: time
    X0,Y0: {float, numpy.ndarray}
        initial coordinate(s) at the start
    Mx,My: numpy.ndarray, size=(n,)
        first moment of the flock

    Returns
    -------
    D_x,D_y: numpy.ndarray, size=(n,), unit={degrees,meters}
        spread of the center of mass over time for the different spatial axis

    See Also
    --------
    center_of_mass_displacement

    References
    ----------
    .. [La08] LaCasce, "Statistics from Lagrangian observations", Progress in
              Oceanography, vol.77(1) pp.1-29, 2008.
    """
    assert len(set({X.size, Y.size})) == 1
    assert len(set({X.ndim, Y.ndim})) == 1

    X,Y = np.atleast_2d(X), np.atleast_2d(Y)
    if X0 is None:
        X0,Y0 = X[:,0], Y[:,0]
    if M_x is None:
        M_x,M_y = center_of_mass_displacement(X, Y, X0=X0, Y0=Y0)

    def _estimate_dispersion(Z, Z0, M_z):
        m, n = Z.shape[:2]
        D_z = np.sum(np.power( Z \
                               - np.tile(np.atleast_2d(Z0).T,(1, n)) \
                               - np.tile(np.atleast_2d(M_z), (m, 1)),2),
                     axis=0) / (n-1)
        return D_z

    D_x = _estimate_dispersion(X, X0, M_x)
    D_y = _estimate_dispersion(Y, Y0, M_y)
    return D_x, D_y

def absolute_dispersion(X, Y, X0=None, Y0=None):
    """ see equation (2) in [Ha08]_

    Parameters
    ----------
    X,Y: numpy.ndarray, size=(m,n), unit={degrees,meters}
        m: id, n: time
    X0,Y0: {float, numpy.ndarray}
        initial coordinate(s) at the start

    Returns
    -------

    References
    ----------
    .. [Ha08] Haza, et al. "Relative dispersion from a high-resolution coastal
              model of the Adriatic Sea" Ocean Modelling, vol.22(1) pp.48-65,
              2008.
    """
    return

def relative_dispersion(X, Y, X_ref=None, Y_ref=None, leader_id=None,
                        spherical=True):
    """ see equation (3) in [Ha08]_, also known as, the absolute horizontal
    transport deviation (AHTD) [Ku85]_ in atmospheric sciences.

    Parameters
    ----------
    X,Y: numpy.ndarray, size=(m,n), unit={degrees,meters}
        trajectery stack with m: id, n: time
    X_ref,Y_ref: numpy.ndarray, size=(n,)
        reference or leader trajectory
    leader_id: integer, range=0...m
        index of the leader within the trajectery stack {X,Y}
    spherical: bool
        when True, then spherical coordinates are given
        otherwise metric plane coordinates are assumed

    Returns
    -------
    numpy.ndarray, size=(n,), unit=meters
        temporal evolution of the relative dispersion

    References
    ----------
    .. [Ha08] Haza, et al. "Relative dispersion from a high-resolution coastal
              model of the Adriatic Sea" Ocean Modelling, vol.22(1) pp.48-65,
              2008.
    .. [Ku85] Kuo, et al. "The accuracy of trajectory models as revealed by the
              observing system simulation experiments" Monthly weather review,
              vol.113 pp.1852—1867, 1985.
    """
    if leader_id is not None:
        X_ref, Y_ref = X[leader_id,:], Y[leader_id,:]
        X, Y = np.delete(X, leader_id, axis=0), np.delete(Y, leader_id, axis=0)

    if spherical:
        D = dist_meter(X_ref, X, Y_ref, Y) # distance from target
    else:
        D = np.sqrt(np.power(X - X_ref, 2) + np.power(Y - Y_ref, 2))
    D = np.mean(D, axis=0)
    return D

def mean_cumulative_separation_distance(X, Y, X_ref=None, Y_ref=None,
                                        leader_id=None, spherical=True):
    """ see equation (5) in [Mh20]_.

    Parameters
    ----------
    X,Y: numpy.ndarray, size=(m,n), unit={degrees,meters}
        trajectery stack with m: id, n: time
    X_ref,Y_ref: numpy.ndarray, size=(n,)
        reference or leader trajectory
    leader_id: integer, range=0...m
        index of the leader within the trajectery stack {X,Y}
    spherical: bool
        when True, then spherical coordinates are given
        otherwise metric plane coordinates are assumed

    Returns
    -------
    float, unit=meters
        spatial-temporal mean of the separation within the flock

    References
    ----------
    .. [Mh20] van der Mheen, et al. "Depth-dependent correction for wind-driven
              drift current in particle tracking applications." Frontiers in
              marine science vol.7 pp.305, 2020.
    """
    if leader_id is not None:
        X_ref, Y_ref = X[leader_id,:], Y[leader_id,:]
        X, Y = np.delete(X, leader_id, axis=0), np.delete(Y, leader_id, axis=0)

    if spherical:
        D = dist_meter(X_ref, X, Y_ref, Y) # distance from target
    else:
        D = np.sqrt(np.power(X - X_ref, 2) + np.power(Y - Y_ref, 2))

    D = np.sum(D.ravel())
    D /= D.size
    return D

def normalized_cumulative_lagrangian_separation(X, Y, X_ref=None, Y_ref=None,
                                                leader_id=None, spherical=True):
    """ eq. (3) in [LW11]_

    Parameters
    ----------
    X,Y: numpy.ndarray, size=(m,n), unit={degrees,meters}
        trajectery stack with m: id, n: time
    X_ref,Y_ref: numpy.ndarray, size=(n,)
        reference or leader trajectory
    leader_id: integer, range=0...m
        index of the leader within the trajectery stack {X,Y}
    spherical: bool
        when True, then spherical coordinates are given
        otherwise metric plane coordinates are assumed

    Returns
    -------
    numpy.ndarray, size=(m,), unit=meters
        skill score for the different tracks in respect to the leader/reference

    References
    ----------
    .. [LW11] Liu & Weisberg, "Evaluation of trajectory modeling in different
              dynamic regions using normalized cumulative Lagrangian separation"
              Journal of geophysical research, vol.116 pp.C09013, 2011.
    """

    if leader_id is not None:
        X_ref, Y_ref = X[leader_id,:], Y[leader_id,:]
        X, Y = np.delete(X, leader_id, axis=0), np.delete(Y, leader_id, axis=0)

    if spherical:
        D = dist_meter(X_ref, X, Y_ref, Y) # distance from target
        L = dist_meter(X[:,:-1], X[:,1:], Y[:,:-1], Y[:,1:]) # travel distance
    else:
        D = np.sqrt(np.power(X - X_ref, 2) + np.power(Y - Y_ref, 2))
        L = np.sqrt(np.power(X[:,:-1] - X[:,1:], 2) +
                    np.power(Y[:,:-1] - Y[:,1:], 2))
    L = np.c_[np.zeros((L.shape[0],1)), L]
    L_cum = np.cumsum(L, axis=1)

    c = np.divide(np.sum(D, axis=1), np.sum(L_cum, axis=1))
    return c

def relative_horizontal_transport_deviation(X, Y, X_ref=None, Y_ref=None,
                                            leader_id=None, spherical=True):
    """ see also [SW85]_

    Parameters
    ----------
    X,Y: numpy.ndarray, size=(m,n), unit={degrees,meters}
        trajectery stack with m: id, n: time
    X_ref,Y_ref: numpy.ndarray, size=(n,)
        reference or leader trajectory
    leader_id: integer, range=0...m
        index of the leader within the trajectery stack {X,Y}
    spherical: bool
        when True, then spherical coordinates are given
        otherwise metric plane coordinates are assumed

    Returns
    -------
    numpy.ndarray, size=(n,), unit=meters
        temporal evolution of the relative dispersion

    References
    ----------
    .. [SW85] Stohl & Wotawa, "A method for computing single trajectories
              representing boundary layer transport" Atmospheric environment,
              vol.29 pp.3235—3239, 1995.
    """
    if leader_id is not None:
        X_ref, Y_ref = X[leader_id,:], Y[leader_id,:]
        X, Y = np.delete(X, leader_id, axis=0), np.delete(Y, leader_id, axis=0)

    if spherical:
        D = dist_meter(X_ref, X, Y_ref, Y) # distance from target
        L = dist_meter(X_ref[:-1], X_ref[1:], Y_ref[:-1], Y_ref[1:])
    else:
        D = np.sqrt(np.power(X - X_ref, 2) + np.power(Y - Y_ref, 2))
        L = np.sqrt(np.power(X_ref[:-1] - X_ref[1:], 2) +
                    np.power(Y_ref[:-1] - Y_ref[1:], 2))
    L = np.cumsum(L)
    D = np.mean(D, axis=0)
    return

def cumulative_incremental_trajectory_error(X, Y, dX=None, dY=None,
                                            X_ref=None, Y_ref=None,
                                            leader_id=None, spherical=True):
    """ see equation (3) in [Ri06]_.

    References
    ----------
    .. [Ri06] Riddle, et al. "Trajectory model validation using newly developed
              altitude-controlled balloons during the international consortium
              for atmospheric research on transport and transformations 2004
              campaign" Journal of geophysical research - atmospheres vol.111
              pp.D23, 2006.
    """
    if leader_id is not None:
        X_ref, Y_ref = X[leader_id,:], Y[leader_id,:]
        X, Y = np.delete(X, leader_id, axis=0), np.delete(Y, leader_id, axis=0)

    # get heading
    if dX is None:
        dX, dY = X[:,:-1] - X[:,1:], Y[:,:-1] - Y[:,1:]

    dX_ref, dY_ref = X_ref[:-1] - X_ref[1:], Y_ref[:-1] - Y_ref[1:]

    if spherical:
        dE = haversine(dX-dX_ref, dY-dY_ref, Y[:,:-1])
    else:
        dE = np.sqrt(np.power(dX - dX_ref, 2) + np.power(dY - dY_ref, 2))
    dE = np.sum(dE, axis=1)
    return dE

def frechet_dist(X, Y, spherical=True):
    """ Fréchet distance, typically it is defined for polygons or polylines.
    The distance is typically explained as a "dog on a leash" measure. Where,
    the geometry is traverse, and the longest separation distance is taken.
    However, in this case the data is ordered along time, see also [LN13]_.
    Hence, here the separation distance at each time step is analysed and the
    maximum distance is kept.

    Parameters
    ----------
    X,Y: np.ndarray, size=(m,n), unit={degrees,meters}
        m: id, n: time

    Returns
    -------
    np.ndarray, size=(n,), unit=meters
        maximum separation distance for each time step

    References
    ----------
    .. [LN13] Long & Nelson, "A review of quantitative methods for movement
              data" International journal of geographic information science,
              vol.23(2) pp.292-318, 2013.
    """
    assert len(set({X.size, Y.size})) == 1
    assert len(set({X.ndim, Y.ndim})) == 1

    X, Y = np.atleast_2d(X), np.atleast_2d(Y)
    m,n = X.shape[:2]
    fréchet = np.zeros((n,))
    for i in range(n):
        X_A, X_B = np.meshgrid(X[:, i], X[:, i])
        Y_A, Y_B = np.meshgrid(Y[:, i], Y[:, i])
        if spherical:
            D = dist_meter(X_A, X_B, Y_A, Y_B)
        else:
            D = np.sqrt(np.power(X_A - X_B, 2) + np.power(Y_A - Y_B, 2))
        fréchet[i] = np.max(D)
    return fréchet

def hausdorff_dist(X, Y, spherical=True):
    assert len(set({X.size, Y.size})) == 1
    assert len(set({X.ndim, Y.ndim})) == 1

    X, Y = np.atleast_2d(X), np.atleast_2d(Y)
    m,n = X.shape[:2]
    hausdorff = np.zeros((n,))
    for i in range(n):
        X_A, X_B = np.meshgrid(X[:, i], X[:, i])
        Y_A, Y_B = np.meshgrid(Y[:, i], Y[:, i])
        if spherical:
            D = dist_meter(X_A, X_B, Y_A, Y_B)
        else:
            D = np.sqrt(np.power(X_A - X_B, 2) + np.power(Y_A - Y_B, 2))
        hausdorff[i] = np.min(np.max(D, axis=1), axis=0)
    return hausdorff
