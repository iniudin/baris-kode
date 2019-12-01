import java.util.*;

public class Main {
	public static void main(String[] args) {
		int n, f_n, f_n1, f_n2;
		
		Scanner inputUser = new Scanner(System.in);

		System.out.print("Nilai Fibonacci ke-: ");
		n = inputUser.nextInt();

		f_n2 = 0;
		f_n1 = 1;
		f_n = 1;
		for (int i = 1; i < n; i++) {
			f_n = f_n1 + f_n2;
			f_n2 = f_n1;
			f_n1 = f_n;
			System.out.println("Fib ke " + i + " adalah " + f_n);
		}
	}
}