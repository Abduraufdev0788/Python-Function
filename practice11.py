def calculate_tax(salary: float) -> float:
    if salary > 5_000_000:
        tax_rate = 0.20
    else:
        tax_rate = 0.13  
    return salary * tax_rate


def calculate_net_salary(salary: float) -> float:
    tax = calculate_tax(salary)
    return salary - tax



maosh = float(input("Maoshingizni kiriting: "))
soliq = calculate_tax(maosh)
sof_maosh = calculate_net_salary(maosh)

print(f"Soliq: {soliq:.2f} soʻm")
print(f"Sof maosh: {sof_maosh:.2f} soʻm")
