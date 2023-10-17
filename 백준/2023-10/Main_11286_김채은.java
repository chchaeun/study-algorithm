package practice;
import java.io.*;
import java.util.*;
public class Main_11286_김채은 {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	
	public static void main(String[] args) throws NumberFormatException, IOException {

		int N = Integer.parseInt(br.readLine());
		
		PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> {

			if (Math.abs(a) < Math.abs(b)) {
				return -1;
			}else if (Math.abs(a) == Math.abs(b)) {
				// 절댓값 같으면 원래 오름차순 연산대로
				return a - b;
			}else {
				return 1;
			}
		});
		
		for (int i = 0; i < N; i++) {
			int num = Integer.parseInt(br.readLine());
			
			if (num == 0) {
				if (pq.size() > 0) {
					System.out.println(pq.poll());
				}else {
					System.out.println(0);
				}
			}else {				
				pq.add(num);
			}
		}
	}

}
