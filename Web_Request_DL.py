
import requests

print('Beginning file download')

url = 'http://opendata.arcgis.com/agol/arcgis/8def226d1da847d5b6374c911d63878f/2.zip?outSR=%7B%22latestWkid%22%3A6543%2C%22wkid%22%3A103122%7D'
req = requests.get(url)

with open(r'C:\Development_Projects\GIS_Machine_Learning\test.zip', 'wb') as f:
    f.write(req.content)

# Retrieve HTTP meta-data
print(req.status_code)
print(req.headers['content-type'])
print(req.encoding)