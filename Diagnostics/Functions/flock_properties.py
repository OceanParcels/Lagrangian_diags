import numpy as np

from .geometry_functions import point_advancement_irt_heading, \
    point_direction_irt_line, perpendicular_to_heading, \
    parallel_to_heading

def flock_heading(ψ, axis=0):
    """ estimate the mean orientation of a group of trajectories

    Parameters
    ----------
    ψ : numpy.ndarray, ndim=2, unit=degrees
        array with arguments (direction angle  in respect to North), over
        different timestamps
    axis : integer
        specifies which axis has the flock, while the other axis specifies the
        temporal dimension

    Returns
    -------
    numpy.ndarray, unit=degrees, range=0...360
        array with mean heading over time
    """
    C, S = np.nanmean(np.cos(np.deg2rad(ψ)), axis=axis), \
           np.nanmean(np.sin(np.deg2rad(ψ)), axis=axis)
    θ = np.rad2deg(np.arctan2(S, C))
    θ = θ % 360 # bring to compass range: 0 ... 360
    return θ

def flock_mean(X, Y, axis=0):
    """ get the mean location of a group over time

    Parameters
    ----------
    X,Y : numpy.ndarray, ndim=2
        coordinates of the flock, where one axis have the different actors,
        while the other is the temporal dimension
    axis : integer
        specifies which axis has the flock, while the other axis specifies the
        temporal dimension

    Returns
    -------
    x,y : numpy.ndarray, ndim=1
        coordinates of the mean flock location over time
    """
    assert len(set({X.size, Y.size})) == 1
    assert len(set({X.ndim, Y.ndim})) == 1
    x = np.nanmean(X, axis=axis)
    y = np.nanmean(Y, axis=axis)
    return x, y

def flock_spread(X, Y, axis=0):
    """ estimate the major spread and direction of a flock, see [Is09]_.

    Parameters
    ----------
    X,Y : numpy.ndarray, ndim=2
        coordinates of the flock, where one axis have the different actors,
        while the other is the temporal dimension
    axis : integer
        specifies which axis has the flock, while the other axis specifies the
        temporal dimension

    Returns
    -------
    θ : numpy.ndarray, ndim=1, unit=degrees
        orientation of the major axis of variance
    σ : numpy.ndarray, ndim=1
        magnitude of the particle position variance

    References
    ----------
    .. [Is09] Isobe et al. "Two-way particle tracking model for specifying
              sources of drifting objects: Application to the east China sea
              shelf" Journal of atmospheric and oceanic technology, vol.26(8)
              pp.1672-1682, 2009.
    """
    sixa = np.mod(axis+1,2)
    x_bar,y_bar = flock_mean(X, Y, axis=axis)
    x_bar, y_bar = np.atleast_2d(x_bar), np.atleast_2d(y_bar)
    x_bar, y_bar = np.repeat(x_bar, X.shape[sixa], axis=sixa), \
                   np.repeat(x_bar, X.shape[sixa], axis=sixa)

    x, y = X-x_bar, Y-y_bar

    # equation 2.1 in [Is09]_
    θ = .5 * np.arctan(np.divide(2*np.sum(x*y, axis=axis),
                                 x**2 - y**2))
    ax = 1 if axis==0 else 0

    # equation A.1 in [Is09]_
    σ = np.mean((x*np.cos(θ) + y*np.cos(θ))**2, axis=ax)
    θ = np.rad2deg(θ)
    return σ, θ

def flock_leader(X, Y, X_ref, Y_ref, Dir):
    """ get the index of the leader as a function of time

    Parameters
    ----------
    X,Y : numpy.ndarray, ndim=2, dtype=float
        coordinates of the flock, where one axis have the different actors,
        while the other is the temporal dimension

    Returns
    -------
    numpy.ndarray, dtype=int
        index of the leader as a function of time
    """
    assert len(set({X.size, Y.size})) == 1
    assert len(set({X.ndim, Y.ndim})) == 1
    assert len(set({X_ref.size, Y_ref.size, Dir.size})) == 1

    L = np.zeros(Dir.shape, dtype=np.int32)
    for idx, heading in enumerate(Dir):
        e_perp = perpendicular_to_heading(heading, direction='right')
        dist = point_advancement_irt_heading(np.array([X_ref[idx], Y_ref[idx]]),
             e_perp, np.column_stack([X[:,idx], Y[:,idx]]))
        L[idx] = np.argmax(dist)
    return L

def flock_orientation_irt_leader(X, Y, L, Dir):
    """ estimate the orientation of group members in relation to the leader

    Parameters
    ----------
    X,Y : numpy.ndarray, ndim=2, dtype=float
        coordinates of the flock, where one axis have the different actors,
        while the other is the temporal dimension
    L : numpy.ndarray, dtype=int
        index of the leader as a function of time
    Dir : numpy.ndarray, dtype=float, unit=angle
        heading of the group

    Returns
    -------
    numpy.ndarray, dtype=integer
        filled grid specifying if the actor is either leader (0), left (+1) or
        right (-1) of the leader, as this progresses through time

    See Also
    --------
    flock_leader, flock_heading, flock_order_irt_leader
    """
    # estimate if trajectories are left or right i.r.t. its leader

    D = np.zeros(X.shape, dtype=np.int32)
    for idx, heading in enumerate(Dir):
        e_para = parallel_to_heading(heading)
        p = np.array([X[L[idx], idx], Y[L[idx], idx]])
        lhrh = point_direction_irt_line(p, p+e_para,
                                        np.column_stack([X[:,idx], Y[:,idx]]))
        D[:,idx] = lhrh
    return D

def flock_order_irt_leader(X, Y, L, Dir):
    """ estimate the orientation of group members in relation to the leader

    Parameters
    ----------
    X,Y : numpy.ndarray, ndim=2, dtype=float
        coordinates of the flock, where one axis have the different actors,
        while the other is the temporal dimension
    L : numpy.ndarray, dtype=int
        index of the leader as a function of time
    Dir : numpy.ndarray, dtype=float, unit=angle
        heading of the group

    Returns
    -------
    numpy.ndarray, dtype=integer
        filled grid specifying if the actor is either leader (0), left (+1) or
        right (-1) of the leader, as this progresses through time

    See Also
    --------
    flock_leader, flock_heading, flock_orientation_irt_leader
    """
    m = X.shape[0]
    Ord = np.zeros(X.shape, dtype=np.int32)
    for idx, heading in enumerate(Dir):
        e_para = parallel_to_heading(heading)
        p = np.array([X[L[idx], idx], Y[L[idx], idx]])
        dist_perp = point_advancement_irt_heading(p, e_para,
            np.column_stack([X[:,idx], Y[:,idx]]))
        idx_ord = np.argsort(dist_perp)
        idx_off = np.where(idx_ord==L[idx])[0][0]
        Ord[idx_ord,idx] = np.arange(m) - idx_off
    return Ord

def formation_stability(v_x, v_y):
    """ the average of the magnitudes of the velocity difference of each entity
    and the group, that is the variance, see also [He97]_ and [Vi04]_.

    Parameters
    ----------
    v_x,v_y : numpy.ndarray
        velocity in planar coordinates

    Returns
    -------
    numpy.ndarray, dtype=float

    References
    ----------
    .. [He97] Heppner, "Three-dimensional structure and dynamics of bird
              flocks." Animal groups in three dimensions, pp.68-89, 1997.
    .. [Vi04] Viscido, et al. "Individual behavior and emergent properties of
              fish schools: a comparison of observation and theory." Marine
              ecology progress series vol.273 pp.239-249, 2004.
    """
    speed = np.hypot(v_x, v_y)
    return np.nanvar(speed, axis=0)

#todo: flock_density
# estimate the alpha-shape or convex-hull
