userName= "shailendra singh"
for i in userName:
     print(i)

    #print 1 to 10 using for loop
for i in range(1,11):

    print(i*2)


#wap to create table of any no by user
# tableno=int(input("enter no for create table"))

#WAP to print even no from 1 to 10 using for loop
# for a in range(1,11):
#   if a % 2 ==0: 
#     print(a)

#WAP print this pattern 1 4 7 10 13 using for loop
# for i in range(1, 14,3):
#     print(i)

#WAP print this pattern 1 3 7 13 15 using for loop
# for i in range(1,16,2):
#   if i == 9 or i==5:
#         continue
# else:
#         print(i)

n=[1,2,3,4,5]

squares=[n**2 for n in n]
print(squares)



