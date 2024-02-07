package homework;

import java.io.*;
import java.util.*;

public class Solution_1228_김채은 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	static StringTokenizer st;
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		
		for (int tc = 1; tc <= 10; tc++) {

			int N = Integer.parseInt(br.readLine());
			ArrayList<String> original = new ArrayList<>();

			st = new StringTokenizer(br.readLine());
			for (int i = 0; i < N; i++) {
				original.add(st.nextToken());
			}
			
			int M = Integer.parseInt(br.readLine());
			
			String[] arr = br.readLine().split("I");
			
			for (String a: arr) {
				if (a.length() == 0) {
					continue;
				}
				st = new StringTokenizer(a);
				int x = Integer.parseInt(st.nextToken());
				int y = Integer.parseInt(st.nextToken());
				
				for (int i = 0; i < y; i++) {
					original.add(x + i, st.nextToken());
				}
			}
			
			bw.write("#" + tc +" ");
			
			for (int i = 0; i < 10; i++) {
				bw.write(original.get(i) + " ");
			}

			bw.write("\n");
		}
		
		
		bw.flush();
		bw.close();
		
		
	}

}
