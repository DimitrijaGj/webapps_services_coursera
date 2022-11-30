#!/usr/bin/env python3

import os
import requests
text_dir = "./feedback/"

dict_file = {}
for text_file in os.listdir(text_dir):
    print(text_file)
#----- so far works------
    with open(text_dir + text_file, 'r') as file:
        for line in file:
            review= line.strip()
    
            print(review)
