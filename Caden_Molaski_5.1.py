#Code-like 5.1 Movie Age Ratings

#PG rated Movies (everyone can view)
#PG-13 rated Movies (13+ can view)
#R rated Movies (17+ can view)

#INPUT

#Ask user for their age
age = int(input("Enter your age:"))
#PROCESSING

#check users age

#if they are under 13, they can see PG movies
   #output movie ratings they can watch
if age < 13:
   print(f"At {age} years old, you can see PG rated movies.")
#if they are 13 or older but under 17, they can see Pg and Pg-13 mvoies
   #output movie ratings they can watch
elif 13 <= age < 17:
   print(f"At {age} years old, you can see PG, PG-13 rated movies.")   
#if they are 17 and over, they can see PG, PG-13 and rated R movies
    #output movie ratings they can watch
elif age >= 17:
   print(f"At {age} years old, you can see PG, PG-13 and rated R movies.")