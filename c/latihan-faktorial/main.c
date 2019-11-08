#include <stdio.h>

int faktorial(int n);

int main() {
	int n, hasil;

	printf("Nilai faktorial dari: ");
	scanf("%i", &n);

	hasil = faktorial(n);

	printf("adalah %d\n", hasil);

	return 0;
}

int faktorial(int n) {
	if (n <= 1) {
		return n;
	} else {
		return n * faktorial(n - 1);
	}
}
