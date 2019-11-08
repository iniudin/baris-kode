#include <stdio.h>

int nilai_mutlak(int angka) {
	if (angka < 0) {
		angka = angka * - 1;
	}
	return angka;
}

int manhattan(int x1, int x2, int y1, int y2) {
	int hasil;
	hasil = nilai_mutlak(x1 - x2) + nilai_mutlak(y1 - y2);
	return hasil;
}

int main() {
	int x1, x2, y1, y2, jarak;
	printf("==== Program Menghitung Jarak Manhattan ====\n");

	printf("Masukan absis x1: ");
	scanf("%i", &x1);

	printf("Masukan ordinat y1: ");
	scanf("%i", &y1);

	printf("Masukan absis x2: ");
	scanf("%i", &x2);

	printf("Masukan ordinat y2: ");
	scanf("%i", &y2);

	jarak = manhattan(x1, x2, y1, y2);

	printf("Jarak Manhattan adalah %i satuan\n", jarak);

	return 0;
}
