# 11.1 valid zip

# Part 1
# write a function valid_zip that takes an user-entered string and
# checks to see if it is 5 characters long
# note: len() will work on strings, but not integers
# returns True or False
def valid_zip():
    return 5 == len(zip_code)
    


# main
# input - get a zip code from the user
zip_code = (input("Please enter your zip code: "))

# Part 1
# processing - make sure the zip is valid
print(valid_zip())

# Part 1
# output whether the zip code is valid (True or False)
