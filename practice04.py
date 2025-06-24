def get_grade(score):
    if 90<= score <=100:
        print(f"sizning darajangiz A ---{score}")
    elif 80 <= score <90 :
        print(f"sizning darajangiz B ----{score}")
    elif 70 <= score <80 :
        print(f"sizning darajangiz C ----{score}")
    elif 60 <= score <70 :
        print(f"sizning darajangiz D ----{score}")
    elif 0 <= score <60 :
        print(f"sizning darajangiz F ----{score}")
    else:
        print("bunday ball mavjud emas")
def main():
    score = int(input("ballni kiriting: "))
    get_grade(score)

main()