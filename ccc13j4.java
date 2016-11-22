//https://dmoj.ca/problem/ccc13j4
import java.util.Scanner;
import java.util.Arrays;

public class ccc13j4{

	public static void main(String[] args) {
		Scanner input = new Scanner (System.in);
		int maxmin = input.nextInt();
		int numtask = input.nextInt();
		int [] time = new int [numtask];
		for (int i = 0; i < numtask; i++){
			time[i] = input.nextInt();
		}
		Arrays.sort(time);
		int maxtask = 0;
		int index = 0;
		int totaltime = 0;
		while(totaltime + time[index] <= maxmin){
			totaltime = totaltime + time[index];
			index ++;
			maxtask++;
		}
		System.out.println(maxtask);

	}
}