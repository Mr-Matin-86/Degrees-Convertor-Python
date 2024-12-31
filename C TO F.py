from tkinter import messagebox
def Convert(x):
    if x == "C":
        return (C * 1.8) + 32
    if x == "F":
        return (F - 32) / 1.8
while True:
    Cond = input("What is Type Of Your Tempreture(C / F)?Enter 0 To Exit:  ")

    if Cond.capitalize() == "C":
        C = int(input("Enter the temperature in degrees Celsius:  "))
        print(Convert(Cond))
    elif Cond.capitalize() == "F":
        F = int(input("Enter the temperature in degrees Fahrenheit:  "))
        print(Convert(Cond))
    elif Cond.capitalize() == "0":
        break
    else:
        messagebox.showerror("Error", "Please Input Correct Value.")