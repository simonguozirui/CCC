import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {
	public static boolean exactlyElectrical(Scanner scanner){
		int a = scanner.nextInt();
		int b = scanner.nextInt();
		int c = scanner.nextInt();
		int d = scanner.nextInt();
		int t = scanner.nextInt();
		int i = Math.abs(a - c) + Math.abs(b - d);
		if (Math.abs(t - i)%2 == 0){
			return true;
		}else{
			return false;
		}

		
	}

	public static void main(String[] args) {
		Scanner myscan = new Scanner(System.in);
		if (exactlyElectrical(myscan)){
			System.out.println("Y");
		}else{
			System.out.println("N");
		}
	}

}
