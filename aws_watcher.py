import requests
from bs4 import BeautifulSoup
import smtplib

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('***********email*****','***********password*****')
    
    msg = "price gets less"

    server.sendmail(
        'from email',
        'to email',
        msg
    )
    print("EMAIL SENT")
    server.quit()


def extractPrice():
    url = 'https://www.amazon.in/Sinew-Nutrition-Protein-Concentrate-Unflavoured/dp/B0733CPD5D/ref=sr_1_6?keywords=sinew+protein&qid=1563608268&s=gateway&sr=8-6'
    headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0'}
    page = requests.get(url,headers=headers)
    soup = BeautifulSoup(page.content,'html.parser')
    title = soup.find(id='productTitle').get_text().strip()
    price = float("".join(list(soup.find(id='priceblock_ourprice').get_text().strip())[2:]).replace(",",""))
    if price > 2549:
        print (title)
        print(price)
        send_mail()
    else:
        print("nothing happend")


# #follow below instruction
# '''
# Log in to your Google account, and use these links:

# Step 1 [Link of Disabling 2-step verification]:

# https://myaccount.google.com/security?utm_source=OGB&utm_medium=act#signin
# "==================disable it=================="
# Step 2: [Link for Allowing less secure apps]

# https://myaccount.google.com/u/1/lesssecureapps?pli=1&pageId=none
# "==================make it allow==============="
# '''
# #NOTE:-search "my user agent on google, copy that and paste it below"