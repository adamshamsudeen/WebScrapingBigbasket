from bs4 import BeautifulSoup as bs
import requests
urlopen = requests.get('https://www.bigbasket.com/pd/20000457').text
soup = bs(urlopen,'html.parser')
#print(soup)

ProductInfo = soup.find("h1", {"class": "GrE04"}).text
print(ProductInfo)

NewPro = ProductInfo.split(' ', 1)
print(NewPro)

BrandName = soup.find("a", {"class": "_2zLWN _3bj9B rippleEffect"}).text
print(BrandName)

ProductName = ProductInfo.split(' ', 1)[1].split(',')[0].strip()
print(ProductName)

ProductQnty = ProductInfo.split(' ', 1)[1].split(',')[1].strip()
print(ProductQnty)

# ActuallPrice = soup.find("td", {"class": "_2ifWF"}).text.strip()
# print(ActuallPrice)

ProductPrice = soup.find("td",{"data-qa":"productPrice"}).text.strip()
print(ProductPrice)

# DiscountOffered = soup.find("tr", {"class": "_21awm"}).text.strip()
# print(DiscountOffered)

ProductDesc = soup.find("div",{"class":"_26MFu"}).text.strip().split('   ')[-1:]
print(ProductDesc)
