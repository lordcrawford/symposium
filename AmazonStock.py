import csv
import requests
import bs4
from decimal import Decimal
from Algorithm import *

#STORING DATA FROM CSV FILES
AmazonDates = []
AmazonPrices = []


count = 0

with open('stockInfo/AMZN (1).csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        if count == 1:
            AmazonDates.append(row[0])
            AmazonPrices.append(float(round(Decimal(row[1]), 2)))
        else:
            count = 1



#SCRAPING FOR CURRENT PRICE

res = requests.get('https://finance.yahoo.com/quote/AMZN?p=AMZN')

soup = bs4.BeautifulSoup(res.text, 'lxml')
AmazonCurrentPrice = soup.select("span[data-reactid*='21']")[0].text




##SIMPLE MOVING AVERAGE

AmazonDailyDates = []
AmazonDailyPrices = []

count1 = 0

with open('stockInfo/FullYearDailyAmazonData.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        if count1 == 1:
            AmazonDailyDates.append(row[0])
            AmazonDailyPrices.append(float(round(Decimal(row[1]), 2)))
        else:
            count1 = 1




##13 DAY MOVING AVERAGE
amazon_moving_averages13 = []

for i in range(13, len(AmazonDailyPrices)+1):
    new13 = AmazonDailyPrices[(i-13) : (i)]
    amazon_moving_averages13.append(round((sum(new13))/(13.0),2))




##52 DAY MOVING AVERAGE
amazon_moving_averages52 = []

for i in range(52, len(AmazonDailyPrices)+1):
    new52 = AmazonDailyPrices[(i-52) : (i)]
    amazon_moving_averages52.append(round((sum(new52))/(52.0),2))




#NEXT YEAR ESTIMATE

soup1 = bs4.BeautifulSoup(res.text, 'lxml')
amazon_nextyearest = soup1.select("span[data-reactid*='90']")[0].text




#RETURN ON ASSETS
res1 = requests.get('https://finance.yahoo.com/quote/AMZN/key-statistics?p=AMZN')

soup2 = bs4.BeautifulSoup(res1.text, 'lxml')
amazon_returnassets = soup2.select("td[data-reactid*='133']")[0].text


#VOLUME

soup3 = bs4.BeautifulSoup(res.text, 'lxml')
amazon_volume = soup1.select("span[data-reactid*='41']")[0].text