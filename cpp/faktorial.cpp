#include <iostream>

using namespace std;

// Fungsi Prototype
int faktorial(int n);

int main() {
	int n, hasil;

	cout << "Menghitung faktorial dari: ";
	cin >> n;

	hasil = faktorial(n);

	cout << " = " << hasil << endl;

	return 0;
}

int faktorial(int n) {
	/*
		Rumus: 
		f(n)! = n * (n-1)!

		Agar tidak infinity looping,
		Jika n <= 1, maka return n
	*/ 
	if (n <= 1) {
		cout << n;
		return n;
	} else {
		cout << n <<" * ";
		return n * faktorial(n - 1);
	}

}
