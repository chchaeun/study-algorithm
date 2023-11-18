package practice;

import java.io.*;
import java.util.*;

public class Solution_5215_김채은 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	
	static int T;
	static int N, L;
	static int[][] food;
	
	static int answer;
	
	public static void nCr(Stack<Integer> arr, int score, int kcal) {
		if (answer < score) {
			answer = score;
		}
		
		if (arr.size() == N) {
			return;
		}
		
		for (int i = 0; i < N; i++) {
			if (arr.size() > 0 && arr.peek() >= i) {
				continue;
			}
			
			if (kcal + food[i][1] > L) {
				continue;
			}
			
			arr.add(i);
			nCr(arr, score + food[i][0], kcal + food[i][1]);
			arr.pop();
		}
	}
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		T = Integer.parseInt(br.readLine());
		
		for (int tc = 1; tc <= T; tc++) {
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			L = Integer.parseInt(st.nextToken());

			food = new int[N][2];
			for (int i = 0; i < N; i++) {
				st = new StringTokenizer(br.readLine());
				
				food[i][0] = Integer.parseInt(st.nextToken());
				food[i][1] = Integer.parseInt(st.nextToken());
			}
			
			answer = 0;
			
			nCr(new Stack<Integer>(), 0, 0);
			
			System.out.println("#" + tc + " " + answer);
		}
	}

}
