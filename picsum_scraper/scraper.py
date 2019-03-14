import urllib

import urllib
count = 0
for x in range(993):
    url = "https://picsum.photos/800/800/?image=" + str(x)
    resource = urllib.urlopen( url)
    if resource.read() == '{"error":"Invalid image id"}':
        print("Bad")
    else:
        count +=1
        urllib.urlretrieve("https://picsum.photos/800/800/?image=" + str(x), str(count) + ".jpg")
