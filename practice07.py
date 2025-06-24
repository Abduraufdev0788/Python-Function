def ask_question(question: str, correct_answer: str):
    print("savol : ",question)
    user_answer = input("javobingizni kiriting: ")
    user_answer = user_answer.lower().strip()
    correct_answer = correct_answer.lower().strip()
    check_answer(user_answer,correct_answer)
    


def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer :
        print("siz togri javob berdingiz")
    else:
        print("sizning javobingiz xato")

ask_question("Uzb ni poytqaxti","Toshkent")
       