package homework;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Solution_1954_김채은 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	
	static int T;
	static int N;
	static int[][] board;
	static int[] dys = { 0, 1, 0, -1 };
	static int[] dxs = { 1, 0, -1, 0 };
	
	public static boolean inRange(int y, int x) {
		return 0 <= y && y < N && 0 <= x && x < N;
	}
	
	public static void main(String[] args) throws IOException {
		T = Integer.parseInt(br.readLine());
		
		for (int tc = 1; tc <= T; tc++) {
			N = Integer.parseInt(br.readLine());
			board = new int[N][N];
			
			int y = 0;
			int x = 0;
			int d = 0;
			
			int count = 1;
			board[y][x] = count;
			
			int ny, nx;
			
			while (count < N * N) {
				ny = y + dys[d];
				nx = x + dxs[d];
				
				if (inRange(ny, nx) && board[ny][nx] == 0) {
					board[ny][nx] = ++count;
					y = ny;
					x = nx;
				}else {
					d = (d + 1) % 4;
				}
			}
			
			System.out.println("#" + tc);
			for (int[] b: board) {
				for (int e : b) {
					System.out.print(e + " ");
				}
				System.out.println();
			}
		}
	}
}
