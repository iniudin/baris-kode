# Fungsi untuk mencari nilai fib ke N
def fibbonaci(n):
    if n <= 1:
        return n
    else:
        return fibbonaci(n - 1) + fibbonaci(n - 2)


n = int(input("Bilangan Real: "))
print(f"nilai fib ke {n} adalah {fibbonaci(n)}")
