package practice;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main_16926_김채은 {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	
	static int N, M, R;
	static int[][] board;
	static boolean[][] visited;
	
	static ArrayList<int[]> points;
	static ArrayList<Integer> values;
	
	public static boolean inRange(int y, int x) {
		return 0 <= y && y < N && 0 <= x && x < M;
	}
	
	public static void search(int sy, int sx) {
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
			if (!inRange(ny, nx) || visited[ny][nx]) {
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
	
	public static void put() {
		// 등록해준 포인트에 몇 번 밀지 계산해서 board에 넣기
		// 범위 넘어가면 나머지 연산 처리
		for (int i = 0; i < values.size(); i++) {
			int[] point = points.get((i + R) % values.size());
			board[point[0]][point[1]] = values.get(i);
		}
	}
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		R = Integer.parseInt(st.nextToken());

		board = new int[N][M];
		visited = new boolean[N][M];
		
		for(int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			
			for (int j = 0; j < M; j++) {
				board[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		// 0, 0 출발해서 대각선 아래로 넘어가면서 맨 안쪽까지 search, put 반복
		int sy = 0;
		int sx = 0;
		while (!visited[sy][sx]) {
			search(sy, sx);
			put();
			sy++;
			sx++;
		}

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				System.out.print(board[i][j] + " ");
			}
			System.out.println();
		}
	}
}
