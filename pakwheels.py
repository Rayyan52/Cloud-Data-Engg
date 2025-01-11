from bs4 import BeautifulSoup
import requests
import csv

url = "https://www.pakwheels.com/new-cars/audi/"
request = requests.get(url)
soup = BeautifulSoup(request.text, 'html.parser')

# we are getting the link of the first car
# link = soup.find('a', class_='show')['href']
# print(https://www.pakwheels.com/+link)

# gives me all the links on the page, lets clean it up
# for link in soup.find_all('a'):
#     print(link.get('href'))


# new audi cars container 

new_audi_container = soup.find(class_="generic-car-widgets-container")
# print(new_audi_container)

car_li = new_audi_container.find_all(class_="col-md-3")
# print(len(car_li))
# gives ans 4 because there are 4 cars in that container

urls = []
for car in car_li:
    link = car.find('a')['href'] # or car.find('a').get('href')
    # print("https://www.pakwheels.com/"+link)
    urls.append("https://www.pakwheels.com/"+link)
# print(urls)




other_audi_container = soup.find_all(class_="generic-car-widgets-container")[1]
car_li1 = other_audi_container.find_all(class_="col-md-3")
for car in car_li1:
    link = car.find('a')['href'] # or car.find('a').get('href')
    # print("https://www.pakwheels.com/"+link)
    urls.append("https://www.pakwheels.com/"+link)

# print(urls)
# print(len(urls))





# through a nested loop
# url = 'https://www.pakwheels.com/new-cars/audi/'
# request = requests.get(url)
# soup = BeautifulSoup(request.content,'html.parser')
# urls = []
# audi_containers = soup.find_all(class_='generic-car-widgets-container')
# for audi_container in audi_containers:
#     car_li = audi_container.find_all(class_='col-md-3')
#     for car_url in car_li:
#         tag = car_url.find('a')
#         link = 'https://www.pakwheels.com' + tag.get('href')
#         urls.append(link)



# working on a sngle link now

requesting = requests.get(urls[0])
soup = BeautifulSoup(requesting.text, 'html.parser')

# this will find the fitst image on the page
# image = soup.find('img')
image_url = soup.find('img', class_='lazy')
# it gives us the url of the image on the first link 
# print(image_url)
# print(image_url.get('src'))

#lets get the specification of the car

table = soup.find('table', class_="table bike-version-detailscont")
table_rows = table.find_all('tr')
for data in table_rows:
    table_data = data.find('td').text
    key = table
 
print("hello")