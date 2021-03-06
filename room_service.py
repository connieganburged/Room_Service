#Dictionary for guests and their rooms
from tracemollac import start

guests = {'1':'Khaliun','2':'Joy','3':'Connie','4':'Dari','5':'Enkhriilen'}

#Dictionary for menu
appetizers = {'1':'Ceaser Salad','2':'Pigs in a Blanket', '3':'Mozarella Sticks'}
main_courses = {'4':'Cheese Pizza', '5':'Carbonara', '6':'Lasagna'}
desserts = {'7':'Vanilla Ice-Cream','8':'Chocolate Milkshake','9':'Fruit Salad'}

#Guest's name and room
name = None
room = None

#Guests's order
order = {}

#Check for booked room
while room not in guests.keys():
  room = input('What is your room number?: ')
  #check if room exists
  if room in guests.keys():
    name = input('What is your name?: ')
    #Check if the room and guest name match
    if guests[room] !=name:
      print ('Your name does not match our records.')
      room = None
  else:
    print (f'Room {room} has not been booked.')
  
#Print Appetizers
print()
print ('Appetizers Menu')
print ('-------------')
for code, food in appetizers.items():
  print (code, '->', food)
  
#Add a blank line
print()

#Select Appetizers
appteizer = None
#Check the Appetizer
while appetizer not appetizers.keys():
  appetizer = input('Enter the appetizer code: ')
  if appetizer not in appetizers:
    print('Wrong appetizer code: ')
  else:
    order[appetizer] = appetizers[appetizer]
  
#Print main courses
print ()
print ('Main courses menu')
print ('-----------------')
for code, food in main_courses.items():
    print (code, '->', food)


#Select main course
main_course = None
#Check the appetizer
while main_course not in main_courses.keys():
    main_course = input ('Enter the starter code: ')
    if main_course not in main_courses:
        print('Wrong main course code.')
    else:
        order[main_course] = main_courses[main_course]

#Print desserts
print ()
print ('Desserts menu')
print ('-------------')
for code, food in desserts.items():
    print (code, '->', food)

#Select desserts
dessert = None
#validate the dessert
while dessert not in desserts.keys():
    dessert = input ('Enter the dessert code:')
    if dessert not in desserts:
        print('Wrong dessert code.')
    else:
        order[dessert] = desserts[dessert]

#Check delivery
validtime = False
timeformat = "%H:%M"
while not validtime:
    delivery_time = input("Enter the delivery time (hh:mm): ")
    try:
        validtime = datetime.datetime.strptime(delivery_time, timeformat)
    except ValueError:
       print ('Time format hh:mm')

#Print order:
print ()
print ('Here is your order')
for code, food in order.items():
    print (code, '->', food)

print('Delivery time:', delivery_time)

#Check order
place_order = ''

while place_order.lower() not in ('yes', 'no'):
    place_order = input ('Would you like to confirm your order (yes/no)? ')

print ()
if place_order == 'yes':
    print ('Please wait for your order to be ready')
else:
    print ('Sorry, your order has not been processed')

print ('Thank you for choosing us!')
