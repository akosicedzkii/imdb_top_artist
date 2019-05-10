import requests
from bs4 import BeautifulSoup
import shutil
import os

res = requests.get("https://www.imdb.com/list/ls050274118/")
res = requests.get("https://www.imdb.com/list/ls063784435/")

#print(res.text)



soup = BeautifulSoup(res.text,features="html.parser")

matches = soup.findAll("div", {"class":"lister-item-image"})
for m in matches:
    print(m)
    children = m.findChildren("img" , recursive=True)
    for child in children:
        print (child['alt'])
        response = requests.get(child['src'], stream=True)
        os.mkdir('knn_examples/train/'+str(child['alt']))
        with open("knn_examples/train/"+str(child['alt']) + "/" + str(child['alt']) +".png", 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response  



