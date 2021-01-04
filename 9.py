a = int(input("Wpisz liczbę a: "))
b = int(input("Wpisz liczbę b: "))
while a != b:
        if a > b:
            a -= b
        else:
            b -= a
print("NWD a i b to: ", a)