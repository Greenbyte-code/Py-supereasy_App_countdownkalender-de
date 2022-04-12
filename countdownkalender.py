"""Countdown-Kalender aus 'Progammieren mit Python supereasy'(ISBN'978-3-8310-3457-4')[S.110]"""
from tkinter import Tk, Canvas
from datetime import date, datetime
import os

#def get_ereignisse():
#    list_ereignisse = []
#    with open('./ereignisse.txt') as file:
#        for line in file:
#            line = line.rsplit('\n')
#            current_ereignis = line.split(',')
#            ereignisse_date = datetime.strptime(current_ereignis[1], '%d/%m/%y').date()
#            current_ereignis[1] = ereignisse_date
#            list_ereignisse.append(current_ereignis)
#    return list_ereignisse

#["Geburtstag", "05/02/2023", "Weihnachten", "24/12/2022", "Ostern", "02/04/2023"]

def get_ereignisse():
    list_ereignisse = ["Geburtstag", "05/02/2023", "Weihnachten", "24/12/2022", "Ostern", "02/04/2023"]
    return list_ereignisse

def days_zw_data(data1, data2):
    time_between = str(data1 - data2)
    number_of_days = time_between.split(' ')
    return number_of_days[0]

root = Tk()
c = Canvas(root, width=800, height=800, bg='black')
c.pack()
c.create_text(100, 50, anchor='w', fill='orange', font='Arial 28 bold underline', text='Mein Kalender')

#ereignisse = get_ereignisse()
ereignisse = get_ereignisse()
heute = date.today()

for ereignisse in ereignisse:
    ereigniss_name = ereignisse[0]
    days_till = days_zw_data(ereignisse[1], heute)
    display = "Es sind noch %s Tage bis %s" % (days_till, ereigniss_name)
    c.create_text(100, 100, anchor='w', fill='lightblue', font='Arial 28 bold', text=display)
