#version 2.2
import requests
from bs4 import BeautifulSoup
import pandas as pd
pd.set_option("display.max_rows", None, "display.max_columns", None)

urls = ["https://leomoon173.pixnet.net/blog/post/6777691", 
        "https://leomoon173.pixnet.net/blog/post/27331605", 
        "https://leomoon173.pixnet.net/blog/post/6777767", 
        "https://leomoon173.pixnet.net/blog/post/6777940", 
        "https://leomoon173.pixnet.net/blog/post/6777982"]

name_list = []; ingredient_list = []; kitchen_list = []; price_list = []
for url in urls:
    html = requests.get(url)
    html.encoding = "utf-8"
    sp = BeautifulSoup(html.text, 'lxml')

    infos = sp.find_all('td')
    info_list = []
    for info in infos:
        temp = info.text.strip('\n')
        name = ""
        for i in range(len(temp)):
            if(temp[i] == '\n' or temp[i] == '('):
                break
            name += temp[i]
        info_list.append(name)
        
    for i in range(len(info_list)):
        if(i % 4 == 0):
            name_list.append(info_list[i])
            continue
        elif(i % 4 == 1):
            ingredient_list.append(info_list[i])
            continue
        elif(i % 4 == 2):
            kitchen_list.append(info_list[i])
            continue
        elif(i % 4 == 3):
            price_list.append(info_list[i].replace('5☆ ', '').replace(' G', ''))
            continue
            
for i in range(len(ingredient_list)):
    temp_list = []
    ingredient_list[i] = ingredient_list[i].replace(' + ', ',')
    temp_list = ingredient_list[i].split(',')
    ingredient_list[i] = temp_list

for name in name_list:
    if(name == "名稱"):
        name_list.remove(name)
        
for ingredient in ingredient_list:
    if(ingredient[0] == "材料"):
        ingredient_list.remove(ingredient)
        
for kitchen in kitchen_list:
    if(kitchen == "廚具"):
        kitchen_list.remove(kitchen)
        
for price in price_list:
    if(price == "市集賣價"):
        price_list.remove(price)
    
search = input('請輸入食材(Please enter the ingredient)：')
output = pd.DataFrame(columns = ["name", "ingredient", "kitchenware", "price"])
search_list = search.split(' ')

if(search != "index"):
    for i in range(len(ingredient_list)):
        for j in range(len(search_list)):
            if(search_list[j] in ingredient_list[i]):
                if(j == len(search_list) - 1):
                    output.loc[len(output)] = [name_list[i], ingredient_list[i], kitchen_list[i], price_list[i]]
                    break
                else:
                    continue
            else:
                break            
else:
    for i in range(len(ingredient_list)):
        output.loc[len(output)] = [name_list[i], ingredient_list[i], kitchen_list[i], price_list[i]]
        
output.price = output.price.astype(int)
output.sort_values(by = "price", inplace = True, ascending = False)
output.index = [i + 1 for i in range(len(output))]
print(output)
