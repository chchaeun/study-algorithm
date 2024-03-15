package practice;

import java.io.*;
import java.util.*;

public class Main_17406_김채은 {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	
	static int N, M, K;
	static int[][] order;
	
	static ArrayList<int[]> points;
	static ArrayList<Integer> values;
	static int answer = (int)1e9;

	public static boolean inRange(int y, int x, int[] order) {
		int r = order[0];
		int c = order[1];
		int s = order[2];
		
		return r-s <= y && y <= r+s && c-s <= x && x <= c+s;
	}
	
	public static void get(int[][] board, boolean[][] visited, int sy, int sx, int[] order) {
		// 좌표, 값 배열 초기화
		points = new ArrayList<>();
		values = new ArrayList<>();
		
		// 시작 좌표, 값 입력
		points.add(new int[]{sy, sx});
		values.add(board[sy][sx]);
		
		int[] dys = {1, 0, -1, 0};
		int[] dxs = {0, 1, 0, -1};
		
		visited[sy][sx] = true;
		
		int y = sy;
		int x = sx;
		int d = 0;

		while (true) {
			int ny = y + dys[d];
			int nx = x + dxs[d];
			
			// 출발점에 도착하면 끝
			if (ny == sy && nx == sx) {
				break;
			}
			// 범위 벗어나거나 이미 방문 했으면 돌려주기
			if (!inRange(ny, nx, order) || visited[ny][nx]) {
				d = (d + 1) % 4;
				ny = y + dys[d];
				nx = x + dxs[d];
			}
			
			// 출발점에 도착하면 끝
			if (ny == sy && nx == sx) {
				break;
			}
			
			y = ny;
			x = nx;
			visited[y][x] = true;

			// 등록
			points.add(new int[] {y, x});
			values.add(board[y][x]);
			
		}
		
	}
	
	public static void put(int[][] board) {
		// 등록해준 포인트 1번 밀어서 넣기
		// 범위 넘어가면 나머지 연산 처리
		for (int i = 0; i < values.size(); i++) {
			int[] point = points.get(i);
			board[point[0]][point[1]] = values.get((i + 1) % values.size());
		}
	}
	
	public static void rotate(int[][] board, int[] order) {
		
		boolean[][] visited = new boolean[N + 1][M + 1];
		
		int r = order[0];
		int c = order[1];
		int s = order[2];

		int sy = r-s;
		int sx = c-s;
		
		while (sy != r && sx != c) {
			get(board, visited, sy, sx, order);
			put(board);
			
			sy++;
			sx++;
		}
		
	}
	
	public static void nPr(Stack<Integer> arr, int[][] board) {
		if (arr.size() == K) {
			// 탐색 완료 후 최솟값 업데이트
			for (int i = 1; i <= N; i++) {
				int sum = 0;
				for (int j = 1; j <= M; j++) {
					sum += board[i][j];
				}
				if (answer > sum) {
					answer = sum;
				}
			}
			return;
		}
		
		for (int i = 0; i < K; i++) {
			if (arr.indexOf(i) > -1) {
				continue;
			}

			// 분기 처리를 위해 board 복사
			
			int[][] newBoard = new int[N + 1][M + 1];

			for (int j = 0; j < N + 1; j++) {
				newBoard[j] = board[j].clone();
			}
			
			rotate(newBoard, order[i]);
			arr.add(i);
			nPr(arr, newBoard);
			arr.pop();
		}
	}
	
	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());
		
		int[][] board = new int[N+1][M+1];
		
		for (int i = 1; i <= N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 1; j <= M; j++) {
				board[i][j] = Integer.parseInt(st.nextToken());
			}
		}


		order = new int[K][3];
		
		for (int i = 0; i < K; i++) {
			st = new StringTokenizer(br.readLine());
			
			order[i][0] = Integer.parseInt(st.nextToken());
			order[i][1] = Integer.parseInt(st.nextToken());
			order[i][2] = Integer.parseInt(st.nextToken());
		}
		
		// 순열
		nPr(new Stack<>(), board);
		
		System.out.println(answer);
		
	}

}
