import os
import json
from my_lib.spilt import spilt_lyrics, dict_adjust
orgin_path = os.getcwd()

data = dict()
freq_dict = dict()

sel = int(input("Input a path for 1 and use the default data in file 'data.json' for 0: "))
if sel == 1:
    data['path'] = input("Please input the ABSOLUTE PATH of your folder: ")
    data['name'] = input("Please input the name you want for the folder: ")
elif sel == 0:
    with open("data.json") as f_obj:
        data = json.load(f_obj)
else:
    print("请不要演我！")

data_adjust = input("Adjust some data to decrease the influencce of the songs which contains a lot of a word (Y/N): ")

os.chdir(data['path'])
files = os.listdir()

for file in files:
    spilt_dict = spilt_lyrics(file)

    if data_adjust.lower() == "y":
        spilt_dict = dict_adjust(spilt_dict)
    
    for key, value in spilt_dict.items():
        if key in freq_dict:
            freq_dict[key] = freq_dict[key] + value
        else:
            freq_dict[key] = value
    
freq_dict = sorted(freq_dict.items(), key = lambda kv:(kv[1], kv[0]), reverse=True)

os.chdir(orgin_path)
with open('rank.txt', 'w', encoding='utf-8') as f_obj:
    f_obj.write(str(freq_dict))
