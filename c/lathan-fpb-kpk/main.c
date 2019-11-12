#include <stdio.h>

int hitung_FPB(int x, int y) {
	int sisa;
	while (1) {
		sisa = x % y;
		if (sisa == 0) {
			break;
		}
		x = y;
		y = sisa;
	}
	return y;
}

int hitung_KPK(int x, int y) {
	int perkali_x = 1;
	int perkali_y = 1;

	int p = x * perkali_x;
	int q = y * perkali_y;

	while (p != q) {
		while (p > q) {
			perkali_y += 1;
			q = y * perkali_y;
		}

		while (p < q) {
			perkali_x += 1;
			p = x * perkali_x;
		}
	}
	return p;
}

int main(){
	int bil1, bil2, hasil_fpb, hasil_kpk;

	printf("+++ Program Menentukan FPB & KPK +++\n");
	
	printf("Masukan bilangan 1: ");
	scanf("%i", &bil1);

	printf("Masukan bilangan 2: ");
	scanf("%i", &bil2);

	hasil_fpb = hitung_FPB(bil1, bil2);
	hasil_kpk = hitung_KPK(bil1, bil2);

	printf("FPB dari %i dan %i adalah %i\n", bil1, bil2, hasil_fpb);
	printf("KPK dari %i dan %i adalah %i\n", bil1, bil2, hasil_kpk);
	return 0;
}
