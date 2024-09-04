from itertools import product,  permutations, combinations, accumulate, groupby
import operator

a=[1,2,3,4,5]

# res=accumulate(a,func=operator.mul)
# print(list(res))

def greaterThan(data: int)-> bool:
    return data > 3


res=groupby(a, key=lambda data : data > 3)

for k,v in res:
    print(k, list(v))

 

import os


with open("greater.txt","w") as f:
    f.write("this is the line 1")
    f.write("this is line 2")
    f.write("this is line 3")


with open("greater.txt","r") as rf:
    outputData=rf.read()
    print(outputData)



    # try and catch , excetpions , loggings ,  generators, 
    # create a class with customer (name, id, age, bmi,  training period, calories burnt, created_at, emaiid, password, profession)
    #[custom1,cust2.. custn]
    #final op/p dict => cust1:{name:abc, id:1, age:23,bmi:86, tp: 3 mo, cb:10}

import os
with open("list.txt","w") as ed:

 
        Customer1={"name":"Vinay","id":100 ,"age":23,"BMI":24.5,"tp":"6 months","Calories_burnt":"1000cal","Created_at":"12.02.23","e-mail":"vinay23@gmail.com","Password":"Vinay@2011","Profession":"Data-analyst"}
        Customer2={"name":"Madhan","id":101 ,"age":24,"BMI":22.75,"tp":"3 months","Calories_burnt":"1200cal","Created_at":"21.03.23","e-mail":"madhanisactive11@gmail.com","Password":"ma-dan@2004","Profession":"Enterpreneur"}
        Customer3={"name":"Vijay","id":102 ,"age":31,"BMI":19.66,"tp":"12 months","Calories_burnt":"2000cal","Created_at":"31.01.24","e-mail":"MailtoVijay@gmail.com","Password":"Vijaycanlift@1996","Profession":"software-Engineer"}
        Customer4={"name":"Mukesh","id":103 ,"age":19,"BMI":29.33,"tp":"18 months","Calories_burnt":"750cal","Created_at":"27.06.23","e-mail":"virumandimukesh@gmail.com","Password":"virumandi@2002","Profession":"Driver"}
        Customer5={"name":"Abishek ","id":104 ,"age":21,"BMI":22.11,"tp":"12 months","Calories_burnt":"1450cal","Created_at":"03.03.23","e-mail":"swathiist@gmail.com","Password":"Swathi__101","Profession":"App developer"}

for k,v in enumerate(Customer2):
        print(k,v)


print(Customer3.items())
n=int(input("enter the num:- "))
for i in range(0,n-4):
    if(i%3==0):
        print(i, end=" ")
    else:
        print(" ")
        
    
with open("loginpage.txt","w") as ab:
    ab.write("hey this is your musclenation gym !!")
with open("kart.txt","w") as ka:
    ka.write("this is madness")   