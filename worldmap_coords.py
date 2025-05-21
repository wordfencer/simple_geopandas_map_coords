import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import geodatasets


# create Pandas DataFrame
df = pd.DataFrame(
    {
        "City": ["Buenos Aires", "Brasilia", "Santiago", "Bogota", "Caracas"],
        "Country": ["Argentina", "Brazil", "Chile", "Colombia", "Venezuela"],
        "Latitude": [-34.58, -15.78, -33.45, 4.60, 10.48],
        "Longitude": [-58.66, -47.91, -70.66, -74.08, -66.86],
    }
)

# create geopandas GeoDataFrame
# Latitude & Longitude are converted into a list of shapely.Point objects
# crs value explicit declaration that the geometry data defines latitude/longitude world geodetic degree values
gdf = gpd.GeoDataFrame(
    df, geometry=gpd.points_from_xy(df.Longitude, df.Latitude), crs="EPSG:4326"
)

# create the background map
# load the low resolution world map
world = gpd.read_file(geodatasets.get_url('naturalearth.land'))
# set the map attributes
ax = world.plot(figsize=(20, 10), color="lightgray", edgecolor="black", alpha=0.5)

# set the plot title
plt.title("Our Stores")

# turn off axis ticks
ax.set_xticks([])
ax.set_yticks([])

# plot the GeoDataFrame
gdf.plot(ax=ax, color="red")

plt.show()