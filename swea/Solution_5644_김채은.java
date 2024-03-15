import java.util.*;
import java.io.*;
public class Solution_5644_김채은 {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	
	static int N = 10;
	static int T;
	static int M, A;
	static int[] aMove;
	static int[] bMove;
	static int[][] BC;
	
	static int ay, ax;
	static int by, bx;
	
	static ArrayList<Integer> aIn;
	static ArrayList<Integer> bIn;
	
	public static void move(int t) {
		int[] dys = {0, 0, 1, 0, -1};
		int[] dxs = {0, -1, 0, 1, 0};
		
		ay += dys[aMove[t]];
		ax += dxs[aMove[t]];
		by += dys[bMove[t]];
		bx += dxs[bMove[t]];
	}
	
	public static int getDistance(int y1, int x1, int y2, int x2) {
		return Math.abs(y1 - y2) + Math.abs(x1 - x2);
	}
	
	public static boolean isIn(int y, int x, int[] bc) {
		return getDistance(y, x, bc[0], bc[1]) <= bc[2];
	}
	
    // 현재 초에 a와 b가 어느 영역에서 충전할 수 있는지
	public static void nowIn() {
		aIn = new ArrayList<>();
		bIn = new ArrayList<>();
		
		for (int i = 0; i < A; i++) {
			if (isIn(ay, ax, BC[i])) {
				aIn.add(i);
			}if (isIn(by, bx, BC[i])) {
				bIn.add(i);
			}
		}
	}
	
	public static int maxCharge() {
		int charge = 0;
		// a 안에만 있는 경우
		for(int a: aIn) {
			if (charge < BC[a][3]) {
				charge = BC[a][3];
			}
		}
        // b 안에만 있는 경우
		for(int b: bIn) {
			if (charge < BC[b][3]) {
				charge = BC[b][3];
			}
		}
		
        // 둘 다 있는 경우
		for (int a: aIn) {
			for (int b: bIn) {
				if (a == b && charge < BC[a][3]) {
                    // 같은 영역에 들어가 있는 경우
					charge = BC[a][3];
				}else if (a != b && charge < BC[a][3] + BC[b][3]){
                    // 다른 영역에 들어가 있는 경우
					charge = BC[a][3] + BC[b][3];
				}
			}
		}
		return charge;
	}
	
	public static void main(String[] args) throws IOException{
		T = Integer.parseInt(br.readLine());
		
		for (int tc = 1; tc <= T; tc++) {
			int answer = 0;
			
			st = new StringTokenizer(br.readLine());
			M = Integer.parseInt(st.nextToken());
			A = Integer.parseInt(st.nextToken());
			
			aMove = new int[M];
			bMove = new int[M];
			st = new StringTokenizer(br.readLine());
			for (int i = 0; i < M; i++) {
				aMove[i] = Integer.parseInt(st.nextToken());
			}
			st = new StringTokenizer(br.readLine());
			for (int i = 0; i < M; i++) {
				bMove[i] = Integer.parseInt(st.nextToken());
			}
			
			BC = new int[A][4];
			for (int i = 0; i < A; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j < 4; j++) {
					BC[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			
			ay = 1; ax = 1;
			by = N; bx = N;
    
			nowIn();
			answer += maxCharge();
			
			for (int i = 0; i < M; i++) {
				move(i);
				nowIn();
				
				answer += maxCharge();
			}
			
			System.out.println("#" + tc + " " + answer);
		}
	}

}
