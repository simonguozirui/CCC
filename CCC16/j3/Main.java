import java.util.*;
import java.io.*;
import java.lang.*;


public class Main {
	public static int hiddenPalindrome(Scanner scanner){
		int max = 0;
		String word = scanner.nextLine();
		for (int i = 0; i < word.length(); i ++){
			for (int j = 1; i+j <= word.length(); j ++){
				StringBuilder currentString = new StringBuilder(word.substring(i,i+j));
				if (currentString.reverse().toString().equals(word.substring(i,i+j))){
					//System.out.println(currentString.reverse().toString());
					//System.out.println(currentString.toString());
					//System.out.println(j);
					if (j > max) max = j;
				}
			}
		}

		return max;

	}

	public static void main(String[] args) {
		Scanner myscan = new Scanner(System.in);
		System.out.println(hiddenPalindrome(myscan)); 
	}

}
