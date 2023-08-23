import requests
import urllib

username = 'MikiNik'
password = 'nick1261098'

userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'

data = requests.get('https://api.imgflip.com/get_memes').json()['data']['memes']

images = [{'name':image['name'],'url':image['url'],'id':image['id']} for image in data]

print('Лист доступных мемов:')

ctr = 1
for img in images:
    print(ctr, img['name'])
    ctr = ctr+1

id = int(input('Введите номер картинки: '))
text0 = input('Введите первый текст: ')
text1 = input('Введите первый текст: ')

URL = 'https://api.imgflip.com/caption_image'
params = {
    'username':username,
    'password':password,
    'template_id':images[id-1]['id'],
    'text0':text0,
    'text1':text1
}
response = requests.request('POST',URL,params=params).json()
print(response)

opener = urllib.request.URLopener()

opener.addheader('User-Agent', userAgent)

filename, headers = opener.retrieve(response['data']['url'], images[id-1]['name']+'.jpg')

