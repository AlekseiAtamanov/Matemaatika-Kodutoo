import random 
x=int(input("Сколько примеров хотите? \n"))
z=int(input("Какой сложности хотите примеры? (Значение от 1-легко, 2-средне, 3-сложно) "))
print("Учитывайте, что в случае если ответ не целое число, то оно округляется до двух знаков до запятой")
y=0
if z==1:
    for i in range(1,x+1):
        a=random.randint(1,15)
        b=random.randint(1,15)
        ans1=float(a+b)
        ans2=float(input(f"Введите ответ на этот пример {a}+{b} \n"))
        if 2*ans1==ans1+ans2:
            y=y+1
elif z==2:    
    for i in range(1,x+1):
        a=random.randint(1,15)
        b=random.randint(1,15)
        c=random.randint(1,15)
        var=random.randint(1,3)
        if var==1:
            ans1=float(a+b-c)
            ans2=float(input(f"Введите ответ на этот пример {a}+{b}-{c} \n"))
        elif var==2:
            ans1=float(a+b+c)-(b+c)
            ans2=float(input(f"Введите ответ на этот пример {a}+{b}-{c}-({b}+{c}) \n"))
        elif var==3:
            ans1=float(a+b)*c
            ans2=float(input(f"Введите ответ на этот пример {a}+{b}*{c} \n"))
        if 2*ans1==ans1+ans2:
            y=y+1
elif z==3:
    for i in range(1,x+1):
        a=random.randint(1,15)
        b=random.randint(1,15)
        c=random.randint(1,15)
        d=random.randint(1,15)
        var=random.randint(1,3)
        if var==1:
            ans1=float(a+d-c)*(b+c)/a
            ans1=round(ans1,2)
            ans2=float(input(f"Введите ответ на этот пример ({a}+{d}-{c})*({b}+{c})/{a} \n"))
        elif var==2:
            ans1=float(a/b*c)-(d+c)+(b**2)
            ans1=round(ans1,2)
            ans2=float(input(f"Введите ответ на этот пример ({a}/{b}*{c})-({d}+{c})+({b}°2) \n"))
        elif var==3:
            ans1=float(b*c*a)/d+(c**2)+d
            ans1=round(ans1,2)
            ans2=float(input(f"Введите ответ на этот пример ({b}*{c}*{a})/{d}+({c}°2)+{d} \n"))
        if 2*ans1==ans1+ans2:
            y=y+1
else:
    print("Error value")
print(f"Количество правильных ответов на примеры - {y}")
hind=(y/x)*100
if hind <=59:
    print("Оценка 2")
elif hind <=74:
    print("Оценка 3")
elif hind <=90:
    print("Оценка 4")
else:
    print("Оценка 5")
