#Codelike 7.2 Where's Waldo
print("Where’s Waldo?")
print("Guess the secret location!")

#list of countries
countries = ["Belgium", "Bolivia", "Brazil", "China", "Colombia", "Costa Rica", "Denmark", "France", "Germany", "India", "Italy", "Japan",
             "Norway", "Russia", "Switzerland", "United States", "Zimbabwe"]

#
print("Countries to choose from: ", countries)

random_number = int(input("Choose a random number: "))
secret_location = countries[random_number] 

#LOOP
    #Ask user to guess where they think Waldo is
guess = input("Where do you think waldo is ? ")
    #if they are wrong, tell them and ask them to try again
while guess != secret_location:
    print("Wrong try again")
    guess = input("Where do you think waldo is ? ")

print(f"Correct it was {secret_location}")
       
#if they are right, tell them and end loop/program