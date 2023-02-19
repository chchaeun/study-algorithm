package practice;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solution_2805_김채은 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

	static int T;
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		T = Integer.parseInt(br.readLine());
		
		for (int tc = 1; tc <= T; tc++) {
			int answer = 0;
			int N = Integer.parseInt(br.readLine());
			String[] board = new String[N];
			
			for (int i = 0; i < N; i++) {
				board[i] = br.readLine();
			}

			int HALF = (int) Math.ceil(N/2);
			
			// 거리가 HALF 이하인 것들 다 더해주기
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					if (Math.abs(HALF - i) + Math.abs(HALF - j) <= HALF) {
						answer += (int) (board[i].charAt(j) - '0');
					}
				}
			}
			
			System.out.println("#" + tc + " " + answer);
		}
	}
}
