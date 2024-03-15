package practice;

import java.io.*;
import java.util.*;

public class Solution_4012_김채은 {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	
	static int T;
	static int N;
	static int[][] S;
	
	static int answer;
	static int count;
	static int maxCount;
	
	public static int diff(boolean[] visited) {
		ArrayList<Integer> food1 = new ArrayList<>();
		ArrayList<Integer> food2 = new ArrayList<>();

		for (int i = 0; i < N; i++) {
			if (visited[i]) {
				food1.add(i);
			}else {
				food2.add(i);
			}
		}
		
		
		int score1 = 0;
		int score2 = 0;
		
		for (int i = 0; i < N/2; i++) {
			for (int j = 0; j < N/2; j++) {
				if (i!=j) {
					score1 += S[food1.get(i)][food1.get(j)];
					score2 += S[food2.get(i)][food2.get(j)];
				}
			}
		}
		
		return Math.abs(score1 - score2);
	}
	
	public static int nCrValue() {
		int result = 1;
		
		for (int i = 0; i < N/2; i++) {
			result *= N - i;
			result /= i + 1;
		}
		
		return result;
	}
	
	public static void nCr(Stack<Integer> arr, boolean[] visited) {		
		if (arr.size() == N / 2) {
			if (count == maxCount) {
				return;
			}
			
			int difference = diff(visited);
			if (answer > difference) {
				answer = difference;
			}
			
			count++;
			return;
		}
		
		for (int i = 0; i < N; i++) {
			if (arr.size() > 0 && arr.peek() >= i) {
				continue;
			}
			
			arr.add(i);
			visited[i] = true; 
			nCr(arr, visited);
			arr.pop();
			visited[i] = false;
		}
	}
	public static void main(String[] args) throws NumberFormatException, IOException {
		T = Integer.parseInt(br.readLine());
		
		for (int tc = 1; tc <= T; tc++) {
			N = Integer.parseInt(br.readLine());
			S = new int[N][N];
			
			for (int i = 0; i < N; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j < N; j++) {
					S[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			
			answer = (int) 1e9;
			count = 0;
			maxCount = nCrValue() / 2;
			
			nCr(new Stack<Integer>(), new boolean[N]);
		
			System.out.println("#" + tc + " " + answer);
		}
		
		
		
	}

}
