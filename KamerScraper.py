import requests
import time

from email.message import EmailMessage
import ssl
import smtplib


URL = "https://www.klikvoorkamers.nl/portal/object/frontend/getallobjects/format/json"

Interval = 900.0 #15 mins

global TotalItemsWhenLastChecked
TotalItemsWhenLastChecked = 0


SendersEMail = "Email_1"
Password = "placeholder"

ReceiversEMail  = "Email_2"

Subject = "Site Updated"

Body = "Site Updated Check it ASAP"


Email = EmailMessage()

Email["From"] = SendersEMail
Email["To"] = ReceiversEMail
Email["Subject"] = Subject
Email.set_content(Body)

Context = ssl.create_default_context()

def GetNumberOfItems():
    Request = requests.get(URL)

     what to do if the request times out ie bad internet
    
    JsonData = Request.json()
    
    Result = JsonData["result"]
    
    ItemNum = 0
    
    for House in Result:
        
        Category = House["dwellingType"]["categorie"]
        
        if (Category == "woning" and Category != "voorVoertuig"):
            
            ItemNum+=1
            

    return ItemNum



def NotifyUser():
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=Context) as smtp:
 
     smtp.login(SendersEMail, Password)
     smtp.sendmail(SendersEMail, ReceiversEMail, Email.as_string())

    


def Update():
    CurrentTotalItems = GetNumberOfItems()

    print(CurrentTotalItems)
    
    global TotalItemsWhenLastChecked
 
    if TotalItemsWhenLastChecked != CurrentTotalItems:
    
        TotalItemsWhenLastChecked = CurrentTotalItems

        NotifyUser()
    



while True:

    Update()
    time.sleep(Interval)
