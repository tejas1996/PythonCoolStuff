import random
import urllib.request

def download_web(url):
    name = random.randrange(1,1000);
    filetype = "pdf"
    fullname = str(name) + filetype
    urllib.request.urlretrieve(url, fullname)

download_web("http://newsonair.nic.in/GST_FAQ.pdf")