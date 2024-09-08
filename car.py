ask = input("color name ? ")

class Car:
    def __init__(self):
        print()

    def blueCar(self):
        print('color: blue brand : 56 BMW')
        print('color: blue brand : 600 MINI')
        print('color: blue brand : 2000 ASTON MARTIN')
        print('color: blue brand : 3009 BUGATTI')
        print('color: blue brand : 2010 ROLLS ROYCE')

    def redCar(self):
        print('color:red brand : 2 BMW')
        print('color:red brand : 100 MINI')
        print('color:red brand : 1900 ASTON MARTIN')
        print('color:red brand : 340 BUGATTI')
        print('color:red brand : 22 ROLLS ROYCE')


    def greenCar(self):
        print('color: green brand : 39 BMW')
        print('color: green brand : 1 MINI')
        print('color: green brand : 90 ASTON MARTIN')
        print('color: green brand : 4 BUGATTI')
        print('color: green brand : 338 ROLLS ROYCE')   


oneCar = Car() 


if ask == "red":
    print("List of cars with red color:")
    oneCar.redCar()
elif ask == "blue":
    print("List of cars with blue color:")
    oneCar.blueCar()
elif ask == "green":
    print("List of cars with green color:")
    oneCar.greenCar()
else:
    print("no")
 

