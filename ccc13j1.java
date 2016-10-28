import java.util.Scanner;

public class ccc13j1 {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		System.out.println("Enter youngest:");
		int y = input.nextInt();
		//Integer y = Integer.valueOf(input.next())
		System.out.println("Enter middle:");
		//Integer m = Integer.valueOf(input.next())
		int m = input.nextInt();
		//m-y+m = 2*m - y
		System.out.println("Oldest sibling is " + (2*m-y) + " year old");

	}
}

