# 13.3 valid zip update

def valid_zip(is_zip):
    # update the code hereto see: 
    #   if zip code is 5 characters long OR 10 characters long
    #   if zip is 5 -- make sure it's all digits
    #   if zip is 10 -- make sure it's 5 digits, one + sign, and 4 digits
    if len(is_zip) == 5 and is_zip.isdigit():
        return True
    elif len(is_zip) == 10:
        return is_zip[:5].isdigit() and is_zip[5] == "+" and is_zip[-4:].isdigit()
    else:
        return False


# customized location info for each valid zip code
def find_zip(is_zip):
    if not valid_zip(is_zip):
        return "That's not a valid zip code."

    # update this to checks only the base zipcode
    # a.k.a. the first five numbers
    if 47401 <= int(is_zip[:5]) <= 47408:
        return "How's the weather in Bloomington?"
    else:
        return "How's the weather in your hometown?"

# main
# take zipcode in as a string to start - convert to int() when needed
zip_code = input("Please enter your zip code: ")

result = find_zip(zip_code)

print(result)

