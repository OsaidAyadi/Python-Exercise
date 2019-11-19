#Q1
print("Hello \n\t Hello \n\t \t Hello")
#Q2
print("Orange academy \n" *20 )
#Q3
a=float(1)
b=float(2.8)
c=float("3")
d=float("4.2")
print(a,b,c,sep=' 10 ')
#Q4
x1=int(input("enter num1:" ))
y1=int(input("enter num2:" ))
print ("your oproduct is", x1*y1)
#Q5
avg=eval(input("enter five numbers with (,) between them :"))
res=0
for x in avg:
    res=res+x
print (res/5)
#Q6
x=1
y=2.8
z=1j
org="Orange"
A=True
print(type(x),type(y),type(z),type(org),type(A))
#Q7
str1,str2="Osaid",1
str3,str4=100,-1
print(str1,str2,str3,str4)
#Q8
q=10
print(q)
q_Q="orange"
print(q_Q)
AB=10
print(AB)
print("10"*10)
#Q11
#Q12
name,age=input("enter your Name and your Age with (,) between them :").split(",")
age=int(age)
div=100-age
print("Hello" ,name, "at ",2019+div,"Years to turn 100")
#Q13
base, h= input ("enter base and height of tringale with (,) between them :").split(",")
print("the Area is", int(base)*int(h)/2)


