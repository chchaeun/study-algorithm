package practice;

import java.io.*;
import java.util.*;

public class Main_15650_김채은 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int N, M;
	
	public static void nCr(ArrayList<Integer> arr) {
		if (arr.size() == M) {
			for (int a: arr) {
				System.out.print(a + " ");
			}
			System.out.println();
			return;
		}
		
		for (int i = 1; i <= N; i++) {
			// arr가 존재하면, arr의 마지막 원소보다 큰 값만 새롭게 arr에 추가할 수 있음(중복x)
			// 원소가 정렬돼있을 때만 사용 가능. 정렬되지 않은 경우 visited로 처리
			if (arr.size() > 0 && i <= arr.get(arr.size() - 1)) {
				continue;
			}
			arr.add(i);
			nCr(arr);
			arr.remove(arr.size()-1);
		}
	}
	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
	
		nCr(new ArrayList<Integer>());
	}
}
