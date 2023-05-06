package practice;

import java.io.*;

public class Solution_1289_김채은 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		// 입력
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		
		for (int i = 0; i < N; i++) {
			String bits = br.readLine();
			
			// 몇 번 바뀌었는지 카운트하는 변수
			int switching = 0;
			
			// 현재 비트 저장하는 변수
			char current = '0';
			
			for (int j = 0; j < bits.length(); j++) {
				// 현재 비트와 다른 경우 switching 증가, 현재 비트 바꿔주기
				// 현재 비트와 같은 경우 덮어쓸 필요없기 때문에 패스
				
				if (current != bits.charAt(j)) {
					switching += 1;
					current = bits.charAt(j);
				}
			}
			
			System.out.println("#" + (i+1) + " " + switching);
		}
	}

}
