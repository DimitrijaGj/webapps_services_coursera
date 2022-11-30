#!/usr/bin/env python3
import os
import requests
web_ip ='34.72.37.98'
text_dir = '~/data/feedback/'
keys = ['title', 'name', 'date', 'feedback']
feedback_files = os.listdir(text_dir)
for file in feedback_files:
    fb_dict = {}
    key_count = 0
    with open (text_dir + file) as fb:
        x=1
        for line in fb: #we go trough file
            review = line.strip() # we rad every line in the file
            if not keys[key_count] in fb_dict: # we add keys value pair so if is key not in dict
                fb_dict[keys[key_count]]=review 
                '''# then we take the key from the list and assign the value from .strip method 
                key will be the first vlaue from list and the first line from .strip mehtod. 
                Goes again checks and if is not there it repeats'''
            key_count += 1 #go over again 
        print(fb_dict)

response = requests.post('https://{}/feedback/'.format(web_ip), json=fb_dict)
print(response.raise_for_status())