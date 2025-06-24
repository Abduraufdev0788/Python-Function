def c_to_F(celius):
    calc = celius * 9/5 + 32
    return calc

def f_to_c(fahrenheit):
    calc = (fahrenheit - 32) * 9/5
    return calc


print("1)Celsius → Fahrenheit")
print("2)Fahrenheit → Celsius")
print("quyidagilardan birini tanlang")
choise = int(input("tanlangan raqamni kiriting: "))
if choise == 1 or choise == 2:
    if choise == 1:
        celius = int(input("haroratni kiriting: "))
        print(c_to_F(celius))
    elif choise == 2 :
        fahrenheit = int(input("haroratni kiriting:"))
        print(f_to_c(fahrenheit))
        


