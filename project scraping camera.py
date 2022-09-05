import requests
from bs4 import BeautifulSoup
import pandas as pd

#url of requested page(camera)
url = "https://www.flipkart.com/search?q=camera&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
#total values  and data in page(scrapping is done on this data)
response = requests.get(url)
print(response)

#print(response.content)
htmlcontent =  response.content

#to pretify and parsing data
soup = BeautifulSoup(htmlcontent,'html.parser')
#print(soup.prettify())

print(soup.title)

titles = []
prices = []
images = []

#to convert in CSV file
#with open ('camera.csv','w',encoding='utf8',newline='') as f:
     #thewriter = writer(f)
     #header = ['title','price','image']
     #thewriter.writerow(header)

    #to print  product,price,image
for d in soup.find_all('div', attrs={'class':'_2kHMtA'}):
    title = d.find('div',attrs={'class':'_4rR01T'}).string
     #titles.append(title.string)
    #titles = [title.string]


    price = d.find('div',attrs={'class':'_30jeq3 _1_WHN1'}).string
      #prices.append(price.string)
     #prices = [price.string]


    image = d.find('img', attrs={'class': '_396cs4 _3exPp9'})
       #images.append(image.get('src'))

    #images =[image.get('src')]


#info = ['title','price','image']
#thewriter.writerow(info)
#file.close()
    titles.append(title.string)
    prices.append(price.string)
    images.append(image.get('src'))
print(titles)
print(prices)
print(images)

#to covert list into dataframe
dict = {'TITLE': titles, 'PRICE': prices, 'IMAGE': images}
df = pd.DataFrame(dict)
#print(df)

#to convert into CSV file
df.to_csv(r'C:\Users\ASUS\PycharmProjects\project web scraping\cameraScraping.csv')




