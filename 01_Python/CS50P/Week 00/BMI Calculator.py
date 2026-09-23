def main():
    height = float(input("Your Height (m): "))
    weight = float(input("Your Weight (in Kg): "))

    BMI = weight/(height ** 2)
    BMI = round(BMI, 1)
    print("Your BMI is", BMI)

main()