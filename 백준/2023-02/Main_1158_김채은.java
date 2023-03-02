package practice;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main_1158_김채은 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	static StringTokenizer st;
	
	public static void main(String[] args) throws IOException {

		st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		
		boolean[] deleted = new boolean[N];
		
		int idx = -1;
		
		bw.append("<");
		
		for (int i = 0; i < N; i++) {
			int count = 0;
			while (count < K) {
				idx = (idx + 1) % N;
				if (!deleted[idx]) {
					count++;
				}
			}
			deleted[idx] = true;
			
			bw.append(String.valueOf(idx + 1));
			bw.append(i == N-1 ? ">" : ", ");
		}
		
		bw.flush();
		bw.close();
	}

}
