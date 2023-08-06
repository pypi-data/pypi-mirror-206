# H-transport-materials
[![DOI](https://zenodo.org/badge/488195123.svg)](https://zenodo.org/badge/latestdoi/488195123)
![CI](https://github.com/RemDelaporteMathurin/h_transport_materials/actions/workflows/ci.yml/badge.svg)
[![codecov](https://codecov.io/github/RemDelaporteMathurin/h-transport-materials/branch/main/graph/badge.svg?token=zroa7Y8If6)](https://codecov.io/github/RemDelaporteMathurin/h-transport-materials)

## Installation

```
pip install h-transport-materials
```

## Usage

1. [Access the internal database](#access-the-internal-database)  
2. [Add custom properties](#add-custom-properties)  
3. [Filters](#filters)  
4. [Compute mean values](#compute-mean-values)  
5. [Export to BibTeX](#export-to-bibtex)  


### Access the internal database
```python
import h_transport_materials as htm
import matplotlib.pyplot as plt

# filter only tungsten and H
diffusivities = htm.diffusivities.filter(material="tungsten").filter(isotope="h")

htm.plotting.plot(diffusivities)


plt.yscale("log")
plt.ylabel("Diffusivity (m$^2$/s)")
plt.legend()
plt.show()
```
![Figure_1](https://user-images.githubusercontent.com/40028739/213814746-9dadb8dc-599e-4004-8135-e496b19fd8bc.png)

>
### Add custom properties

```python
import h_transport_materials as htm

import numpy as np

# Create a custom property
my_custom_property = htm.ArrheniusProperty(pre_exp=1e-5, act_energy=0.2)

# From (T, y) data
my_fitted_property = htm.ArrheniusProperty(
    data_T=[300, 400, 500, 600],
    data_y=[1e-8, 1e-7, 1e-6, 1e-5],
)

print("Pre-exponential factor: {:.2e}".format(my_fitted_property.pre_exp))
print("Activation energy: {:.2f} eV".format(my_fitted_property.act_energy))

# Pre-exponential factor: 4.40e-03
# Activation energy: 0.35 eV
```

### Filters

```python
import h_transport_materials as htm

# tungsten solubilities
htm.solubilities.filter(material="tungsten")

# copper and cucrzr solubilities
htm.solubilities.filter(material=["copper", "cucrzr"])

# all_authors_except_ryabchikov
htm.diffusivities.filter(material="tungsten").filter(author="ryabchikov", exclude=True)

# only Tritium
htm.diffusivities.filter(isotope="t")
```

### Compute mean values

```python
import h_transport_materials as htm
import matplotlib.pyplot as plt

tungsten_diffusivities = htm.diffusivities.filter(material="tungsten").filter(
    author=["moore", "zakharov"], exclude=True
)

# compute mean diffusivity
mean_diffusivity = tungsten_diffusivities.mean()

# plot
htm.plotting.plot(tungsten_diffusivities, alpha=0.5)

htm.plotting.plot(mean_diffusivity, color="black", linewidth=3)

x_annotation = 0.0034
plt.annotate("mean value", (x_annotation, mean_diffusivity.value(T=1 / x_annotation)))

plt.ylabel("Diffusivity (m$^2$ s$^{-1}$)")
plt.yscale("log")
plt.show()
```
![Figure_1](https://user-images.githubusercontent.com/40028739/169285178-7cccc183-8ae1-4afe-8e4e-af2d54ac8741.svg)

### Export to BibTeX

The refernces of properties and properties groups can be exported to a bibfile.

```python
import h_transport_materials as htm

tungsten_diffusivities = htm.diffusivities.filter(material="tungsten")

tungsten_diffusivities.export_bib("my_bibfile.bib")

```


# Contributions

The current database is far from complete.
[Contributions](https://github.com/RemDelaporteMathurin/h-transport-materials/issues/new) are most welcome to extend it by adding new properties and also new materials!
