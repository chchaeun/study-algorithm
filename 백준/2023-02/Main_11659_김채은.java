package practice;

import java.io.*;
import java.util.*;

public class Main_11659_김채은 {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	static StringTokenizer st;
	static int N, M;
	static int[] arr;
	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		arr = new int[N + 1];
		st = new StringTokenizer(br.readLine());
		
		// 누적합으로 초기화
		for (int i = 1; i <= N; i++) {
			arr[i] = arr[i-1] + Integer.parseInt(st.nextToken());
		}
		
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			
			// 1부터 b까지의 합 - 1부터 a-1까지의 합 = a부터 b까지의 합
			bw.write(String.valueOf(arr[b] - arr[a-1]));
			bw.write("\n");
		}
		
		bw.flush();
		bw.close();
	}
}
