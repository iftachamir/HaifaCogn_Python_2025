# Define the function
def bmi(grams, cms):
    # Convert to kgs and metres
    kgs = grams / 1000
    metres = cms / 100

    # BMI Formula
    BMI_value = kgs / (metres**2)
    return(BMI_value)

# Call the function
weight_g = int(input('Weight in *grams*:'))
height_cm = int(input('Height in *cm*:'))
b = bmi(weight_g, height_cm)
print(b)
