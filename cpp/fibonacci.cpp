#include <iostream>

using namespace std;

long fib(long n);

long fib(long n) {
	// cout << "Fibonacci ke-" << n << endl;
	if ((n == 0) || (n == 1)) {
		return n;
	} else {
		return fib(n - 1) + fib(n - 2);
	}
}

int main() {
	long n, hasil;

	cout << "Nilai fibonacci ke :";
	cin >> n;

	hasil = fib(n);

	cout << "adalah " << hasil << endl;

	return 0;
}
