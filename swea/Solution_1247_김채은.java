import java.util.*;
import java.io.*;

public class Solution_1247_김채은 {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	
	static int T;
	static int N;
	
	static int[] home = new int[2];
	static int[] company = new int[2];
	
	static int[][] customer;
	
	static int answer;
	
	public static void nPr(Stack<Integer> arr, int y, int x, int dist) {
		if (arr.size() == N) {
			dist += Math.abs(y - home[0]) + Math.abs(x - home[1]);
			if (answer > dist) {
				answer = dist;
			}
			return;
		}
		
		for (int i = 0; i < N; i++) {
			if (arr.indexOf(i) > -1) {
				continue;
			}
			
			arr.add(i);
			nPr(arr, customer[i][0], customer[i][1], dist + Math.abs(y - customer[i][0]) + Math.abs(x - customer[i][1]));
			arr.pop();
		}
	}
	
	public static void main(String[] args) throws IOException {
		T = Integer.parseInt(br.readLine());
		
		for (int tc = 1; tc <= T; tc++) {
			answer = (int)1e9;
			N = Integer.parseInt(br.readLine());
			st = new StringTokenizer(br.readLine());
			
			company[0] = Integer.parseInt(st.nextToken());
			company[1] = Integer.parseInt(st.nextToken());
			home[0] = Integer.parseInt(st.nextToken());
			home[1] = Integer.parseInt(st.nextToken());
			
			customer = new int[N][2];
			
			for (int i = 0; i < N; i++) {
				customer[i][0] = Integer.parseInt(st.nextToken());
				customer[i][1] = Integer.parseInt(st.nextToken());
			}
			
			nPr(new Stack<>(), company[0], company[1], 0);
			
			System.out.println("#" + tc + " " + answer);
		}
	}

}
