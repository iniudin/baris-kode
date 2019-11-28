#include <stdio.h>

int main() {
	int n;
	int count = 0;

	printf("Masukkan angka positif: ");
	scanf("%i", &n);

	if (n > 1) {
		for (int i = 2; i < n; i++) {
			if (n % i == 0) {
				count++;
				break;
			}
		}
		if (count == 0) {
			printf("%i, adalah bilangan prima\n", n);
		} else {
			printf("%i, adalah bukan bilangan prima\n", n);
		}
	} else {
		printf("%i, adalah bukan bilangan prima\n", n);
	}
}