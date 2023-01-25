#!/usr/bin/env python
# coding: utf-8

# In[12]:


ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
ages.append(min(ages))
ages.append(max(ages))
print((sum(ages))/len(ages))
ages.sort()
print((ages[6]+ages[7])/2)
print(max(ages)-min(ages))


# In[23]:


dog={}
dog={ "name":"milkshake", "color":"white", "breed":"jersey", "legs":"4", "age":"10"}
student={ "first_name":"Manisha", "last_name":"Addula", "gender":"Female", "age":"22", "marital status":"single",
"skills":["java", "python", "web development"], "country":"USA", "city":"OverLand Park", "address":"1111,ABC Street"}
print(len(student))
print(student['skills'])
print(type(student['skills']))
student["skills"].append("html")
print(student.keys())
print(student.values())


# In[56]:


brothers=("laddu","sai") #Brother Tuple Creation
print(brothers)
sisters=("Mouni","pandu") #Sister Tuple Creation
print(sisters)
siblings=brothers+sisters #Merging brother and sister tuples
print(siblings)
print("Sibblings Count:",+len(siblings)) #printing tuple length
siblings=("Parameshwar", "vijitha")+siblings #adding father and mother
print("Siblings:",siblings) #printing after parents added
family_members=siblings #assigning siblings to family members
print("Family Members:",family_members) #printing family members


# In[28]:


it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
it_companies.add('Twitter') #adding values
print(it_companies)
adding_companies=["Zensar","HighRadius","Hexaware","PWC"] #appending values
it_companies.update(adding_companies)
print(it_companies)
it_companies.remove("PWC")
it_companies.discard("HCL") #though HCL is not in the set it doesn't throwed an error while performing operation where as remove does
print(it_companies)
print(A.union(B))
print(A.intersection(B))
print(A.issubset(B)) #Return true since A is subset of B)
print(A.isdisjoint(B)) #Return false A and B are not disjoint sets
print(A.union(B))
print(B.union(A))
print(A.symmetric_difference(B))
A.clear()
B.clear()
print(A)
print(B)
age2=set(age)
print(age2)
print(len(age))
print(len(age2))
if(len(age2)>len(age)):
   print("set size is greater than list size")
elif(len(age)<len(age2)):
   print("list size is greater than the set size")
else:
   print("set size is equal list size")


# In[39]:


radius=30
print("Default Radius:%s" % radius) #printing given radius
def area(t): #function declaration for area
    area_of_circle=3.14*(t)**2 #formula
    print("Area: %s mt/s^2" % area_of_circle)
def circum(t): #function declaration for circumference
    circum_of_circle=2*3.14*(t) #formula
    print("Circumference: %s mt/s" % circum_of_circle)
area(radius) #function call
circum(radius)
while(True):
    radius=float(input("Enterradius:"))
    if(radius==0):
        break
    elif(radius>0):
        area(radius) #calling area function
        circum(radius) #calling circumference function
    elif(radius<0):
        print("Radius can be calculated for positive values")
    else:
        print("Please enter a valid input")


# In[55]:


str = "I am a teacher and I love to inspire and teach people"
splt = str.split()
set_splt = set (splt)
unique_splt = ( list (set_splt))
for n in unique_splt:
    print (n)
print(len(unique_splt))

    


# In[40]:


print("Name\t\tAge\tCountry\t City") #printing header
print("Asabenah\t250\tFinland\t Helsinki") #printing values


# In[48]:


#Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
f'The area of a circle with radius {radius} is {area} meters square.'


# In[41]:


num=int(input("Enter number of Students: ")) #user input
if(num>0):
    weight=[] #enters only entered number >=0
    for i in range(0,num):
        lb=float(input("Enter weight in lb: ")) #user input of weights
        kg=lb*0.454 #converting lb to kgs
        weight.append(kg) #add to list
else:
    print("Enter the valid number of students") 
print(weight)

