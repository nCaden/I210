# 4.1 Madlibs
# Create a madlib game

# SET UP


# INPUT a user choice for each keyword 
print("Let's write a story together!\n")

job_title = input("Enter a job title, e.g. plumber: ")
noun = input("Enter a noun: ")
volume_level = input("Enter a volume level, e.g. loud: ")
face_part = input("Enter a part of a face or head: ")
adjective1 = input("Enter an adjective: ")
place = input("Enter a place: ")
drink = input("Enter a kind of drink, e.g. tea: ")
adjective2 = input("Enter another adjective: ")
animal = input("Enter an animal: ")
adjective3 = input("Enter a final adjective: ")
family_member = input("Enter a family member, e.g. cousin: ")

madlib = (f"\nMY STORY\nEverytime I have to zoom into class, my {job_title} complains \
that I don't have my {noun} turned on. Half the time, their sound is on \
{volume_level} and their {face_part} is cut off by their {adjective1} \
virtual background of {place}. Plus, they always seems to be drinking {drink}. \
So, I don't really see what the problem is. But it's also true that pretty \
much every time, my {adjective2} {animal} jumps up on the keyboard, and my \
{adjective3} {family_member} walks around behind me. I guess no one is perfect.\n")

print(madlib)
# 1A - PROCESS / OUTPUT using .format()
# each keyword matches to a placeholder in the madlib story
# print out the result to read your completed madlib

# 1B - WARNING: If you want to use f strings, you need to move the SETUP
# template to be UNDER the inputs. Then add the f to the template.

