# Write your program here
wage=round(float(input("Tell me the hourly wage")),2)
reghrs=round(float(input("Tell me the regular hours")),2)
othrs=round(float(input("Tell me the overtime hours")),2)
print(f'The weekly pay is ${format(wage*(reghrs+othrs*1.5),".2f")}')