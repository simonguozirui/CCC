
import java.util.Scanner;

public class ccc11j4{
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		boolean [][] wellplan = new boolean[200][401];//row, col
		wellplan[4][199] = true;
		wellplan[5][199] = true;
		wellplan[6][199] = true;
		wellplan[0][200] = true;
		wellplan[0][200] = true;
		wellplan[6][200] = true;
		wellplan[2][201] = true;
		wellplan[6][201] = true;
		wellplan[2][202] = true;
		wellplan[6][202] = true;
		wellplan[2][203] = true;
		wellplan[3][203] = true;
		wellplan[4][203] = true;
		wellplan[5][203] = true;
		wellplan[4][204] = true;
		wellplan[6][204] = true;
		wellplan[2][205] = true;
		wellplan[3][205] = true;
		wellplan[4][205] = true;
		wellplan[6][205] = true;
		wellplan[2][206] = true;
		wellplan[6][206] = true;
		wellplan[2][207] = true;
		wellplan[3][207] = true;
		wellplan[4][207] = true;
		wellplan[5][207] = true;
		wellplan[6][207] = true;

		String direction = input.next();
		boolean move = true;
		int row = 4;
		int col = 199;
		while (!direction.equals("q")&&move){
			int dx = 0;
			int dy = 0;
			if (direction.equals("l")) dx = -1;
			else if (direction.equals("r")) dx = 1;
			else if (direction.equals("u")) dy = 1;
			else if (direction.equals("d")) dy = -1;
			int distance = input.nextInt();
			while (distance > 0){
				row = row + dx;
				col = col + dy;
				if (wellplan[row][col]) move = false;
				else wellplan[row][col] = true;
				distance = distance -1;
				
				}
				if(move)System.out.println((col-200) +" "+(row+1)*-1+" safe");
				else{
					System.out.println((col-200) +" "+(row+1)*-1+" Danger");			

			}
			direction = input.next();


		}
	}
}