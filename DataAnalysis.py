from urllib import request

goog = "http://samplecsvs.s3.amazonaws.com/SalesJan2009.csv"

def downloadStock(url):
    response = request.urlopen(url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split(r"\n")
    desturl = r'goog.csv'
    fx = open(desturl,"w")
    for line in lines:
        line.rstrip("\\n")
        fx.write(line)
    fx.close()

downloadStock(goog)