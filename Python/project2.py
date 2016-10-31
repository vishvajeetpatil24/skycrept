import sys
sys.path = sys.path[1:]
import urllib.request
import random
import os
from PIL import Image
def image_download(url):
	urllib.request.getproxies()
	fname = str(random.randrange(1,1000))+".jpg"
	urllib.request.urlretrieve(url,fname)
	try:
		im = Image.open(fname)
		im.thumbnail((700,700),Image.ANTIALIAS)
		os.remove(fname)
		im.save(fname,"JPEG")
	except:
		print("Error occured")

image_download("https://upload.wikimedia.org/wikipedia/commons/4/49/Emma_Watson_2012.jpg")