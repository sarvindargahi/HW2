

dict1=[{"name":"ali","age":"20"},{"name":"amin","age":"19"}]
print(dict1[0])
print(dict1[1]["age"])

user=[]

tedad_karbar=int(input("tedad ra vared konid= "))

for i in range(tedad_karbar):
    name=input("nam  ra vared konid= ")
    age=input("sen ra vared konid= ")
    user.append({"name":name,"age":age})
print(user)

x=input("nam ra baraye jostejo vared konid= ")
flag=0
n=0
for j in range(tedad_karbar):
    if user[n]["name"]==x:
        print(user[n]["age"])
        flag=1
        break
    n+=1
if flag==0:
    print("karbar mored nazar yaft nashod!")
    

