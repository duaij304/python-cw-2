my_name= input("whats your name?")
my_age= input("How old are you?")

print(f"my name is {my_name} and my age is {my_age}")

first_number= int(input("first number"))
second_number= int(input("second number"))
operation=input(" select +-*/")

if operation== "+":
 print(first_number + second_number)
elif operation== "*":
 print(first_number*second_number)
elif operation == "/":
  print(first_number/second_number)
elif operation== "-":
 print (first_number-second_number)


bus_capacity= 60
people_inbus=int(input("how many people are in the bus"))
empty_seats = bus_capacity - people_inbus

if bus_capacity>= people_inbus :
 print (f"there is {empty_seats} empty seats")
elif bus_capacity< people_inbus :
 print ("there is no seats")
