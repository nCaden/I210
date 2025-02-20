#Mastery Check 0
#Goal: Debugging code

#INPUT
student1 = "Amy"
student2 = "Carmen" #invalid variable name cannot have spaces
student3 = "Josh"
student4 = "Simon" #missing an end quotation
student5 = input("Enter student name: ")

score1 = 96
score2 = 92
score3 = 73
score4 = 81 #variable cannot start with a number
score5 = int(input("Enter a student score: "))

#PROCESSING

#Calculate the average score
avg_score = (score1+score2+score3+score4+score5)/5

#Calculate the highest score
high_score = max(score1,score2,score3,score4,score5)

#Calculate the lowest score
low_score = min(score1,score2,score3,score4,score5)


#OUTPUT
print("--"*23)
#output the average score
print("The average student score was", avg_score) #missing a quotation mark at the end

#output the high score
print("The high score was", high_score) #missing an end parenthesis

#output the low score
print("The low score was", low_score) #"lowest_score" is not a variable, meant low_score

#output student names
print("Students who took this assignment include", student1 + ",", student2 + ",", student3 + ",", student4 + ", and", student5 +".") #there is no student6 must have meant student5 which is missing
print("--"*23)
print(f"{student5} is my favorite student") #making use of a "f-string" to recieve my bonus point