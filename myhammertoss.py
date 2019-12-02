#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
import cv2 as cv
import numpy as np
import base64

tusername='pozha15'
taddr='https://twitter.com/'

turl=taddr+tusername
data=requests.get(turl)
#print(data.text)
soup=BeautifulSoup(data.text, 'html.parser')
tweets=soup.find_all('p', {'class':'TweetTextSize TweetTextSize--normal js-tweet-text tweet-text'})
for tweet in tweets:
	text=str(next(tweet.children)) # the tweet itself
	hashtag=str(next(tweet.b.children)) # hashtag
	#print(text+" #"+hashtag)
	#print(tweet.a)
	#for att in tweet:
	#	print(att)


gusername='zhopa15'
gaddr='https://github.com/'

gurl=gaddr+gusername

data=requests.get(gurl)
#print(data.text)
soup=BeautifulSoup(data.text, 'html.parser')
#print(soup.prettify())
repos=soup.find_all('span', {'class': 'repo'})
for r in repos:
	repo=r['title']
	gurl=gaddr+gusername+"/"+repo
	data=requests.get(gurl)
	soup=BeautifulSoup(data.text, 'html.parser')
	#print(soup.prettify())
	files=soup.find_all('a', {'class': 'js-navigation-open'})
	for f in files:
		if f['class'][0]=='js-navigation-open' and f['href'].split('.')[-1]=='jpg':
			picurl=gaddr+f['href']
			pic=requests.get(picurl.replace('blob', 'raw'), allow_redirects=True)
			nparr=np.frombuffer(pic.content, np.uint8)
			img=cv.imdecode(nparr, 0)
			#cv.imshow('secret cat', img)
			#k = cv.waitKey(0) & 0xFF
			#if k == 27:
			#	cv.destroyAllWindows()
			#with open()
			#with open('gitcat1.jpg', 'wb') as fd:
			#	fd.write(pic.content)
			#pic1 = open(pic)
			#print(type(pic.content))
			#base64.b64decode(pic.content)
			#img = cv.imread(pic.content)
			#np.fromstring

#now obtain collabedit postfix
#secret=img[0:5][-1][1]
postfix=''
for ind in range(5):
	#print(img[ind][-1][1])
	postfix+=chr(img[ind, 0])
	ind+=1
print(postfix)

img1=cv.imread('secretcat1.jpg',0)
postfix=''
for ind in range(5):
	#print(img1[ind][-1][1])
	postfix+=chr(img1[ind, 0])
	ind+=1
print(postfix)
for indx in range(10):
	for indy in range(10):
		print(img1[indx, indy], end=' ')
	print()

cv.imshow('secret cat', img)
k = cv.waitKey(0) & 0xFF
if k == 27:
	cv.destroyAllWindows()
