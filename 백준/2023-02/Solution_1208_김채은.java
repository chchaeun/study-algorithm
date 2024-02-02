package practice;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Solution_1208_김채은 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int T = 10;
	static int N = 100;
	static int D;
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		
		for (int tc = 1; tc < T + 1; tc++) {

			D = Integer.parseInt(br.readLine());
			st = new StringTokenizer(br.readLine());
			ArrayList<Integer> arr = new ArrayList<>();
			
			for (int i = 0; i < N; i++) {
				arr.add(Integer.parseInt(st.nextToken()));
			}
			
			// 최대 최소 찾기
			int max = 0;
			int min = 10000;
			for (int i = 0; i < D; i++) {
				int maxIndex = 0;
				int minIndex = 0;
				for (int j = 0; j < N; j++) {
					if (arr.get(j) > max) {
						max = arr.get(j);
						maxIndex = j;
					}if (arr.get(j) < min) {
						min = arr.get(j);
						minIndex = j;
					}
				}
				
				// 차이가 2 미만이면 빠져나옴
				if (max - min < 2) {
					break;
				}
				
				// 최대 최솟값 각각 -1 +1 
				arr.set(minIndex, arr.get(minIndex) + 1);
				arr.set(maxIndex, arr.get(maxIndex) - 1);

				max = 0;
				min = 10000;
			}

			// 최종으로 답을 구할 최대 최소 값 구하기
			int maxIndex = 0;
			int minIndex = 0;
			for (int j = 0; j < N; j++) {
				if (arr.get(j) > max) {
					max = arr.get(j);
					maxIndex = j;
				}if (arr.get(j) < min) {
					min = arr.get(j);
					minIndex = j;
				}
			}
			
			System.out.println("#" + tc + " " + (max - min));
		}
	}
}
