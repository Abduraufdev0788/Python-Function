def calculate_bmi(weight: float, height: float) -> float:
    
    bmi = weight / (height ** 2)
    
    return bmi

def bmi_status(bmi: float) -> str:
    if bmi < 18.5:
        return "ozg'in vazn"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "semiz"
    else:
        return "ortiqcha vazn"

weight = float(input("og'irligingizni kiriting: "))
height = float(input("boyingizni kiriting: "))
bmi = calculate_bmi(weight, height)
print(bmi_status(bmi))
