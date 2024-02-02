package practice;

import java.io.*;
import java.util.*;

public class Solution_1210_김채은 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	
	static int TC = 10;
	static int N = 100;
	
	static int EMPTY = 0;
	static int LADDER = 1;
	static int GOAL = 2;
	
	public static boolean inRange(int y, int x) {
		return 0 <= y && y < N && 0 <= x && x < N;
	}
	
	public static void main(String[] args) throws IOException{
		for (int tc = 1; tc < TC; tc++) {

			int T = Integer.parseInt(br.readLine());
			
			int[][] board = new int[N][N];
			
			for (int i = 0; i < N; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j < N; j++) {
					board[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			
			// 목표 지점 찾기 (출발지로 설정)
			int y = N-1;
			int x = 0;
			for (int start = 0; start < N; start++) {
				if (board[N-1][start] == GOAL) {
					x = start;
				}
			}
			
			int[] dys = {0, 0, -1};
			int[] dxs = {1, -1, 0};
			
			boolean[][] visited = new boolean[N][N];
			visited[y][x] = true;
			
			while (y != 0) {
				
				for (int d = 0; d < 3; d++) {
					int ny = y + dys[d];
					int nx = x + dxs[d];
					
					// 사다리이며 방문하지 않은 경우 그곳으로 탐색
					// 방문지 하나라도 찾으면 그쪽으로만 이동
					if (inRange(ny, nx) && board[ny][nx] == LADDER && !visited[ny][nx]) {
						y = ny;
						x = nx;
						visited[y][x] = true;
						break;
					}
				}
			}
			
			System.out.println("#" + T + " " + x);
		}
	}
	
}
