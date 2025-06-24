def is_valid_phone_number(phone:str):
    print( phone.isnumeric() and len(phone) == 9)

def main():
    phone = input("raqamni kiriting : ")
    is_valid_phone_number(phone)
    
main()
