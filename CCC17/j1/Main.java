import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {
	public static int quadrantSelection(Scanner scanner){
		int quadrant = 0;
		int x = Integer.parseInt(scanner.nextLine());
		int y = Integer.parseInt(scanner.nextLine());
		if (x > 0 && y > 0){
			quadrant = 1;
		}else if (x < 0 && y > 0){
			quadrant = 2;
		}else if (x < 0 && y < 0){
			quadrant = 3;
		}else if (x > 0 && y < 0){
			quadrant = 4;
		}
		return quadrant;
	}

	public static void main(String[] args) {
		Scanner myscan = new Scanner(System.in);
		System.out.println(quadrantSelection(myscan)); 
	}

}
