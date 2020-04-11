import pandas as pd
from bs4 import BeautifulSoup as bs
import requests

eanCodeLists = []

ProductNameList = []
BrandNameList = []
ProductQntyList = []

ProductPriceList = []

ProductDescList = []

for items in eanCodeLists:
    urlopen = requests.get('https://www.bigbasket.com/pd/'+str(items)).text
    soup = bs(urlopen, 'html.parser')

    ProductInfo = soup.find("h1", {"class": "GrE04"}).text.strip()
    ProductName = ProductInfo.split(' ', 1)[1].split(',')[0]
    ProductNameList.append(ProductName)

    BrandName = ProductInfo.split(' ', 1)[0]
    BrandNameList.append(BrandName)

    ProductQnty = ProductInfo.split(' ', 1)[1].split(',')[1].strip()
    ProductQntyList.append(ProductQnty)

    ProductPrice = soup.find("td", {"data-qa": "productPrice"}).text.strip()
    ProductPriceList.append(ProductPrice)

    ProductDesc = soup.find("div", {"class": "_26MFu"}).text.strip().split('   ')[-1:]
    ProductDescList.append(ProductDesc)


table_dict = {'Product_Name': ProductNameList, 'Brand_Name': BrandNameList,
              'Product_Qnty': ProductQntyList, 'Product_Price': ProductPriceList, 'Product_Desc': ProductDescList}

df = pd.DataFrame(table_dict)
print(df)

df.to_csv('Bigbasket_beauty-hygiene.csv', index=False)
