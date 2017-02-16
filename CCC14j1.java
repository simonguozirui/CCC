//https://dmoj.ca/problem/ccc14j1
import java.util.Scanner;

public class CCC14j1{

	public static void main(String[] args) {
		Scanner input = new Scanner (System.in);
		int a = input.nextInt();
		int b = input.nextInt();
		int c = input.nextInt();
		if ((a == 60 && b == 60) && c == 60) System.out.println("Equilateral");
		else if (a+b+c == 180){
			if (a == b || b == c || a == c) System.out.println("Isosceles");
			else System.out.println("Scalene");
		}
		else System.out.println("Error");

	}
}