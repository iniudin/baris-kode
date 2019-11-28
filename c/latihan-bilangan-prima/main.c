#include <stdio.h>

int main(void) {
	/*
	Cek bilangan Prima
	- Bilangan asli yang lebih dari 1
	- dan hanya jika habis di bagi oleh bilangan itu sendiri
	
	variable n, sebagai wadah inputan dari user dan count
	sebagai counter sebanyak berapa kali n dapat di bagi oleh bilangan i
	*/ 
	
	int n;
	int count = 0;

	printf("Masukkan angka positif: ");
	scanf("%i", &n);

	if (n > 1) {
		for (int i = 2; i < n; i++) {
			// Jika n % i == 0, dapat di bagi selain bilangan itu sendiri, maka n bukan bilangan prima.
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