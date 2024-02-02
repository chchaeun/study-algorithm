package personal;

import java.io.*;
import java.util.*;

public class Main_11054 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int N = Integer.parseInt(br.readLine());
		
		int[] arr = new int[N];
		st = new StringTokenizer(br.readLine());
		
		for (int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		
		int[] increase = new int[N];
		int[] reversedIncrease = new int[N];
		
		for (int i = 0; i < N; i++) {
			increase[i] = 1;
			reversedIncrease[N - 1 - i] = 1;
			for (int j = 0; j < i; j++) {
				if (arr[i] > arr[j] && increase[i] < increase[j] + 1) {
					increase[i] = increase[j] + 1;
				}
				
				if (arr[N - 1 - i] > arr[N - 1 -j] && reversedIncrease[N - 1 - i] < reversedIncrease[N - 1 - j] + 1) {
					reversedIncrease[N - 1 - i] = reversedIncrease[N - 1 - j] + 1;
				}
			}
		}
		
		int answer = 0;
		for (int i = 0; i < N; i++) {
			if (answer < increase[i]) {
				answer = increase[i];
			}
			
			for (int j = i; j < N; j++) {
				if (arr[i] > arr[j] && increase[i] + reversedIncrease[j] > answer) {
					answer = increase[i] + reversedIncrease[j];
				}
			}
		}
		
		System.out.println(answer);
	}
}
