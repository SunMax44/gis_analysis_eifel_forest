import rasterio
import numpy as np
import pandas as pd

# Define the path to your raster
raster_path = "/Users/maxsonntag/Documents/GIS Class/EiffelRasterProject/gis_analysis_eifel_forest/data/dhm_cleaned_0s.tif"

# Open the raster and read data
with rasterio.open(raster_path) as src:
    chm_array = src.read(1)  # Read first band
    nodata_value = src.nodata  # Get NoData value
    transform = src.transform  # Spatial transformation (if needed)

# Convert NoData values to NaN (optional)
if nodata_value is not None:
    chm_array = np.where(chm_array == nodata_value, np.nan, chm_array)

# Flatten the array for Pandas (convert raster grid to 1D)
chm_flat = chm_array.flatten()

# Create a Pandas DataFrame
df = pd.DataFrame({"Canopy_Height": chm_flat})

# Drop NaN values (optional)
df_cleaned = df.dropna()

# Print summary statistics
print(df_cleaned.describe())

# Save as CSV if needed
df_cleaned.to_csv("/Users/maxsonntag/Documents/GIS Class/EiffelRasterProject/gis_analysis_eifel_forest/data/dhm_values.csv", index=False)
