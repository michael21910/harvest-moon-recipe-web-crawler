# Harvest Moon DS - recipe web crawler  
  
![image](https://upload.wikimedia.org/wikipedia/en/e/e4/Harvest_Moon_DS_Grand_Bazaar_boxart.jpg)  
"Harvest moon - Welcome! Wind's Bazaar" is one of Nintendo’s NDS games. It is a member of the Harvest moon series.  
  
## Introduction  
This repo is base on web crawling recipe of the game "Harvest moon - Welcome! Wind's Bazaar".  
  
## Why Harvest Moon  
There is a game that I played before on NDSL, called "Harvest moon - Welcome! Wind's Bazaar" (of course Chinese version).  
However, I somehow lost my NDSL since I am busy studing when I was a junior high school student.  
At the summer vacation from sophomore to junior, my dad gave me a box and said: I found this in a drawer, is that yours?  
I quickly recognized that the thing in the box was the NDSL I lost in the junior high school.  
Now, I can finally enjoy this game that I haven't play since 14 years old.  
  
It's a pity that I forgot all of the recipes in this game. Thus, I decided to write a program to help me deal with this problem.  
  
## How to use  
The recipe is base on the webpages below:  
[salad and soup](https://leomoon173.pixnet.net/blog/post/6777691) / [appetizer](https://leomoon173.pixnet.net/blog/post/27331605) / [main course](https://leomoon173.pixnet.net/blog/post/6777767) / [dessert](https://leomoon173.pixnet.net/blog/post/6777940) / [others](https://leomoon173.pixnet.net/blog/post/6777982)  
You can enter multiple ingredients in Chinese(traditional), 1 space after each ingredient except the last one you input.  
After the input, a table(DataFrame) will be printed.  
In the table, there are:  
* The name of the dish  
* The name of the ingredients  
* The kitchenware that you need  
* The price when it is a 5 star dish  
  
## Example  
The user inputs: “油 牛奶”  
The output should be as follows(DataFrame). 
|   | 名稱 | 材料 | 廚具 | 市場賣價 |
|:---:|:---:|:---:|:---:|:---:|
| 1 | 甜甜圈 | [小麥粉, 油, 雞蛋, 牛奶, 黃油] | - | 1230 | 
| 2 | 蛋包飯 | [油, 牛奶, 雞蛋, 米飯] | 煎鍋 | 1000 |  
| 3 | 煎雞蛋捲 | [油, 牛奶, 雞蛋] | - | 840 |  
  
## Translation  
* name -> 名稱  
* ingredient -> 材料  
* kitchenware -> 廚具  
* price -> 市場賣價  

## Contact
I am not really good at English writing, please correct anytime! Thanks for watching.  
  
This program works on jupyter notebook, please use jupyter to run the program.  
If there are any writing mistakes or bugs about the program, please contact me rightaway.  
Email: 410821305@gms.ndhu.edu.tw or faefae31910@gmail.com.  
  
Michael Hsueh 08/10/2021
