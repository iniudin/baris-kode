#include <iostream>

using namespace std;

int main() {
	int N, sisa_ayam;
	
	cout << "Masukan jumlah anak ayam: ";
	cin >> N;	

	sisa_ayam = N;

	// Menggunakan While-loop
	
	while (N) {
		sisa_ayam--;
		if (N > 1){
			cout << "Anak ayam turun " << N << ", mati satu tinggal " << sisa_ayam << endl;
		} else {
			cout << "Anak ayam turun " << N << ", mati satu tinggal Induknya"<< endl;
		}
		N--;
	}

	return 0;
}