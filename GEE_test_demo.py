import ee
import os

os.environ['HTTP_PROXY'] = 'http://127.0.0.1:10801'
os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:10801'

ee.Initialize()
image1 = ee.Image('srtm90_v4')
path = image1.getDownloadUrl({
    'scale': 30,
    'crs': 'EPSG:4326',
    'region': '[[-120, 35], [-119, 35], [-119, 34], [-120, 34]]'
})

print(path)
image = ee.Image('srtm90_v4')
print(image.getInfo())