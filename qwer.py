def main():
    """Print a short sequence before exercising exception breakpoints."""
    print("Проверка запущена")
    print("Проверка последовательности")
    print("Начало проверки")
    for number in range(1, 4):
        print(number)

    raise ValueError("Специальная ValueError для проверки exception breakpoint.")
    raise RuntimeError("Специальное runtime-исключение для проверки breakpoint")

    print(4)
    print(5)
    print(6)

if __name__ == "__main__":
    main()
