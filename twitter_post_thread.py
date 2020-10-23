'''
Script to post tweets
Fecha: 05/03/2020
Author: Julio Burgos
'''


#Import modules
import TwitterAPI
import threader



#an app need to be create on twitter https://developer.twitter.com/apps to get the values need below

api = TwitterAPI.TwitterAPI(consumer_key='',consumer_secret='',access_token_key='',access_token_secret='')

#open file to be post
f = open('texto.txt','r')
fread = f.readline()
f.close()
#array to post
post = []
slices =  '' 
#read file to create array of 280 character 
for i in fread:
    slices += i
    if len(slices) == 280:
        if slices[-1].isspace():
            post.append(slices)
            slices = ''
        else:
            #variable to delimiter the white space to avoid cut words
            stopspace=0
            while not slices[stopspace].isspace():
                stopspace -= 1
            post.append(slices[0:stopspace])
            slices=slices[stopspace:]
post.append(slices)

th = threader.Threader(post,api,wait=2)
th.send_tweets()
