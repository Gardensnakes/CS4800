# Import requests, shutil python module.
import requests
import shutil
from os.path import join as pjoin

def download(name,link):

	# # This is the image url.
	# image_url = link
	# # Open the url image, set stream to True, this will return the stream content.
	# resp = requests.get(image_url, stream=True)
	# # Open a local file with wb ( write binary ) permission.
	# filename = name + '.jpg'
	# # path_to_file = pjoin("C:", "foo", "bar", "baz", filename)
	# local_file = open(filename , 'wb')
	# # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
	# resp.raw.decode_content = True
	# # Copy the response stream raw data to local image file.
	# shutil.copyfileobj(resp.raw, local_file)
	# # Remove the image url response object.
	# del resp


	f = open(name + '.jpg','wb')
	f.write(requests.get(link).content)
	f.close()


