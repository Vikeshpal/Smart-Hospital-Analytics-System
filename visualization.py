import matplotlib.pyplot as plt


# ------------------------------------
# Age Distribution Histogram
# ------------------------------------
def age_distribution(df):

    plt.figure(figsize=(8,5))

    plt.hist(df["Age"], bins=5, color="skyblue", edgecolor="black")

    plt.title("Age Distribution")

    plt.xlabel("Age")

    plt.ylabel("Number of Patients")

    plt.grid(axis="y", linestyle="--", alpha=0.5)

    plt.show()


# ------------------------------------
# Disease Distribution Bar Chart
# ------------------------------------
def disease_bar_chart(df):

    disease_count = df["Disease"].value_counts()

    plt.figure(figsize=(8,5))

    plt.bar(
        disease_count.index,
        disease_count.values,
        color=["red", "green", "blue"]
    )

    plt.title("Disease Distribution")

    plt.xlabel("Disease")

    plt.ylabel("Number of Patients")

    plt.grid(axis="y", linestyle="--", alpha=0.5)

    plt.show()


# ------------------------------------
# Disease Percentage Pie Chart
# ------------------------------------
def disease_pie_chart(df):

    disease_count = df["Disease"].value_counts()

    plt.figure(figsize=(6,6))

    plt.pie(
        disease_count.values,
        labels=disease_count.index,
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Disease Percentage")

    plt.show()


# ------------------------------------
# BMI Box Plot
# ------------------------------------
def bmi_box_plot(df):

    plt.figure(figsize=(8,5))

    plt.boxplot(df["BMI"])

    plt.title("BMI Distribution")

    plt.ylabel("BMI")

    plt.grid(axis="y", linestyle="--", alpha=0.5)

    plt.show()