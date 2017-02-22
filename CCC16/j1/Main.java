import java.util.*;
import java.io.*;

public class Main {
	public static int tournamentSelection(Scanner scanner){
		int w = 0;
		int l = 0;
		int c = 0;
		while (scanner.hasNext()){
			if (scanner.next().equals("W")){
				w++;
			}
		}
		if (w >= 5){
			c = 1;
		}else if(w >= 3){
			c = 2;
		}else if (w >= 1){
			c = 3;
		}else if (w == 0){
			c = -1;
		}
		return c;

	}

	public static void main(String[] args) {
		Scanner myscan = new Scanner(System.in);
		System.out.println(tournamentSelection(myscan)); 
	}

}
