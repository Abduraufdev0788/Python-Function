def deposit(balance, amount):
    if amount > 0:
        balance += amount
        print(f"{amount} soʻm depozit qilindi.")
    else:
        print("Depozit miqdori manfiy bo‘lmasligi kerak.")
    return balance

def withdraw(balance, amount):
    if amount <= balance:
        balance -= amount
        print(f"{amount} soʻm yechildi.")
    else:
        print("Yetarli mablagʻ mavjud emas.")
    return balance

def check_balance(balance):
    print(f"Joriy balans: {balance} soʻm")
    return balance


balance = 0

while True:
    print(" Dasturimizga xush kelibsiz!")
    print("1) Deposit qilish")
    print("2) Pul yechish (Withdraw)")
    print("3) Balansni ko‘rish")
    print("0) Chiqish")
    
    choise = int(input("Tanlov raqamingizni kiriting: "))
    
    if choise == 1:
        amount = int(input("Qo‘shmoqchi bo‘lgan summani kiriting: "))
        balance = deposit(balance, amount)
        print(balance) 
    elif choise == 2:
        amount = int(input("Yechmoqchi bo‘lgan summani kiriting: "))
        balance = withdraw(balance, amount)
        print(balance)
    elif choise == 3:
        check_balance(balance)
        print(balance)
    elif choise == 0:
        print("Dasturdan chiqildi.")
        break
    else:
        print(" Noto‘g‘ri tanlov. Iltimos, 0–3 oralig‘idagi raqam kiriting.")
