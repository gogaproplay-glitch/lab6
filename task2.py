n = int(input("Введіть кількість слів N: "))

result = ""

for i in range(n):
    word = input("Введіть слово: ")
    result = result + " ".join(word) + ","

print(result[:-1])
