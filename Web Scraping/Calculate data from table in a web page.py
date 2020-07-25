# Calculate data from table in a web page

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')

# This opens the link.
html = urllib.request.urlopen(url, context=ctx).read()

# This parses through the html tags and makes a tree.
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the span tags
tags = soup('span')
ans = 0
for tag in tags:
    # Look at the parts of a tag
    # print('TAG:', tag)
    # print('URL:', tag.get('class', None))
    # print('Contents:', tag.contents[0])
    # print('Attrs:', tag.attrs)
    ans += int(tag.contents[0])

print(ans)
