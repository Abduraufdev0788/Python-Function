a = float(input("Birinchi sonni kiriting: "))
b = float(input("Ikkinchi sonni kiriting: "))
amal = input("Amalni tanlang (+, -, *, /): ")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Nolga bo‘lish mumkin emas!"
if amal == "+":
    print("Natija:", add(a, b))
elif amal == "-":
    print("Natija:", subtract(a, b))
elif amal == "*":
    print("Natija:", multiply(a, b))
elif amal == "/":
    print("Natija:", divide(a, b))
else:
    print("Xatolik: Noto‘g‘ri amal kiritildi.")


