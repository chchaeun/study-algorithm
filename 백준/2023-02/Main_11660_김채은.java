package practice;

import java.io.*;
import java.util.*;


public class Main_11660_김채은 {	
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	static StringTokenizer st;
	
	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		int[][] board = new int[N + 1][N + 1];
		
		for (int i = 1; i <= N; i++) {
			st = new StringTokenizer(br.readLine());
			
			// 누적합 초기화
			for (int j = 1; j <= N; j++) {
				board[i][j] = board[i-1][j] + board[i][j-1] - board[i-1][j-1] + Integer.parseInt(st.nextToken());
			}
		}
		
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int y1 = Integer.parseInt(st.nextToken());
			int x1 = Integer.parseInt(st.nextToken());
			int y2 = Integer.parseInt(st.nextToken());
			int x2 = Integer.parseInt(st.nextToken());
			
			// 누적합을 통해 네모 범위 빼주기
			bw.write(String.valueOf(board[y2][x2] - board[y2][x1-1] - board[y1-1][x2] + board[y1-1][x1-1]));
			bw.write("\n");
		}
		
		bw.flush();
		bw.close();
	}
}
