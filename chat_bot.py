def main():
    name = get_name()
    print(f"Привіт, {name}")


def get_name():
    print("Введіть ім'я")
    name = input()
    if name == "":
        print("Ведено порожнє значення")
        get_name()
    if has_digit(name):
        print("Цифри недопустимі в імені")
        get_name()

    return name


def has_digit(value):
    for char in value:
        if char.isdigit():
            return True
    return False


if __name__ == "__main__":
    main()
