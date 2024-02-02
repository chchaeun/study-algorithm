package practice;

import java.io.*;
import java.util.*;

public class Main_15649_김채은 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int N, M;
	
	public static void recursion(ArrayList<Integer> arr, boolean[] visited) {
		// 배열 사이즈가 M과 같아지면 출력 후 리턴
		if (arr.size() == M) {
			for (int a: arr) {
				System.out.print(a + " ");
			}
			System.out.println();
			return;
		}
		
		// N만큼 돌면서 방문하지 않는 숫자 arr에 넣고 재귀함수 실행
		// 빠져나온 뒤 넣은 수 pop 해주고, visited도 다시 미방문 처리
		for (int i = 1; i < N + 1; i++) {
			if (visited[i]) {
				continue;
			}
			arr.add(i);
			visited[i] = true;
			recursion(arr, visited);
			arr.remove(arr.size() - 1);
			visited[i] = false;
		}
	}
	
	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());

		ArrayList<Integer> arr = new ArrayList<>();
		boolean[] visited = new boolean[N + 1];
		recursion(arr, visited);
	}
}
