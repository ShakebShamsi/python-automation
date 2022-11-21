import requests
import schedule
import time

def send_message():
    resp = requests.post('https://textbelt.com/text', {
    'phone': '+918826038099',
    'message': 'Hello Shakeb! how are you?',
    'key': 'textbelt',
    })
    print(resp.json())

def job():
    print("I'm working...")

schedule.every(10).seconds.do(send_message)
# schedule.every(10).minutes.do(send_message)
# schedule.every().hour.do(send_message)
# schedule.every().day.at("10:30").do(send_message)
# schedule.every(5).to(10).minutes.do(send_message)
# schedule.every().monday.do(send_message)
# schedule.every().wednesday.at("13:15").do(send_message)
# schedule.every().minute.at(":17").do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)