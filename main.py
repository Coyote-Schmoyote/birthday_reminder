import os
import datetime
from datetime import date, timedelta
import notify2
import dbus

birthday_dict = {}

filename = 'birthday_log.txt'

def add_to_log(filename):
    name = input("Name: ")
    date_str = input("Birthday (day/month) :")
    birthday_dict.update({name: date_str})

    with open(filename, mode='a') as birthday_log:

        file = birthday_log.write(f'\n {name}:{date_str}')
    print ('Birthday added!')


def reminder(filename):
    file = open(filename, 'r')
    today = date.today()
    today_str = today.strftime("%d/%m")
    minus_three_days = today - datetime.timedelta(days=-3)
    minus_three_days_str = minus_three_days.strftime("%d/%m")
    text1 = "Today is {}'s birthday".format(line[0])
    text2 = "{}'s birthday is in 3 days".format(line[0])
    notify2.init("Birthday Reminder")
    n1 = notify2.Notification(None, message=text1)
    n2 = notify2.Notification(None, message=text2)
    n.set_urgency(notify2.URGENCY_NORMAL)
    n.set_timeout(1000)
    flag = 0
    for line in file:
        if today_str in line:
            line = line.split(':')
            flag = 1
            n1.show()
        elif minus_three_days_str in line:
            line = line.split(':')
            flag = 1
            n2.show()


#look up birthday

def look_up(filename):
    user_input = input("Who\'s birthday do you want to know? ")
    file = open(filename, 'r')
    for line in file:
        if user_input in line:
            line = line.split(':')
            flag = 1
            print (f'{line[0]}\'s birthday is {line[1]}')


#do you want to add another birthday?
play = True
reminder("birthday_log.txt")


while play:

    again_add = input("Do you want to add a birthday? (y/n) : ")
    if again_add == "y":
        add_to_log("birthday_log.txt")
    elif again_add == "n":
        again_look_up = input("Do you want to look up somebody\'s birthday? (y/n) : ")
        if again_look_up == "y":
            look_up("birthday_log.txt")
        elif again_look_up == "n":
            play = False
            print ("Au revoir then!")
        else:
            print ("I don\'t understand you.")
    else:
        print("I don\'t understand you.")
        play = True