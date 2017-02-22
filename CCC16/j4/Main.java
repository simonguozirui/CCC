import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {
	public static String arrivalTime(Scanner scanner){
		String inputTime = scanner.nextLine();
		int startHour = Integer.parseInt(inputTime.substring(0,2));
		int startMin = Integer.parseInt(inputTime.substring(3,5));
		//System.out.println(startHour);
		//System.out.println(startMin);
		int endHour = startHour + 2;
		int endMin = startMin + 0;

		if (startHour+2 > 7 && startHour+2 < 10){
			endHour += startHour+2 - 7;
			endMin += startMin - 0;
		}

		if (startHour+2 > 15 && startHour+2 < 19){
			endHour += startHour+2 - 15;
			endMin += startMin - 0;
		}
		//07:00 (7am) until 10:00 (10am) in the morning and 15:00 (3pm) until 19:00 (7pm) 


		String displayMin = "";
		if (endMin < 10) displayMin += "0" + Integer.toString(endMin);
		else if (endMin > 60){
			displayMin = Integer.toString(endMin - 60);
			endHour ++;
		} 
		else displayMin = Integer.toString(endMin);

		String displayHour = "";
		if (endHour < 10) displayHour += "0" + Integer.toString(endHour);
		else if (endHour > 23)displayHour = "0" +Integer.toString(endHour - 24);
		else displayHour = Integer.toString(endHour);



		return displayHour+":"+displayMin;

	}

	public static void main(String[] args) {
		Scanner myscan = new Scanner(System.in);
		System.out.println(arrivalTime(myscan)); 
	}

}
