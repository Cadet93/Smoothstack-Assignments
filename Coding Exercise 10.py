#Day 5 –Weekend exercise work – please use functions for this problem

#Let us apply our programming skills to some quasi-scientific problem - since it is bit dull to learn only abstract things.
#The simple measure of body constitution was proposed at the middle of XIX century.
#It depends only on the height and weight of a person - and is called Body Mass Index or BMI. It is defined as:
#BMI = weight / height^2
#Where weight is taken in kilograms and height in meters.
#Four general grades are proposed:
#Underweight     -           BMI < 18.5
#Normal weight   -   18.5 <= BMI < 25.0
#Overweight      -   25.0 <= BMI < 30.0
#Obesity         -   30.0 <= BMI
#For example, if I have weight of 80 kg and height of 1.73 m I can calculate:
#BMI = 80 / (1.73)^2 = 26.7
#i.e. somewhat overweight.
#We will not discuss how proper or improper this gradation is. Instead you should simply calculate grades for several people.
#Input data contain number of people in the first line.
#Other lines will contain two values each - weight in kilograms and height in metres.
#Answer should contain words under, normal, over, obese for each corresponding test-case, separated with spaces. For example:
#input data:
#3
#80 1.73
#55 1.58
#49 1.91
 
#answer:
#over normal under

def bmi_class(weight, height):
    bmi = round(weight / (height * height), 2)
    print(bmi)
    if bmi < 18.5:
        return "underweight"
    elif bmi >=18.5 and bmi <= 25.0:
        return "normal"
    elif bmi >= 25.0 and bmi <= 30.0:
        return "overweight"
    else:
        return "obese"


classifications = []
num_people = int(input("Input number of people: "))

for person in range(num_people):
    height = float(input("Input your height in meters: "))
    weight = float(input("Input your weight in kilogram: "))
    classifications.append(bmi_class(weight, height))
    
print(' '.join(classifications))




