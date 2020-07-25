from plyer import notification
import requests
from bs4 import BeautifulSoup
import time


def notifyme(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon=r"D:\Drive G\corona.ico",
        timeout=10
    )


def getData(url):
    r = requests.get(url)
    return r.text


while True:

    myHtmlData = getData('https://www.mohfw.gov.in/')    

    soup = BeautifulSoup(myHtmlData, 'html.parser')

        # print(soup.prettify())

    myDatastr= ""

    for tr in soup.find_all('tbody')[0].find_all('tr'):

        myDatastr += tr.get_text()

    myDatastr = myDatastr[1:]

    itemList = myDatastr.split("\n\n")


    for item in itemList[0:29]:

        datalist = item.split('\n')

            # print(datalist)        

        nTitle = 'Cases of COVOID-19'

        nText = f"State - {datalist[1]}\nActive cases: {datalist[2]}\nCured: {datalist[3]}\nDeaths: {datalist[4]}"

        notifyme(nTitle, nText)

        time.sleep(30)

    time.sleep(120)