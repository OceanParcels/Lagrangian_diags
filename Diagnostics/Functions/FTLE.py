import numpy as np
import numpy.linalg as LA
import Haversine_distance


def ftle_brunton_2009(J, Td):  # http://cwrowley.princeton.edu/papers/BruntonChaos09.pdf
    D = np.dot(np.transpose(J), J)  # Cauchy–Green strain tensor
    lamda = LA.eigvals(D)
    lam_max = max(lamda)
    ftle = (1 / Td) * np.log(np.sqrt(lam_max))
    return ftle

def compute_ftle(x0,y0,x1,y1, Td):

    H = x0.shape[0]
    L = x1.shape[1]

    FTLE_f = np.ones_like(np.asarray(x0))
    FTLE_f[:,:] = np.NaN

    J = np.empty([2, 2], float)

    # 1, H-1 --> to ignore bordersx for now
    for i in range(1, H - 1):  # 0, H-2
        for j in range(1, L - 1):  # 0, L-2
            J [:,:] = np.NaN
            J[0][0] = Haversine_distance.dist_pairs_km(x1[i, j], x1[i - 1, j], y1[i, j], y1[i - 1, j]) / Haversine_distance.dist_pairs_km(x0[i, j], x0[i - 1, j],
                                                                                                    y0[i, j], y0[i - 1, j])
            J[0][1] = Haversine_distance.dist_pairs_km(x1[i, j], x1[i, j - 1], y1[i, j], y1[i, j - 1]) / Haversine_distance.dist_pairs_km(x0[i, j], x0[i, j - 1],
                                                                                                    y0[i, j], y0[i, j - 1])
            J[1][0] = Haversine_distance.dist_pairs_km(x1[i, j], x1[i, j + 1], y1[i, j], y1[i, j + 1]) / Haversine_distance.dist_pairs_km(x0[i, j], x0[i, j + 1],
                                                                                                    y0[i, j], y0[i, j + 1])
            J[1][1] = Haversine_distance.dist_pairs_km(x1[i, j], x1[i + 1, j], y1[i, j], y1[i + 1, j]) / Haversine_distance.dist_pairs_km(x0[i, j], x0[i + 1, j],
                                                                                                    y0[i, j], y0[i + 1, j])

            if np.isnan(J).any():
                continue
            elif np.all((J == 1.0)):  # identify all land points- static points: No dispersion?
                continue
            else:
                f_value = ftle_brunton_2009(J, Td)
                FTLE_f[i][j] = f_value
    return FTLE_f