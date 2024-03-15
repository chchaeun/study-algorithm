package homework;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution_2001_김채은 {

	private static int N, M;
	private static int[][] board;
	public static int calculate(int y, int x) {
		int sum = 0;
		for (int i = 0; i < M; i++) {
			for (int j = 0; j < M; j++) {
				sum += board[y+i][x+j];
			}
		}
		
		return sum;
	}
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int T = Integer.parseInt(br.readLine());
		
		for (int tc = 1; tc <= T; tc++) {
			st = new StringTokenizer(br.readLine());
			
			N = Integer.parseInt(st.nextToken());
			M = Integer.parseInt(st.nextToken());
			
			board = new int[N][N];
			
			for (int i = 0; i < N; i++) {
				st = new StringTokenizer(br.readLine());
				
				for (int j = 0; j < N; j++) {
					board[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			
			int answer = 0;
					
			for (int y = 0; y < N - M + 1; y++) {
				for (int x = 0; x < N - M + 1; x++) {
					int result = calculate(y, x);
					
					if (answer < result) {
						answer = result;
					}
				}
			}
			
			System.out.println("#" + tc + " " + answer);
		}
	}

}
