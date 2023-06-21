# List of diagnostics

## Distance
### Absolute distance (AD)
* Method 1 : [absolute_distance_method01.ipynb](absolute_distance_method01.ipynb)

$$ AD(x,y,t=T) = r(t=T) - r(t=0) $$

### Cumulative distance (CD)
* Method 1 : [cumulative_distance_method01.ipynb](cumulative_distance_method01.ipynb)

$$ CD(x,y,t=T) = r(t=T) - r(t=0) $$

, where $r(t) = f(x,y)$ and is the position of the particle at time, t.  T is the total time period considered for the distance calculation.

## Spatial particle distribution 
### Histograms
* Method 1 : [2DHistogram_method01.ipynb](2DHistogram_method01.ipynb)

### Gaussian Kernel Density Estimation
* Method 1 : [GKDE_method01.ipynb](GKDE_method01.ipynb)
  * When to use it:
    * Example
  * Alternative methods:
    * Histograms
  * Papers where the method is applied:
    * Example
* Method 2 : [GKDE_method02.ipynb](GKDE_method02.ipynb)

## Lyapunov exponents
* Method 1: https://github.com/LauraGomezNavarro/OceanParcels_Lyapunov
