import os

print("Slope Calculator:")

#Python always assumes that your input is a
#a string unless you tell it. 
#To make a numeric type you have two options
#decimals - float
#integers - int


os.system("say Welcome to my slope calculator please enter you x and y values")
#Imput
x1 = input("Input x1: ")
x1 = int(x1)

y1 = input("Input y1: ")
y1 = int(y1)

x2 = input("Input x2: ")
x2 = int(x2)

y2 = input("Input y2: ")
y2 = int(y2)

#Process
rise = x2 - x1
run = y2 - y1

fSlope = rise/run   
#real numbers are called float

#Three types to consider
#Strings - Store collections of characters
# result = str(<value>)
#integers - Store integer values
# result = int(<value>)
#floats - Store real numbers
# result = float(<value>)


#Output
print("your slope is m="+str(rise)+"/"+str(run))
print("Your slope as a decimal is "+str(fSlope))
os.system("say your slope is m="+str(rise)+"/"+str(run))
os.system("say your slope as a decimal is "+str(fSlope))
print(rise)
print(run)
os.system("say thank you for using this slope calculator")






