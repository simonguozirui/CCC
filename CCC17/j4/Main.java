import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {
	public static int favouriteTimes(Scanner scanner){
		int count = 0;
		int d = scanner.nextInt();
		int h = 12;
		int m = 0;

		for (int i = 0; i <= d; i ++){
			if (i > 59){
				m = i%60;
				h += (i-i%60)/60;
			}else{
				m+=i;
			}

			if (h > 12){
				h = h%12;
			}
			if (h < 10 && m >= 10){
				if (h - (m-m%10)/10 == (m-m%10)/10 - m%10){
					//System.out.println(h+":"+m);
					count++;
				} 
			}else if (h >= 10 && m >= 10){
				if (1 - (h-10) == (h-10) - (m-m%10)/10){
					if (h-10 - (m-m%10)/10 == (m-m%10)/10 - m%10){
						//System.out.println(h+":"+m);
						count++;
					}
				} 
			}else if (h < 10 && m < 10){
				if (h - 0 == 0 - m){
					//System.out.println(h+":"+m);
					count++;
				} 
			}else if (h >= 10 && m < 10){
				if (1 - (h-10) == (h-10) - 0){
					if (h-10 - 0 == 0 - m){
						//System.out.println(h+":"+m);
						count++;
					}
				} 
			}
			h = 12;
			m = 0;
		}


		return count;
	}

	public static void main(String[] args) {
		Scanner myscan = new Scanner(System.in);
		System.out.println(favouriteTimes(myscan)); 
	}

}
