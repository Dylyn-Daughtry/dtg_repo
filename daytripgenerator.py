import random
import time
import os


clear = lambda: os.system('cls')


destinations = ['Los Angeles ', 'Chicago ', 'New York ', 'Seattle ', 'San Fran', 'Rome Italy', 'Paris France', 'Miami', 'Milwaukee']
restaraunts = ['Zippys BBQ ', 'Mad Max Hotdogs ', 'Greenthumb Winery ', 'Chronic Tacos ', 'Todds Steakhouse', 'Pizza Planet', 'Bigfoot Diner']
transporation = ['Train', 'Roadtrip', 'flying']
entertainment = ['Gaming Convention ', 'Magic Show ', 'Museum ', 'Concert ']


def random_destination(city):
    city_selected = (random.choice(city))                   #chooses random city stores in a return
    return city_selected

def random_restaraunt(where_to_eat):
    return(random.choice(restaraunts))

def random_transport(how_youre_traveling):
    return(random.choice(transporation))

def random_entertainment(what_to_do):
    return(random.choice(entertainment))

clear()
proceed_destination = False
city_selected = random_destination(destinations)
while proceed_destination is False:
        print(f'We have selected the city of {city_selected}')
        proceed_destination = input(f' To confirm {city_selected} enter "Yes". If not then enter "No"').upper() == 'YES'
        clear()
        if proceed_destination is False:
            city_selected = random_destination(destinations)

proceed_restaraunt = False
restaraunt_selected = random_restaraunt(restaraunts)
while proceed_restaraunt is False:
    print(f'We have selected the restaraunt {restaraunt_selected}')
    proceed_restaraunt = input(f' To confirm {restaraunt_selected} enter "Yes". If not then enter "No"').upper() == 'YES'
    clear()
    if proceed_restaraunt is False:
        restaraunt_selected = random_restaraunt(restaraunts)
    

proceed_transport = False
transport_selected = random_transport(transporation)
while proceed_transport is False:
    print(f'The method of travel will be {transport_selected}')
    proceed_transport = input(f' To confirm {transport_selected} enter "Yes". If not then enter "No"').upper() == 'YES'
    clear()
    if proceed_transport is False:
        transport_selected = random_transport(transporation)


proceed_entertainment = False
entertainment_selected = random_entertainment(entertainment)
while proceed_entertainment is False:
    print(entertainment_selected)
    proceed_entertainment = input(f' To confirm {entertainment_selected} enter "Yes". If not then enter "No"').upper() == 'YES'
    clear()
    if proceed_entertainment is False:
        entertainment_selected = random_entertainment(entertainment)

print(f'Enjoy your trip to {city_selected} by {transport_selected}, also taste the food at {restaraunt_selected}, and enjoy the {entertainment_selected}: ')
print()
print()
print()

trip_complete = True
trip_answer = input('Is day trip okay? ').upper() == 'YES'
clear()
while trip_answer is False:
    print('Do you want to change the city?')
    new_city = random_destination(destinations)
    if input('Yes or No').upper() == 'YES':
        print(new_city)
    print('Do you want to change the restaraunt?')
    if input('Yes or No').upper() == 'YES':
        new_restaraunt = random_restaraunt(restaraunts) 
        print(new_restaraunt)
    print('Do you wish to change the method of transportation?')
    if input('Yes or No').upper() == 'YES':
        new_trans = random_transport(transporation) 
        print(new_trans)
    print('Do you wish to change the entertainment?')
    if input('Yes or No').upper() == 'YES':
        new_entertainment = random_entertainment(entertainment) 
        print(new_entertainment)
        print(f'Your new trip is set to {city_selected} by {transport_selected}, also taste the food at {restaraunt_selected}, and enjoy the {entertainment_selected}: ')
    if input('Do you want to confirm this new daytrip?').upper() == 'YES':
        trip_answer = True
    if trip_answer is True:
        print(f'Enjoy your trip to {city_selected} by {transport_selected}, also taste the food at {restaraunt_selected}, and enjoy the {entertainment_selected}: ')
    



