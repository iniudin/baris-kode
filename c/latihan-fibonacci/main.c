#include <stdio.h>

int fibonacci(int n);

int main() {
	int n, hasil;

	printf("Fibonacci ke N: ");
	scanf("%d", &n);

	hasil = fibonacci(n);

	printf("adalah %d\n", hasil);

	return 0;
}

int fibonacci(int n) {
	if ((n == 0) || (n == 1)) {
		return n;
	} else {
		return fibonacci(n - 1) + fibonacci(n - 2);
	}
}
