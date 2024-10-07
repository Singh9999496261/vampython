#oops in python 

#object oriented programming language

#class  -> it is a container which collection variables ,function

# example -> shailendra class
# shailendra.fullname="shailendrasingh"
# shailendra.age=19
# shailendra.sleeping()
# shailendra.eating()
# shailendra.watching()

class ClassName:
 print("this my class")
class shailendra:
  age =19
  fullName= "shailendra singh"
  email = "shailendrasingh9253@gmail.com"
  def pocketMoney(this,amount):
    print("my pocket is ",amount)
  def monthlysalary(this,daysalary):
    totalsalary = 31*daysalary
    print("your mopnthly salary is",totalsalary)


#create class object :
shailendra :shailendra = shailendra()
shailendra.pocketMoney(5000)
shailendra.monthlysalary(int(input("enter your one day salary")))
print(shailendra.fullName,shailendra.age,shailendra.email)
