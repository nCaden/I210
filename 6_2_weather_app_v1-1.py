# 6.2 Weather app (version 1)
# a tries really hard to be helpful app where YOU enter all the information!

# SETUP - Welcome the user to Weather App 1.0
print("Welcome to Weather App 1.0")
# (1) Weather app converts your temperature!
# INPUT - ask the user some weather related questions
# Q1: Please enter your current temperature:
# Q2: Is this temperature in Fahrenheit or Celsius? Enter F or C:
current_temp = float(input("Please enter your curent temperature:"))
temp_type = input("Is this temperature in Fahrenheit or Celsius? Enter F or C:")

# PROCESSING / OUTPUT - helpfully calculate the temperature in F or C
# temperatures should be displayed to one decimal position
# Figure out if the temperature is "hot" (75 or higher F) or "cold" (40 or lower F)
if temp_type == 'F':
    temp_calc = (current_temp-32) * 5/9
    hot = current_temp >= 75
    cold = current_temp <= 40
    print(f"Your current temperature is {current_temp} F / {temp_calc:.1f} C")
elif temp_type == 'C':
    temp_calc = (current_temp * 9/5) + 32
    hot = temp_calc >= 75
    cold = temp_calc <= 40
    print(f"Your current temperature is {temp_calc} F / {current_temp:.1f} C")


# (2) Weather app tells you what to wear!
# Let's figure out what you should wear to be prepared for the weather...
print("Let's figure out what you should wear to be prepared for the weather...")
# SETUP
# Print a message to explain we're asking about current weather conditions.
# INPUT - ask user about current conditions
# What are your current weather conditions?
print("What are you current weather conditions?")
# Q3: Enter sunny, raining, or neither:
weather_conditions = input("Enter sunny, raining, or neither:")
# PROCESSING - create custom advice on user's fashion choices
    # raining and hot
    # raining and cold
    # raining and neither
    # sunny and hot
    # sunny and cold
    # sunny and neither
    # hot
    # cold
    # neither - advise the user to wear layers
if weather_conditions == 'raining' and hot:
    print("Wear a windbreaker and shorts")
elif weather_conditions == 'raining' and cold:
    print("Wear a raincoat and pants")
elif weather_conditions == 'raining':
    print("Wear a windbreaker")
elif weather_conditions == 'sunny' and hot:
    print("Wear a tank top and shorts")
elif weather_conditions == 'sunny' and cold:
    print("Wear a coat and sunglasses")
elif weather_conditions == 'sunny':
    print("Wear a pair of sunglasses")
elif weather_conditions == hot:
    print("Wear a t-shirt and shorts")
elif weather_conditions == cold:
    print("Wear a coat")
else:
    print("Wear layers")
    

# OUTPUT - print out the message


