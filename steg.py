#!/usr/bin/env python3

##primitive domain/username steganography
#this file creates a new collabedit page and hides the handle in a picture

from bs4 import BeautifulSoup 
import requests
import cv2 as cv




data=requests.get('http://collabedit.com/new')
soup=BeautifulSoup(data.text, 'html.parser')

ex=soup.find_all('script')
exx=str(ex[-5]).split('var guid = "')
secret = exx[1].split('";')[0]
#print(str(ex[-5].split('var guid = ')))

#print(soup.prettify())


img = cv.imread('gitcat1.jpg', 0)

for indx in range(10):
	for indy in range(10):
		print(img[indx, indy], end=' ')
	print()
cv.imwrite('secretcat1.jpg', img)



ind=0
print(len(img))
img[35:475, 35:475]=0
print(len(secret))
for s in secret:
	print(s, ind)
	img[ind, 0]=ord(s)
	print(img[ind, 0])
	ind+=1
for indx in range(10):
	for indy in range(10):
		print(img[indx, indy], end=' ')
	print()
cv.imwrite('secretcat1.jpg', img)

postfix=''
for ind in range(5):
	#print(img[ind][-1][1])
	postfix+=chr(img[ind, 0])
print(postfix)
#img[0:5][-1][1]=[ord(s) for s in secret]
"""postfix=''
for i in range(5):
	print(i)
	print(img[i][-1][1])
	postfix+=chr(img[i][-1][1])
print(postfix)
cv.imwrite('secretcat.jpg', img)

print(secret)"""
for indx in range(10):
	for indy in range(10):
		print(img[indx, indy], end=' ')
	print()

print("\n\n\n")

cv.destroyAllWindows()