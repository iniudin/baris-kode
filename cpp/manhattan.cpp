#include <iostream>

using namespace std;

int nilai_mutlak(int angka) {
	if (angka < 0) {
		angka = angka * -1;
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

	cout << "Masukan absis x1: ";
	cin >> x1;

	cout << "Masukan ordinat y1: ";
	cin >> y1;

	cout << "Masukan absis x2: ";
	cin >> x2;

	cout << "Masukan ordinat y2: ";
	cin >> y2;

	jarak = manhattan(x1, x2, y1, y2);

	cout << "Jarak Manhattan adalah ";
	cout << jarak << " satuan" << endl;

	return 0;
}
