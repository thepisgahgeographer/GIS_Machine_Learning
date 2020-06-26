from arcgis.gis import GIS
from arcgis.features import FeatureLayer
import pandas as pd

portal = GIS("https://www.arcgis.com")

fs_url = "https://services7.arcgis.com/F4iYwOOvXLYhkPXF/ArcGIS/rest/services/USFS_Nantahala_Pisgah_Trails_updated/FeatureServer/1"
fs = FeatureLayer(fs_url)
fs

#for f in fs.properties.fields:
#    print(f['name'])

query1 = fs.query(where="Trail_Name='LINVILLE GORGE'").sdf
query1

query1.to_csv(r"C:\Users\yuri7100\Desktop\test\test.csv")

