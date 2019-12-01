import java.util.*;

public class Main {
	public static void main(String[] args) {
		// Kotak
		for (int i = 0; i < 5; i++) {
			for (int j = 0; j < 5; j++){
				System.out.print("* ");
			}
			System.out.print("\n");
		}

		System.out.print("\n");
		
		// Segitiga
		for (int i = 0; i < 5; i++) {
			for (int j = 0; j < 5; j++){
				System.out.print("* ");
				if (i == j) {
					break;
				}
			}
			System.out.print("\n");
		}

		System.out.print("\n");

		for (int i = 0; i < 5; i++) {
			for (int j = 0; j < 5; j++){
				System.out.print("* ");
				if (i + j == 4) {
					break;
				}
			}
			System.out.print("\n");
		}

		System.out.print("\n");
		// Setengah wajik

		for (int i = 0; i < 9; i++) {
			for (int j = 0; j < 9; j++){
				System.out.print("* ");
				if (i == j) {
					break;
				} else if (i + j == 8) {
					break;
				}
			}
			System.out.print("\n");
		}

		System.out.print("\n");
		// wajik

		for (int i = 0; i < 15; i++) {
			for (int j = 0; j < 15; j++){
				if (i + j <= 13) {
					System.out.print(" ");
				}else if (i <= j) {
					// System.out.print("["+ j +","+ i + "] ");
					System.out.print("* ");
				}else {
					System.out.print(" ");
				}
			}
			System.out.print("\n");
		}
	}
}