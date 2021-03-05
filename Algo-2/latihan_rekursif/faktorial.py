# faktorial(n) adalah fungsi rekursif untuk mencari nilai faktorial dari n
def faktorial(n):
    print(n, end="!")
    if n <= 1:
        print()
        return n
    else:
        return n * faktorial(n - 1)


n = int(input("Bilangan Real: "))
print(f"faktorial dari {n} adalah {faktorial(n)}")
