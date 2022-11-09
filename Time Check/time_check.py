import time
D = time.strftime("%D")
T = time.strftime("%H:%M")
Darr0 = D.split("/")
Darr1 = [Darr0[1], Darr0[0], Darr0[2]]
current = str("/".join(Darr1)+" "+T)
Dcheck = input("Please enter date in the format DD/MM/YY: ")
Tcheck = input("Please enter time in the format HH:MM: ")
if Dcheck[1] == "/":
    print("fix")
    print(Dcheck)
    Dcheck = " "+Dcheck
    print(Dcheck)
check = Dcheck +" "+ Tcheck
while current != check:
    D = time.strftime("%D")
    T = time.strftime("%H:%M")
    Darr0 = D.split("/")
    Darr1 = [Darr0[1], Darr0[0], Darr0[2]]
    current = str("/".join(Darr1)+" "+T)
    print(current)
    print(check)
    time.sleep(1)
print("Uploading now")
