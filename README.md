# simple_geopandas_map_coords
Creates a basic vector world map with cities plotted using coordinates explicitly written into the Python script.

## geopandas.dataset v. geodatasets
It was challenging to find solutions that showed the correct way to resolve the AttributeError "The geopandas.dataset has been deprecated and was removed in GeoPandas 1.0.". To save others the same headache, a quick note on how to do this:

### GeoPandas (Deprecated)
`geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))`

### geodatasets (Current)
`geopandas.read_file(geodatasets.get_url('naturalearth.land'))`

# Pivotal Resources
These resources were pivotal in learning the concepts needed to develop this repo:

- [Creating a GeoDataFrame from a DataFrame with coordinates](https://geopandas.org/en/stable/gallery/create_geopandas_from_pandas.html)
- [How to Plot a World Map Using Python and GeoPandas](https://naturaldisasters.ai/posts/python-geopandas-world-map-tutorial/)
- [Plot Latitude and Longitude from Pandas DataFrame in Python  ](https://datascientyst.com/plot-latitude-longitude-pandas-dataframe-python/)
- [Connecting Pandas to a Database with SQLAlchemy](https://www.geeksforgeeks.org/connecting-pandas-to-a-database-with-sqlalchemy/)
- [geodatasets](https://geodatasets.readthedocs.io/en/latest/)
- [geodatasets GitHub Repo](https://github.com/geopandas/geodatasets)
