import re
import urllib2

def getHTML(url):
    usock = urllib2.urlopen(url)
    data = usock.read()
    usock.close()
    return data

def download(url, file_name):
    print "downloading " + file_name + " ..."
    req = urllib2.Request(url)
    f = urllib2.urlopen(req)
                    
    local_file = open(file_name, "w")
    local_file.write(f.read())
    local_file.close()

    print "done."
            
url = "http://books.nips.cc/nips25.html"

data = getHTML(url)

search_regex = re.compile(r'http://books.nips.cc/papers/files/nips25/NIPS2012_\d{4}.pdf')

matches = [[m.start(), m.end()] for m in search_regex.finditer(data)]

counter = 1
for m in matches:
    download_url = data[m[0]:m[1]]
    download(download_url, "pdfs/pdf_"+str(counter))
    counter += 1
