def main():
    print(1)
    print(2)
    print(3)

    raise ValueError("Специальная ValueError для проверки exception breakpoint")
    raise RuntimeError("Специальное runtime-исключение для проверки breakpoint")

    print(4)
    print(5)
    print(6)

if __name__ == "__main__":
    main()