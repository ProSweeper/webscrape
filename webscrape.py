import requests
from bs4 import BeautifulSoup

URL = 'https://stilltasty.com'

page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

category_container = soup.find("div", {"class": "images-container"})
cat_lists = category_container.find_all("span")
category_names = []
category_links = []
for span in cat_lists:
  name = span.find('a').text
  category_names.append(name)
  link = span.find("a")['href']
  category_links.append(link)
category_names = category_names[:10]  
category_links = category_links[:10]  
# for name in category_names:
  # print(name)
# for link in category_links:
  # print(link)

new_url = category_links[0]
# print(new_url)
fruits_page = requests.get(new_url)
fruit_soup = BeautifulSoup(fruits_page.content, "html.parser")
fruit_list = fruit_soup.find("div", {"class": "search-list"})
# print(fruit_list)
fruit_anchors = fruit_list.find_all("a")
fruit_anchor = fruit_anchors[4]
# print(fruit_anchor['href'])
fruit_url = fruit_anchor['href']
fruit_page = requests.get(fruit_url)
single_soup = BeautifulSoup(fruit_page.content, "html.parser")

item_name = single_soup.find('h2').text
# print(item_name)
item_tips_container = single_soup.find("div", {"class": "food-tips"})
item_tips = item_tips_container.find_all("li")
food_tip = ""
for tip in item_tips:
  food_tip += tip.text
# print(food_tip)
my_dict = {}
for name in category_names:
  my_dict[name] = {}
# print(my_dict)
