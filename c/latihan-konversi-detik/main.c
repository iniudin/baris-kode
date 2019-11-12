#include <stdio.h>

struct DivMod {
	int x;
	int y;
};

struct DivMod divmod(int x, int y) {
	struct DivMod ret;
	ret.x = x / y;
	ret.y = x % y;
	return ret;
}

void konversi_waktu(int input) {
	struct DivMod menit_detik, jam_menit, hari_jam, minggu_hari, bulan_minggu, tahun_bulan;
	int detik, menit, jam, hari, minggu, bulan, tahun;	
	
	menit_detik = divmod(input, 60);
	detik = menit_detik.y;
	menit = menit_detik.x;

	jam_menit = divmod(menit, 60);
	jam = jam_menit.x;
	menit = jam_menit.y;

	hari_jam = divmod(jam, 24);
	hari = hari_jam.x;
	jam = hari_jam.y;

	minggu_hari = divmod(hari, 7);
	minggu = minggu_hari.x;
	hari = minggu_hari.y;

	bulan_minggu = divmod(minggu, 4);
	bulan = bulan_minggu.x;
	minggu = bulan_minggu.y;

	tahun_bulan = divmod(bulan, 12);
	tahun = tahun_bulan.x;
	bulan = tahun_bulan.y;

	printf("Hasil:\n");

	if (tahun != 0) {
		printf("%d tahun ", tahun);
	}

	if (bulan != 0) {
		printf("%d bulan ", bulan);
	}

	if (minggu != 0) {
		printf("%d minggu ", minggu);
	}

	if (hari != 0) {
		printf("%d hari ", hari);
	}

	if (jam != 0) {
		printf("%d jam ", jam);
	}

	if (menit != 0) {
		printf("%d menit ", menit);
	}

	if (detik != 0) {
		printf("%d detik\n", detik);
	}
}

int main() {
	int input;
	printf("[=== Program Konversi Waktu [Detik ===]\n");
	printf("Masukan detik: ");
	scanf("%d", &input);
	konversi_waktu(input);
	printf("\n[=== Selesai ===]\n");
	return 0;
}
