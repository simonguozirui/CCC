import java.util.*;
import java.io.*;

public class Main {
	public static boolean magicSquares(Scanner scanner){
		boolean magic = true;
		int count = 0;
		int s1 = 0;
		int s2 = 0;
		int static_1 = 0;
		int static_2 = 0;
		int[][] input = new int[4][4];
		while (scanner.hasNext() && count < 16){
			for (int i = 0; i < 4; i ++){
				for (int j = 0; j < 4; j ++){
					input [i][j] = scanner.nextInt();
					count ++;
				}
			}
		}

		s1 = input[0][0] + input[0][1] + input[0][2] + + input[0][3];
		
		for (int i = 1; i < 4; i ++){
			static_1 = 0;
			for (int j = 0; j < 4; j ++){
				static_1 += input[i][j];
			}
			if (static_1 != s1){
				magic = false;
			}
		}

		s2 = input[0][0] + input[1][0] + input[2][0] + + input[3][0];

		for (int j = 1; j < 4; j ++){
			static_2 = 0;
			for (int i = 0; i < 4; i ++){
				static_2 += input[i][j];
			}
			if (static_2 != s2){
				magic = false;
			}
		}

		if (s1!=s2){
			magic = false;
		}

		return magic;
	}

	public static void main(String[] args) {
		Scanner myscan = new Scanner(System.in);
		if (magicSquares(myscan)){
			System.out.println("magic");
		}else{
			System.out.println("not magic");
		}
	}

}
