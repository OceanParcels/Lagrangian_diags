# List of diagnostics

## Distance

Methods 
### Mediod
* Method 1 : [mediod_method01.ipynb](mediod_method01.ipynb)
  * When to use it:
    * to identify a representive trajectory of the whole group

### Center of mass displacement
* Method 1 : [center_of_mass_displacement_method01.ipynb](center_of_mass_displacement_method01.ipynb)
  * When to use it:
    * to construct a representive trajectory of the whole group

### Absolute distance (AD)
* Method 1 : [absolute_distance_method01.ipynb](absolute_distance_method01.ipynb)

$$ AD(x,y,t=T) = r(t=T) - r(t=0) $$

### Cumulative distance (CD)
* Method 1 : [cumulative_distance_method01.ipynb](cumulative_distance_method01.ipynb)

$$ CD(x,y,t=T) = r(t=T) - r(t=0) $$

, where $r(t) = f(x,y)$ and is the position of the particle at time, t.  T is the total time period considered for the distance calculation.

### Center of mass spread
* Method 1 :

### Relative dispersion
* Method 1 :

### Mean cumulative separation distance
* Method 1 :

### Normalized cumulative lagrangian separation
* Method 1 :

### Relative horizontal transport deviation
* Method 1 :

### Cumulative incremental trajectory error
* Method 1 :

### Fréchet distance
* Method 1 :

## Spatial particle distribution 
### Histograms
* Method 1 : [2DHistogram_method01.ipynb](2DHistogram_method01.ipynb)

### Gaussian Kernel Density Estimation (GKDE)
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
