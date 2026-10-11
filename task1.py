s = input("Введіть рядок: ")

letters = 0
digits = 0

for ch in s:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1

print("Кількість літер:", letters)
print("Кількість цифр:", digits)
