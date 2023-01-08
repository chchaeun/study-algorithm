package practice;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main_16935_김채은 {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	
	static int N, M, R;
	static int SIZE;
	static int[][] board;
	static int[][] newBoard;
	
	static ArrayList<Integer> values;
	

	static int sy = 0;
	static int sx = 0;
	
	static int subHeight = 0;
	static int subWidth = 0;
	
	public static int[] format(String direction, int y, int x) {
		switch(direction) {
		case "DOWN_FORWARD":
			return new int[] {x, y};
		case "DOWN_REVERSE":
			return new int[] {x, SIZE-1-y};
		case "RIGHT_REVERSE":
			return new int[] {SIZE-1-y, x};
		case "LEFT_FORWARD":
			return new int[] {y, SIZE-1-x};
		default:
			return new int[] {y, x};
		}
	}
	
	public static void get(int y, int x) {
		values.add(board[y][x]);
	}
	
	public static void put(int y, int x, int value) {
		board[y][x] = value;
	}
	
	public static void execute(String direction, String type) {
		if (type.equals("GET")) {
			values = new ArrayList<>();
		}

		int idx = 0;
		for (int i = 0; i < SIZE; i++) {
			for (int j = 0; j < SIZE; j++) {
				int[] point = format(direction, i, j);
				int y = point[0];
				int x = point[1];
				
				switch(type) {
				case "GET":
					values.add(board[y][x]);
					break;
				case "PUT":
					board[y][x] = values.get(idx);
					break;
				}
				
				idx++;
			}
		}
	}
	
	public static void setSubGroup() {
		sy = 0;
		sx = 0;
		
		subHeight = 0;
		subWidth = 0;
		
		boolean flag = false;
		for (int i = 0; i < SIZE; i++) {
			for (int j = 0; j < SIZE; j++) {
				if (board[i][j] > 0) {
					sy = i;
					sx = j;
					int tmpJ = j;
					while(tmpJ < SIZE && board[i][tmpJ] > 0) {
						subWidth++;
						tmpJ++;
					}
					flag = true;
					break;
				}	
			}
			if (flag) {
				break;
			}
		}
		subHeight = subWidth == N ? M / 2 : N / 2;
		subWidth /= 2;
		
		newBoard = new int[SIZE][SIZE];
	}
	
	public static void subGroup(int h, int w, int sy, int sx, int ey, int ex) {
		for (int i = 0; i < h; i++) {
			for (int j = 0; j < w; j++) {
				newBoard[ey+i][ex+j] = board[sy+i][sx+j];
			}
		}
	}
	
	public static void endSubGroup() {
		for(int i = 0; i < SIZE; i++) {
			for (int j = 0; j < SIZE; j++) {
				board[i][j] = newBoard[i][j];
			}
		}
	}
	
	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		R = Integer.parseInt(st.nextToken());
		
		SIZE = Math.max(N, M);
		board = new int[SIZE][SIZE];
		
		for(int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			
			for (int j = 0; j < M; j++) {
				board[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		st = new StringTokenizer(br.readLine());
		for (int ec = 0; ec < R; ec++) {
			int order = Integer.parseInt(st.nextToken());
			
			switch(order) {
			case 1:
				execute("RIGHT_REVERSE", "GET");
				execute("RIGHT_FORWARD", "PUT");
				break;
			case 2:
				execute("DOWN_FORWARD", "GET");
				execute("DOWN_REVERSE", "PUT");
				break;
			case 3:
				execute("DOWN_FORWARD", "GET");
				execute("LEFT_FORWARD", "PUT");
				break;
			case 4:
				execute("DOWN_FORWARD", "GET");
				execute("RIGHT_REVERSE", "PUT");
				break;
			case 5:		
				setSubGroup();
				// 1번 -> 2번
				subGroup(subHeight, subWidth, sy, sx, sy, sx + subWidth);
				// 2번 -> 3번
				subGroup(subHeight, subWidth, sy, sx + subWidth, sy + subHeight, sx + subWidth);
				// 3번 -> 4번
				subGroup(subHeight, subWidth, sy + subHeight, sx + subWidth, sy + subHeight, sx);
				// 4번 -> 1번
				subGroup(subHeight, subWidth, sy + subHeight, sx, sy, sx);

				endSubGroup();
				break;
			case 6:
				setSubGroup();
				// 1번 -> 4번
				subGroup(subHeight, subWidth, sy, sx, sy + subHeight, sx);
				// 4번 -> 3번
				subGroup(subHeight, subWidth, sy + subHeight, sx, sy + subHeight, sx + subWidth);
				// 3번 -> 2번
				subGroup(subHeight, subWidth, sy + subHeight, sx + subWidth, sy, sx + subWidth);
				// 2번 -> 1번
				subGroup(subHeight, subWidth, sy, sx + subWidth, sy, sx);

				endSubGroup();
				break;
			}
			
		}

		boolean isZero;
		for (int i = 0; i < SIZE; i++) {
			isZero = true;
			for (int j = 0; j < SIZE; j++) {
				if (board[i][j] != 0) {
					isZero = false;
					System.out.print(board[i][j] + " ");
				}
			}
			
			if (!isZero) {
				System.out.println();				
			}
		}
		
	}

}