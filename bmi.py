def calculate_bmi(height,weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight/(height*height)
    print(bmi)

    if bmi < 18.5:
        status = "Underweight"
    elif bmi >= 18.5 and bmi <=25.0:
        status = "Normal Weight"
    elif bmi > 25.0:
        status = "Overweight"

    print(status)

calculate_bmi(weight=90,height=1.73)