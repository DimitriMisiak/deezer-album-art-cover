# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 12:02:07 2019

@author: dimit
"""

import deezer
import requests
from tqdm import tqdm
import re

save_dir = 'output/'

my_id = 438597901

client = deezer.Client()

user = client.get_user(my_id)

my_albums = client.get_object('user', my_id, relation='albums', limit=-1)


def sanitize(string):
    
    clean1 = re.sub('[<>:"/\|?*]', '', string)
    clean2 = re.sub(' ', '', clean1)
    
    return clean2
    

for album in tqdm(my_albums):
    
    title = album.title.replace(' ', '_')
    artist = album.artist.name.replace(' ', '_')

    img_name = sanitize('{}-{}.jpg'.format(artist, title))

    cover_url = album.cover_xl
    
    img = requests.get(cover_url).content
    
    with open(save_dir+img_name, 'wb') as local_img:
        local_img.write(img)
    
    