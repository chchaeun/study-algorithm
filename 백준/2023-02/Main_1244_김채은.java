package homework;

import java.io.*;
import java.util.*;

public class Main_1244_김채은 {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	
	static int MAN = 1;
	static int WOMAN = 2;
	
	static int ON = 1;
	static int OFF = 0;
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		int N = Integer.parseInt(br.readLine());
		boolean[] switches = new boolean[N + 1];

		st = new StringTokenizer(br.readLine());
		for (int i = 1; i <= N; i++) {
			switches[i] = Integer.parseInt(st.nextToken()) == ON ? true : false;
		}
		
		int S = Integer.parseInt(br.readLine());
		int student, number;
		
		for (int i = 0; i < S; i++) {
			st = new StringTokenizer(br.readLine());
			
			student = Integer.parseInt(st.nextToken());
			number = Integer.parseInt(st.nextToken());
			
			if (student == MAN) {
				for (int j = number; j <= N; j++) {
					if (j % number == 0) {
						switches[j] = !switches[j];
					}
				}
			} else if (student == WOMAN) {
				switches[number] = !switches[number];
				int left = number - 1;
				int right = number + 1;
				
				while (1 <= left && right <= N) {
					if (switches[left] == switches[right]) {
						switches[left] = !switches[left];						
						switches[right] = !switches[right];
					} else {
						break;
					}
					
					left--;
					right++;
				}
			}
		}
		
		for (int i = 1; i <= N; i++) {
			System.out.print(switches[i] ? ON : OFF);
			System.out.print(" ");
			
			if (i % 20 == 0) {	
				System.out.println();
			}
		}
	}
}
