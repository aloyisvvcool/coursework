import time

date_str = input("Enter the date (DD/MM/YYYY): ")
time_str = input("Enter the time (HH:MM): ")

date_time_str = date_str + " " + time_str
end_time = time.strptime(date_time_str, "%d/%m/%Y %H:%M")

while True:
    current_time = time.localtime()
    if current_time >= end_time:
        print("Yes")
        break
    time.sleep(60)
