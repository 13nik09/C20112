try:
    numberr = input("Введіть число: ")
    number = int(numberr)
    print(f"Ви ввели число: {number}")
except ValueError:
    print("Помилка: введені дані не є цілим числом.")
