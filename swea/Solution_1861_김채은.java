package practice;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution_1861_김채은 {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	
	static int T;
	static int N;
	static int[][] board;
	
	static int[] dys = {1, 0, -1, 0};
	static int[] dxs = {0, 1, 0, -1};
	
	static int room;
	static int maxCount;
	
	public static boolean inRange(int y, int x) {
		return 0 <= y && y < N && 0 <= x && x < N;
	}
	
	public static void search(int start, int y, int x, int count) {
		for (int d = 0; d < 4; d++) {
			int ny = y + dys[d];
			int nx = x + dxs[d];
			
			if (inRange(ny, nx) && board[ny][nx] == board[y][x] + 1) {
				search(start, ny, nx, count + 1);
			}
		}
		
		if (maxCount < count || maxCount == count && room > start) {
			room = start;
			maxCount = count;
		}
	}
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		T = Integer.parseInt(br.readLine());
		
		for (int tc = 1; tc <= T; tc++) {
			N = Integer.parseInt(br.readLine());
			board = new int[N][N];
			for (int i = 0; i < N; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j < N; j++) {
					board[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			room = (int)1e9;
			maxCount = 0;
			
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {	
					search(board[i][j], i, j, 1);
				}
			}
			
			System.out.println("#" + tc + " " + room + " " + maxCount);
		}
	}

}
