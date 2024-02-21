import numpy as np

def point_orientation(p, q, r):
    """ define if a point is left or right of a directed line, given by p
    towards q

    Parameters
    ----------
    p,q : numpy.ndarray, size=(2,)
        two dimensional points specifing a line
    r : numpy.ndarray, size=(m,2)
        two dimensional points

    Returns
    -------
    det : numpy.ndarray, size=(m,2), dtype=float
        normalized and oriented separation distance
    """
    det = (p[0]*q[1] - p[1]*q[0]) + \
          (p[1]*r[...,0] - p[0]*r[...,1]) + \
          (q[0]*r[...,1] - q[1]*r[...,0])
    return det

def point_direction_irt_line(p,q,r):
    """ define if a point is left or right of a directed line, given by p
    towards q

    Parameters
    ----------
    p,q : numpy.ndarray, size=(2,)
        two dimensional points specifing a line
    r : numpy.ndarray, size=(m,2)
        array with two dimensional points

    Returns
    -------
    dir : {-1,0,+1}, numpy.ndarray, size=(m,2)
        specifies the side where a point is situated in respect to the line

    See Also
    --------
    point_distance_irt_line
    """
    dir = np.sign(point_orientation(p,q,r))
    return dir

def point_distance_irt_line(p, q, r):
    """ calculate the perpendicular distance of a point in respect to a
    directed line, given by 'p' towards 'q'

    Parameters
    ----------
    p,q : numpy.ndarray, size=(2,)
        two dimensional points specifing a line
    r : numpy.ndarray, size=(m,2)
        array with two dimensional points

    Returns
    -------
    dis : numpy.ndarray, size=(m,2), dtype=float
        perpendicular distance of the point in respect to the line

    See Also
    --------
    point_direction_irt_line
    """
    dis_pq = np.linalg.norm(np.diff(np.column_stack([p, q]), axis=1))
    dis = np.divide(np.abs(point_orientation(p, q, r)), dis_pq)
    return dis

def segment_intersection(p,q,r,s):
    """ calculate if two segments intersect

    Parameters
    ----------
    p,q : numpy.ndarray, size=(2,)
        two dimensional points specifing a line
    r,s : numpy.ndarray, size=(m,2)
        array with two dimensional points specifying line-segments

    Returns
    -------
    numpy.ndarray, size=(m,), dtype=bool
        array with verdict if a crossing is present
    """

    t = np.divide((p[0] - r[...,0]) * (r[...,1] - s[...,1]) -
                  (p[1] - r[...,1]) * (r[...,0] - s[...,0]),
                  (p[0] - q[0]) * (r[..., 1] - s[..., 1]) -
                  (p[1] - q[1]) * (r[..., 0] - s[..., 0])
                  )
    u = np.divide((p[0] - r[...,0]) * (p[1] - q[1]) -
                  (p[1] - r[...,1]) * (p[0] - q[0]),
                  (p[0] - q[0]) * (r[..., 1] - s[..., 1]) -
                  (p[1] - q[1]) * (r[..., 0] - s[..., 0])
                  )
    x = np.logical_and(0<=t<=1, 0<=u<=1)
    return x

def point_advancement_irt_heading(p, e, r):
    """

    Parameters
    ----------
    p : np.ndarray, size=(1,2)
        point of interest
    e : np.ndarray, size=(1,2)
        unit-vector specifying the direction
    r : np.ndarray, size=(m,2)
        points to be assessed

    Returns
    -------
    np.ndarray, size=(m,)
        distance either in forward (positive) or reverse direction (negative)
    """
    if np.linalg.norm(e)!=1:
        e /= np.linalg.norm(e) # make vector unit length

    dis = point_orientation(p, p + e, r)
    return dis

def perpendicular_to_heading(ψ, axis='xy', direction='left'):
    """ return an array or a unit vector, given the direction

    Parameters
    ----------
    ψ : numpy.array, unit=degrees
        array with directions, or headings
    axis : {'xy', 'ij'}
        the coordinate frame, either metric ('xy') or image based ('ij')
    direction : {'left', 'right'}
        orientation where the unit vector points towards

    Returns
    -------
    numpy.array
        array with unit-vectors in the direction of the heading

    See Also
    --------
    parallel_to_heading
    """
    if direction in ('left', 'l',):
        ψ += 270
    else:
        ψ += 90

    e_perp = parallel_to_heading(ψ, axis=axis)
    return e_perp

def parallel_to_heading(ψ, axis='xy'):
    """ return an array or a unit vector, given the direction

    Parameters
    ----------
    ψ : numpy.array, unit=degrees
        array with directions, or headings
    axis : {'xy', 'ij'}
        the coordinate frame, either metric ('xy') or image based ('ij')

    Returns
    -------
    numpy.array
        array with unit-vectors in the direction of the heading

    See Also
    --------
    perpendicular_to_heading
    """
    if axis in ('xy', 'metric'):
        e_para = np.array([+np.sin(np.deg2rad(ψ)),
                           +np.cos(np.deg2rad(ψ))])
    else: # 'ij' 'image'
        e_para = np.array([-np.cos(np.deg2rad(ψ)),
                           +np.sin(np.deg2rad(ψ))])
    return e_para
