# 4.1 Madlibs
# Create a madlib game

# SET UP
madlib = "\nMY STORY\nI was {} across campus on my way to class today\
    and I saw two {} {}. I was surprised to see them on a campus in {}.\
    I {} around to see if anyone else saw what I was seeing; but no one was there. \
    I decided to investigate. I {} after the pair of {} as they {} off. \
    What I discovered was unimaginable! The two {} were \
    headed to what must have been a {}. There were at least {} {} ! \
    There were {} of all colors and sizes! I saw {} ones and {} ones, too. \
    It was {} to see so many {} all together. \
    Unfortunately, it was time for class; and, I couldn't be late. So, I had to say \
    {} to my new friends, the {}. I hope to see them around another day soon.\n"

# INPUT a user choice for each keyword
#STEP 1 - place variable names on each input line below (lines 21-33)
#STEP 2 - place the correct variable names you assign in step 1 to the \
#       corresponding places in the madlib paragraph above. They are in order unless noted.
print("Let's write a story together!\n")
verb = input("Enter a verb ending in -ing, e.g. stomping: ")
adj1= input("Enter a color: ")
animal= input("Enter an animal in plural, e.g. bats: ")
country= input("Enter a country name: ")
past_tense_verb1 = input("Enter a verb in the past tense: ")
past_tense_verb2= input("Enter a verb in the past tense: ")
past_tense_verb3 = input("Enter a verb in the past tense: ")
location = input("Enter a festive location, e.g. celebration: ")
num = input("Enter a large number: ")
adj2 = input("Enter an adjective: ")
color = input("Enter a color: ")
emotion = input("Enter an emotion: ")
greeting = input("Enter a greeting: ")


#STEP 3 - PROCESS / OUTPUT using .format()
# each keyword matches to a placeholder in the madlib story
# print out the result to read your completed madlib
print(madlib.format(
    verb, adj1, animal, country, 
    past_tense_verb1, past_tense_verb2, animal, past_tense_verb3, 
    animal, location, num, animal, adj2, color, 
    adj2, color, emotion, animal, greeting, animal
))
#STEP 3B - WARNING: If you want to use f strings, you need to move the SETUP
# template to be UNDER the inputs. Then add the f to the template.
madlib = (f"\nMY STORY\nI was {verb} across campus on my way to class today\
    and I saw two {adj1} {animal}. I was surprised to see them on a campus in {country}.\
    I {past_tense_verb1} around to see if anyone else saw what I was seeing; but no one was there. \
    I decided to investigate. I {past_tense_verb2} after the pair of {animal} as they {past_tense_verb3} off. \
    What I discovered was unimaginable! The two {animal} were \
    headed to what must have been a {location}. There were at least {num} {animal} ! \
    There were {animal} of all colors and sizes! I saw {adj2} ones and {color} ones, too. \
    It was {emotion} to see so many {animal} all together. \
    Unfortunately, it was time for class; and, I couldn't be late. So, I had to say \
    {greeting} to my new friends, the {animal}. I hope to see them around another day soon.\n")
print(madlib)
