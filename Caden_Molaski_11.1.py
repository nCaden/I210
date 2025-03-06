# 11.2 valid email

# Part 1
# write a function valid_email that takes an user-entered string and
# checks to see if it is has a @ symbol
# returns True or False
def valid_email(email):
     valid = "@" in email
     return valid
        

# Part 2
# write a function iu_email that takes a user-entered string
def iu_email(email):
    if valid_email(email) == True:
        valid = "iu.edu" in email
        return valid
    else:
        return False
# first use valid_email() to if that string is a valid email
# then checkes if iu.edu is in the email
# if it is, it returns True
# if it is not, it returns False

# main
# input - get an email from the user
email = input("Please enter your email: ")

# processing - check if it is a valid email
valid = valid_email(email)

# Part 1
# output whether the zip code is valid (True or False)
print("Is this a valid email?", valid)

# Part 2

#check if it is a valid iu email

iu_valid = iu_email(email)

print("Is this an iu email?", iu_valid)
