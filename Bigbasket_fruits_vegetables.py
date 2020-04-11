from bs4 import BeautifulSoup as bs
import requests

eanCodeLists = [10000148, 10000159, 1200045, 10000074, 10000143, 10000389, 10000201,
                10000071, 10000033, 10000203, 40057966, 10000069, 10000269, 10000273, 40022638, 10000025, 10000266, 10000288, 10000102, 10000063, 20000974, 10000066, 40089742, 10000093, 10000207, 10000051, 40023472, 10000046, 40033819, 40033824, 10000175, 10000054, 10000599, 10000166, 40004992, 10000370, 20000911, 1209664, 10000050, 40033823, 20000981, 40048444, 10000295, 10000346, 40113206, 10000091, 10000195, 40033815, 40022639, 40023470, 40150775, 10000271, 20000702, 10000181, 10000060, 40022644, 40050066, 10000274, 10000178, 10000172, 10000038, 10000024, 40073760, 40120006, 40023469, 40073761, 20000909, 10000298, 40023482, 10000208, 10000109, 30000575, 50000469, 40164406, 20000707, 10000133, 40008984, 10000087, 40114961, 40033817, 50000557, 20000727, 10000040, 10000297, 10000005, 40075384, 50000534, 10000156, 40105380, 10000101, 50000483, 10000281, 40105338, 10000587, 40179391, 10000198, 10000057, 40033820, 10000192, 10000123, 40033821, 20000756, 30007415, 40023471, 10000168, 20001095, 40020768, 10000141, 20003956, 10000210, 40104703, 10000001, 20000926, 40104709, 30000543, 10000306, 40158182, 40023483, 40036724, 40036723, 10000583, 40019777, 30003344, 40083737, 40021628, 40040312, 30000598, 30002320, 10000028, 40048953, 30007325, 40004344, 40026326, 40026327, 40126752, 40026325,30006386,40026328]

ProductNameList =[]
BrandNameList = []
ProductQntyList = []
# ProductActuallPrice = []
ProductPriceList = []
# DiscountOfferedInPercent= []
ProductDescList =[]

for items in eanCodeLists:
    urlopen = requests.get('https://www.bigbasket.com/pd/'+str(items)).text
    soup = bs(urlopen,'html.parser')

    ProductInfo = soup.find("h1", {"class": "GrE04"}).text.strip()
    ProductName= ProductInfo.split(' ',1)[1].split(',')[0]
    ProductNameList.append(ProductName)

    BrandName = ProductInfo.split(' ', 1)[0]
    BrandNameList.append(BrandName)

    ProductQnty = ProductInfo = soup.find("h1", {"class": "GrE04"}).text.strip()
    ProductQntyList.append(ProductQnty)

    # ActuallPrice = soup.find("td", {"class": "_2ifWF"}).text.strip()
    # ProductActuallPrice.append(ActuallPrice)

    ProductPrice = soup.find("td",{"data-qa":"productPrice"}).text.strip()
    ProductPriceList.append(ProductPrice)

    # DiscountOffered = soup.find("tr", {"class": "_21awm"}).text.strip()
    # DiscountOfferedInPercent.append(DiscountOffered)

    ProductDesc = soup.find("div",{"class":"_26MFu"}).text.strip().split('   ')[-1:]
    ProductDescList.append(ProductDesc)


import pandas as pd

table_dict = {'Product_Name':ProductNameList,'Brand_Name':BrandNameList,'Product_Qnty':ProductQntyList,'Actuall_Price':ProductActuallPrice,'Product_Price':ProductPriceList,'Discount_offered':DiscountOfferedInPercent,'Product_Desc':ProductDescList}

df = pd.DataFrame(table_dict)
print(df)

df.to_csv('Bigbasket_fruits_vegetables.csv', index=False)
