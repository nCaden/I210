# paste this test code in one line at a time into the interactive mode
# then answer the questions using complex comparisons

bike1_brand = "Trek"
bike1_bell = True
bike1_color = "silver"
bike1_kickstand = False
bike1_gears = 21
bike2_brand = "Cannondale"
bike2_bell = True
bike2_color = "purple"
bike2_kickstand = True
bike2_gears = 7

print(bike1_color == bike2_color) and (bike1_brand == bike2_brand)
print(bike1_bell == True) or (bike1_kickstand == True)
print(bike2_gears > 3 ) and (bike2_gears <= bike1_gears)