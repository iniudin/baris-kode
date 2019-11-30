#include <stdio.h>
#include <stdbool.h>

int main(void) {
	int range_down, range_up;
	bool is_Prime;
	is_Prime = true;

	printf("Masukkan range awal: ");
	scanf("%i", &range_down);
	printf("Masukkan range akhir: ");
	scanf("%i", &range_up);

	printf("Memproses...\n");
	if (range_down == 1) {
		range_down++;
	}

	// Iterasi ini untuk bilangan yang akan di cek
	for (int i = range_down; i <= range_up; i++) {
		// Iterasi ini untuk mengecek apakah nilai i bilangan prima atau tidak
		for (int j = 2; j < i; j++) {
			if (i % j == 0) {
				is_Prime = false;
				break;
			}
		}
		if (is_Prime) {
			printf("%i\n", i);
		}else {
			is_Prime = true;
		}
	}
}