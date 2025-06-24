brith_year = int(input("tug'ilgan yilingizni kiriting: "))
current_year = int(input("tug'ilgan yilingizni kiriting: "))

def age(brith_year,current_year):
    Age = current_year - brith_year
    return Age
yosh = age(brith_year,current_year)
if yosh >= 18 :
    print(f"sizning yoshingiz {yosh} siz balogatga yetgansiz")
else:
    print(f"Sizning yoshingiz {yosh} siz balogatga yetmagansiz")