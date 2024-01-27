def calculate_bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    return bmi

weight = float(input("輸入你的體重（公斤）："))
height = float(input("輸入你的身高（公尺）："))

bmi_result = calculate_bmi(weight, height)

print("你的 BMI 是:", bmi_result)

if bmi_result < 18.5:
    print("過輕")
elif 18.5 <= bmi_result < 24:
    print("正常範圍")
elif 24 <= bmi_result < 27:
    print('過重')
else:
    print('肥胖')

