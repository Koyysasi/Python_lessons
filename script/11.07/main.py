import datetime
import pendulum as p   # pip install pendulum
import matplotlib.pyplot as plt

def time_zones():
    cities = ['Europe/Budapest', 'Europe/London', 'America/Toronto', 'America/New_York']
    times = []
    for city in cities:
        now = p.now(city)
        now = now.to_datetime_string()
        times.append(now)
    for i in range(len(times)):
        print(f"{cities[i]} : {times[i]}")

# time_zones() # a citiesben lévő városok kiírása az időzónáikkal
def main():
    print(datetime.datetime.now()) # pontos dátum és idő
    print(datetime.date.today()) # pontos dátum
    print(datetime.date.today().strftime("%A")) # mai nap a hét melyik napja
    print(datetime.date.today().strftime("%a")) # mai nap a hét melyik napja rövidítve
    print(datetime.date.today().strftime("%B")) # melyik hónap van most
    print(datetime.date.today().strftime("%A%a ... %b")) # egymés után is írhatóak
    print(datetime.date.today().strftime('%W')) # Hanyadik hét van az évben
    print(datetime.date.today().strftime('%w')) # Hanyadik hét van az évben
    print(datetime.date.today().strftime('%W'))
    print(datetime.date.today().strftime('%W'))
    print(datetime.date.today().strftime('%j'))
    print(datetime.date.today().strftime('%d'))
    print(datetime.date.today().strftime('%W'))
    print(datetime.date.today().strftime('%y   %Y'))
    print(datetime.date.today().strftime('%m'))



    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    tomorrow = today + datetime.timedelta(days=1)

    print(f"Ma: {today}")
    print(f"Tegnap: {yesterday}")
    print(f"Holnap: {tomorrow}")

import library.mymodul as mym