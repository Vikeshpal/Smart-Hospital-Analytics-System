def create_age_group(df):

    age_group = []

    for age in df["Age"]:

        if age <= 18:
            age_group.append("Child")

        elif age <= 35:
            age_group.append("Young Adult")

        elif age <= 55:
            age_group.append("Adult")

        else:
            age_group.append("Senior")

    df["Age_Group"] = age_group

    return df  


def create_bmi_category(df):

    bmi_category = []

    for bmi in df["BMI"]:

        if bmi < 18.5:
            bmi_category.append("Underweight")

        elif bmi < 25:
            bmi_category.append("Normal")

        elif bmi < 30:
            bmi_category.append("Overweight")

        else:
            bmi_category.append("Obese")

    df["BMI_Category"] = bmi_category

    return df