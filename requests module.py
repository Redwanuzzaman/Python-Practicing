import requests

#the required first parameter of the 'get' method is the 'url':
x = requests.get('https://w3schools.com/python/demopage.htm')

#print the response text (the content of the requested file):
print(x.text)


import requests

url = 'https://www.w3schools.com/python/demopage.php'
myobj = {'somekey': 'somevalue'}

x = requests.post(url, data = myobj)

#print the response text (the content of the requested file):

print(x.text)


#the required first parameter of the 'delete' method is the 'url':
x = requests.delete('https://w3schools.com/python/demopage.php')

#print the response text (the content of the requested file):
print(x.text)
