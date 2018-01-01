# This is a simple file downloader in which all you have to give is the url of the file to be downloaded and its type(Eg: pdf,jpg)
# Demo Input:
# url = http://newsonair.nic.in/GST_FAQ.pdf
# filetype = pdf


import urllib.request
from pip._vendor.distlib.compat import raw_input

def download_web(url,filetype):
    name = "downloadedFile"
    fullname = name + "."+ filetype
    urllib.request.urlretrieve(url, fullname)
  

url = raw_input("enter the url from where you want to download")
type(url)
filetype = raw_input("enter the fileType")
type(filetype)

download_web(url,filetype)