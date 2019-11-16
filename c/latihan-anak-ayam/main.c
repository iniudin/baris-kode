#include <stdio.h>

int main() {
	int N, sisa_ayam;
	
	printf("Masukan jumlah anak ayam: ");
	// Input N, sebagai sebanyak ayam sebelum mati :(
	scanf("%i", &N);
	
	sisa_ayam = N;

	// Menggunakan While-loop
	
	while (N) {
		sisa_ayam--;
		if (N > 1){
			printf("Anak ayam turun %i, mati satu tinggal %i\n", N, sisa_ayam);	
		} else {
			printf("Anak ayam turun %i, mati satu tinggal Induknya\n", N);
		}
		N--;
	}

	return 0;
}