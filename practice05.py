def check_guess(secret,guess):
    if secret == guess :
        print("tog'ri javob")
    else:
        print("Notogri javob")

def main():
    guess = int(input("sonni kiriting"))
    secret = 123
    if 100 <= guess <= 999 :
        check_guess(secret,guess)
    else:
        print("3 xonali son kiriting ")
        
main()