package practice;

import java.io.*;
import java.util.*;

public class Main_2493_김채은 {
	
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	static StringTokenizer st;
	static int[] tower;
	static int[] receiver;
	
	public static int search(int target, int other) {
		if (other == 0) {
			return other;
		}
		
		if (tower[other] < tower[target]) {
			return search(target, receiver[other]);
		} else {
			return other;
		}
	}
	
	public static void main(String[] args) throws NumberFormatException, IOException {
	
		int N = Integer.parseInt(br.readLine());
		tower = new int[N + 1];
		receiver = new int[N + 1];
		receiver[0] = 0;
		
		st = new StringTokenizer(br.readLine());
		for (int i = 1; i <= N; i++) {
			tower[i] = Integer.parseInt(st.nextToken());
		}

		boolean noReceiver = true;
		
		for (int i = 1; i <= N; i++) {
			receiver[i] = search(i, i-1);
			if (receiver[i] > 0) {
				noReceiver = false;
			}
		}
		
		if (noReceiver) {
			bw.write(String.valueOf(0));
		} else {
			for (int i = 1; i <= N; i++) {
				bw.write(String.valueOf(receiver[i]));
				bw.write(" ");
			}
		}
		
		bw.flush();
		bw.close();
	}

}
