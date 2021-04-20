import pandas as pd

patients_df = pd.read_json('data.json')


def BMI(weight, height):
    bmi = weight / (height / 100) ** 2
    return bmi


def BMI_Category(bmi):
    if bmi <= 18.4:
        return "Underweight"
    elif bmi <= 24.9:
        return "Normal Weight"
    elif bmi <= 29.9:
        return "Overweight"
    elif bmi <= 34.9:
        return "Moderately obese"
    elif bmi <= 39.9:
        return "Severely obese"
    else:
        return "Very severely obese"


def Health_Risk(bmi):
    if bmi <= 18.4:
        return "Malnutrition Risk"
    elif bmi <= 24.9:
        return "Low Risk"
    elif bmi <= 29.9:
        return "Enhanced Risk"
    elif bmi <= 34.9:
        return "Medium Risk"
    elif bmi <= 39.9:
        return "High Risk"
    else:
        return "Very High Risk"


df = pd.DataFrame(patients_df)
df['BMI'] = [BMI(weight, height) for weight, height in zip(patients_df['WeightKg'], patients_df['HeightCm'])]
df['BMI Category'] = [BMI_Category(bmi) for bmi in patients_df['BMI']]
df['Health Risk'] = [Health_Risk(bmi) for bmi in patients_df['BMI']]
print(df)
