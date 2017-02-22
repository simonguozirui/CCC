import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {
	public static int shiftySum(Scanner scanner){
		int n = Integer.parseInt(scanner.nextLine());
		int k = Integer.parseInt(scanner.nextLine());
		int sum = 0;
		int static10 = 1;
		for (int i = 0; i <= k; i++){

			for (int j = 0; j < i; j ++){
				static10 = static10*10;
			}

			sum+= n*static10;
			static10 = 1;
		}

		return sum;
	}

	public static void main(String[] args) {
		Scanner myscan = new Scanner(System.in);
		System.out.println(shiftySum(myscan));
	}

}
