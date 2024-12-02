def check_age():
    try:
        age = int(input("Введіть ваш вік: "))
        assert age >= 18, "Вам має бути 18 років або більше"
        print("Ви можете використовувати цей сервіс")
    except AssertionError as e:
        print(e)
    except ValueError:
        print("Помилка! Переконайтесь що ви ввели рік числом.")

check_age()
