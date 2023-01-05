package practice;

import java.io.*;
import java.util.*;

public class Solution_1233_김채은 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	
	static int N;
	static int[][] binaryTree;
	static String[] values;
	
	public static boolean isInteger(String value) {
		try {
			Integer.parseInt(value);
			return true;
		} catch (NumberFormatException e) {
			return false;
		}
	}
	
	public static boolean validate(int node) {
		// 정수
		// 리프 노드여야 함
		if (isInteger(values[node])) {
			if (binaryTree[node][0] != 0) {
				return false;
			}

			return true;
		}
		
		// 연산자
		// 자식 하나라도 없으면 false
		if (binaryTree[node][1] == 0) {
			return false;
		}
		
		// 자식 있으면 자식 노드 validate
		int left = binaryTree[node][0]; 
		int right = binaryTree[node][1];
		
		return validate(left) && validate(right);

	}
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		int T = 10;
		
		for (int tc = 1; tc <= T; tc++) {

			N = Integer.parseInt(br.readLine());
			binaryTree = new int[N + 1][2];
			values = new String[N + 1];
			
			for (int i = 1; i <= N; i++) {
				String[] input = br.readLine().split(" ");
				int node = Integer.parseInt(input[0]);
				String value = input[1];
				values[node] = value;
			
				if (input.length > 2) {
					int left = Integer.parseInt(input[2]);
					binaryTree[node][0] = left;
					
					if (input.length > 3) {
						int right = Integer.parseInt(input[3]);
						binaryTree[node][1] = right;						
					}
				}
			}
			
			
			int answer = validate(1) ? 1 : 0;
		
			System.out.println("#" + tc + " " + answer);
		}
	}

}
