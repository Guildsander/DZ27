# # 0 -> 0 днів, 00:00:00
# # 224930 -> 2 дні, 14:28:50
# # 466289 -> 5 днів, 09:31:29
# # 950400 -> 11 днів, 00:00:00
# # 1209600 -> 14 днів, 00:00:00
# # 1900800 - > 22 дні, 00:00:00
# # 8639999 -> 99 днів, 23:59:59
# # 22493 -> 0 днів, 06:14:53
# # 7948799 -> 91 день, 23:59:59

seconds_input = int(input("Введіть кількість секунд: "))

days = seconds_input // (24 * 60 * 60)
seconds_input %= 24 * 60 * 60
hours = seconds_input // (60 * 60)
seconds_input %= 60 * 60
minutes = seconds_input // 60
seconds = seconds_input % 60

if days % 10 == 1 and days % 100 != 11:
    days_text = "день"
elif 2 <= days % 10 <= 4 and (days % 100 < 10 or days % 100 >= 20):
    days_text = "дня"
else:
    days_text = "дней"
formatted_time = f"{days} {days_text}, {hours:02}:{minutes:02}:{seconds:02}"

print(formatted_time)
