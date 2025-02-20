# Career Decision Tree
print("Welcome to the Career Decision Tree!")

# Ask about preferred subjects
subject_pref = input("Do you prefer Math or English? ")

# Ask about working environment preference
work_environment = input("Do you prefer working indoors or outdoors? ")
                         
# Ask about additional preferences
group_pref = input("Do you prefer working with people, with animals, or alone? ")

#Create jobs to recommend based on all the options

#Enjoy math, working indoors, and with people -> Math Teacher
#Enjoy math, working indoors, and alone -> Accountant
#Enjoy math, working indoors, and with animals -> Animal Shelter
if subject_pref == 'Math' and work_environment == 'indoors' and group_pref == 'with people':
    print("Math Teacher")
elif work_environment == 'indoors' and group_pref == 'alone':
    print("Accountant")
elif work_environment == 'indoors' and group_pref == 'with animals':
    print("Animal Shelter")
#Enjoy math, working outdoors, and alone -> Geologist
#Enjoy math, working outdoors, and with people -> Carpenter
#Enjoy math, working outdoors, and with animals -> Dog Walker
if subject_pref == 'Math' and work_environment == 'outdoors' and group_pref == 'alone':
    print("Geologist")
elif work_environment == 'outdoors' and group_pref == 'with people':
    print("Carpenter")
elif work_environment == 'outdoors' and group_pref == 'with animals':
    print("Dog walker")

#Enjoy english, working indoors, and alone -> Copy Editor
#Enjoy english, working indoors, and with people -> Marketing Manager
#Enjoy english, working indoors, and with animals -> Animal Shelter Worker
if subject_pref == 'English' and work_environment == 'indoors' and group_pref == 'alone':
    print("Copy Editor")
elif work_environment == 'indoors' and group_pref == 'with people':
    print("Marketing Manager")
elif work_environment == 'indoors' and group_pref == 'with animals':
    print("Animal Shelter Worker")
#Enjoy english, working outdoors, and alone -> Forest Ranger
#Enjoy english, working outdoors, and with people -> Boys/Girl Scout Leader
#Enjoy english, working outdoors, and with animals -> Dog Trainor
if subject_pref == 'English' and work_environment == 'outdoors' and group_pref == 'alone':
    print("Forest Ranger")
elif work_environment == 'outdoors' and group_pref == 'with people':
    print("Boys/Girl Scout Leader")
elif work_environment == 'outdoors' and group_pref == 'with animals':
    print("Dog Trainer")

