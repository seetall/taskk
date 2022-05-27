'''data=[1,"Sunil","Roshan"]
for i in data:
    print(i)'''
'''
data=[1,"Sunil","Roshan"]
print(data[1])'''
'''
data=[1,"Sunil","Roshan"]
print(data[0:2])
'''
'''
data=list(range(0,10,1))
print(data)'''

'''append is used to pass single value. stores value at last
data=[1,"Sunil","Roshan"]
print(data)
data.append(9)
data.append("Programming")
print(data)'''
'''
data=[1,"Sunil","Roshan"]
print(data)
data.insert(2,"Battle")
print(data)'''
'''
mixed_list=[{1,2},[5,6,7],{"a":"r"}]
number_tuple=(3,4)
mixed_list.insert(1,number_tuple)'''
'''
data=[1,"Sunil","Roshan"]
print(data)
data[0]=8
data[1]=10
print(data)'''
'''
data=[1,"Sunil","Roshan"]
print(data)
del data[1]
print(data)
'''
'''
data=[1,"Sunil","Roshan"]
print(data)
data.remove(1)
print(data)'''

#pop: deletes the last element
'''
data=[1,"Sunil","Roshan"]
print(data)
data.pop()
print(data)'''

'''
data=[1,"Sunil","Roshan"]
data2=["a","b"]
print(data+data2)'''
'''
data=[1,"Sunil","Roshan"]
data2=[]
data2=data.copy()
print(data)
print(data2)'''

#extend: to store mutiple element
'''
data=[1,"Sunil","Roshan"]
data2=["a","b",12]
data2.extend(data)
print(data2)'''
'''
data=[1,"Sunil","Roshan"]
data.clear()
print(data)'''
'''
data=(1,"Sunil","Roshan")
print(data) '''
'''
data=(1,"Sunil","Roshan")
for i in data:
    print(i)'''
'''
data=(1,"Sunil","Roshan")
print(data[1])

data=(1,"Sunil","Roshan")
print(data[0:2])'''
'''
data=tuple(range(0,10,1))
print(data)'''
'''
data=(1,"Sunil","Roshan")
print(len(data))'''
'''
num=(1)
num1=(1,)
print(type(num))
print(type(num1))'''
'''
data=(1,"Sunil","Roshan",[20,40,"a"])
print(data)
'''
'''
data=(1,"Sunil","Roshan",[20,40,"a"])
print(data)
print(len(data))
data[3].pop()
print(data)
data[3].append("master")
print(data)
data[3].remove(40)
print(data)'''
'''
print("maximum is:",max(1,2,3,4,5))
print("minimum is:",min(1,2,3,4,5))'''
'''
tuple1=("Ram","Shyam",,"Mohan")
print("original tuple", tuple1)
list1=list(tuple1)
print("original list", list1)
list1.insert(3,"ktishna")
print("changed list", list1)'''

#SET

'''add is used to add in set'''
'''
data={1,2,3,4}
data.add(5)
print(data)'''
'''
data={1,2,3,4}
data.remove(1)
print(data)'''
'''
a={"lemon","cat","cherry"}
a.discard("cat")
print(a)'''
'''
data=(1,2,3,4,5,"Danish")
if "Danish" in data:
    print("present")
else:
    print("Absent")'''
'''
data={1,2,3,4,5,6}
data.clear()
print(data)'''
'''
data={1,2,3,4,5,6}
print(data)
data2=data.copy()
print(data2)'''
'''
x={"a","b","c"}
y={"d","e","f"}
x.update(y)
print(x)'''
#union |
'''
data1={1,2,3,4}
data2={2,4,5,6}
union_set=data1 | data2
print(union_set)'''

#intersection(data1.intersection data2)
'''
data1={1,2,3,4}
data2={2,4,5,6}
intersection_set=data1 & data2
print(intersection_set)'''
#symmetric(data1.symmetric (data2)_
#difference(data1.difference (data2)
#isdisjoint:output true if data of data1 doesnt matches with data2)
'''
data1={1,2,3,4}
data2={2,4,5,6}
intersection_set=data1. isdisjoint (data2)
print(intersection_set)
'''
#issubset:output true when data of data1 and data2 matches)
'''
data1={1,2,3,4}
data2={2,4,5,6}
intersection_set=data1.issubset (data2)
print(intersection_set)'''








#DICTIONARY(indexing not allowed(unordered)), same key isnt passed but same value is passed
'''
data={"name":"sunil rawat","age":17}
print(data)

data1=dict(name="sunil", age=17)
print(data1)'''
'''
data={"name":"sunil rawat","age":17}
print(data)
for i in data:
    print(i)
for i in data.items():
    print(i)
for i in data.values():
    print(i)'''
'''
data={"name":"sunil rawat","age":17}
for "name" in data:
    print("Present")
else:
    print("Not present")

if "sunil rawat" in data.values():
    print("present")
else:
    print("Ansent")'''
'''
data={"name":"sunil rawat","age":17}
data2={"fav movie": "3 idiots", "sport": "Boxing"}
data.update(data2)
print(data)

data={"name":"sunil rawat","age":17}
del data["age"]
print(data)'''
'''
data={"name":"sunil rawat","age":17}
print(data)
remove_pop=data.pop("age")
print(remove_pop)'''
'''
data={"name":"sunil rawat","age":17}
print(data)
get_data=data.get("name")
print(get_data)'''
'''
data={"name":"sunil rawat","age":17}
print(data)
data.clear()
print(data)'''
'''
data={"a":1,"B":17}
new_key="A"
old_key="a"
data[new_key]=data.pop[old_key]
print(data)
'''

'''
a=[1,2,3,4]
b=[]
for i in range(len(a)-1,-1,-1):
    b.append(a[i])
print(b)

lst=[1,2,3,4]
new=[]
count=len(lst)-1
while count>=0:
    new.append(lst[count])
    count-=1
print(new)
'''
'''
a=[1,2,3,4]
sum=1
for i in a:
    sum=sum*i
print(sum)

a=[5,10,15,20]
sum=1
c=len(a)
i=0
while i<c:
    sum=sum*a[i]
    i=i+1
print(sum)
'''
def smallestnumber(numbers):
    smallest_num=numbers[0]
    for num in numbers:
        if num>smallest_num:
            smallest_num=num
    return smallest_num
print(smallestnumber([657,233,666,123,45,987]))



