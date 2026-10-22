
print("-------------------------------------")
print("Grade Match Case")
print("-------------------------------------")

Grade = input("Enter your Grade (A/B/C/D/F): ")

match Grade:
    case "A":
        print("Excellent")
    case "B":
        print("Very Good")
    case "C":
        print("Good")
    case "D":
        print("Pass")
    case "F":
        print("Fail")
    case _:
        print("Invalid Grade")


print("-------------------------------------")
print("Arithmetic Match Case")
print("-------------------------------------")

a = 4
b = 9

Operator = input("Enter your Operator (+,-,*,/,//,**): ")

match Operator:
    case "+":
        print("Addition of", a, "+", b, "=", a + b)
    case "-":
        print("Subtraction of", a, "-", b, "=", a - b)
    case "*":
        print("Multiplication of", a, "*", b, "=", a * b)
    case "/":
        print("Division of", a, "/", b, "=", a / b)
    case "//":
        print("Floor Division of", a, "//", b, "=", a // b)
    case "**":
        print("Exponentiation of", a, "**", b, "=", a ** b)
    case _:
        print("Invalid operation")


print("-------------------------------------")
print("Course Selection")
print("-------------------------------------")

choice = int(input("Enter choice (1/2/3): "))

match choice:
    case 1:
        print("Java course")
    case 2:
        print("Python course")
    case 3:
        print("Data Analytics course")
    case _:
        print("Invalid choice")

print("-------------------------------------")
print("Day of the Week")
print("-------------------------------------")
day = int(input("Enter day number (1-7): "))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid Day")

print("-------------------------------------")
print("Even or Odd")
print("-------------------------------------")
num = int(input("Enter a number: "))

match num % 2:
    case 0:
        print("Even Number")
    case 1:
        print("Odd Number")


print("-------------------------------------")
print("Traffic Signal")
print("-------------------------------------")
signal = input("Enter signal (Red/Yellow/Green): ").lower()

match signal:
    case "red":
        print("Stop")
    case "yellow":
        print("Get Ready")
    case "green":
        print("Go")
    case _:
        print("Invalid Signal")


print("-------------------------------------")
print("Vowel or Consonant")
print("-------------------------------------")
letter = input("Enter a single alphabet: ").lower()

match letter:
    case "a" | "e" | "i" | "o" | "u":
        print("Vowel")
    case _ if len(letter) == 1 and letter.isalpha():
        print("Consonant")
    case _:
        print("Invalid Input")


print("-------------------------------------")
print("Days in a Month")
print("-------------------------------------")
month = int(input("Enter month number (1-12): "))

match month:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print("31 Days")
    case 4 | 6 | 9 | 11:
        print("30 Days")
    case 2:
        print("28 or 29 Days")
    case _:
        print("Invalid Month")


print("-------------------------------------")
print("Food Menu")
print("-------------------------------------")

print("1. Pizza")
print("2. Burger")
print("3. Sandwich")
print("4. Pasta")

choice = int(input("Enter your choice (1-4): "))

match choice:
    case 1:
        print("You selected Pizza")
    case 2:
        print("You selected Burger")
    case 3:
        print("You selected Sandwich")
    case 4:
        print("You selected Pasta")
    case _:
        print("Invalid Choice")