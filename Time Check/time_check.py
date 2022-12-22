import time
D = time.strftime("%D")
T = time.strftime("%H:%M")
Darr0 = D.split("/")
Darr1 = [Darr0[1], Darr0[0], Darr0[2]]
current = str("/".join(Darr1)+" "+T)
Dcheck = input("Please enter date in the format DD/MM/YY: ")
Tcheck = input("Please enter time in the format HH:MM (24-hour time): ")
check = Dcheck +" "+ Tcheck
if current != check:
    while int(time.strftime("%S")) != 0:
        time.sleep(1)
if current != check:
    while int(time.strftime("%M"))%5 != 0 :
        time.sleep(60)
while current != check:
    D = time.strftime("%D")
    T = time.strftime("%H:%M")
    Darr0 = D.split("/")
    Darr1 = [Darr0[1], Darr0[0], Darr0[2]]
    current = str("/".join(Darr1)+" "+T)
    if current == check: break
    time.sleep(300)
print("Uploading now")
