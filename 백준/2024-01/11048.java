import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
public class Main_11048_김채은 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = null;

		int N, M;
		st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		int board[][] = new int[N][M];
		int dp[][] = new int[N][M];
		
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < M; j++) {
				board[i][j] = Integer.parseInt(st.nextToken());
				dp[i][j] = 0;
			}
		}
		
		dp[0][0] = board[0][0];
		
		int dyx[][] = {{0, -1}, {-1, 0}, {-1, -1}};
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				for (int k = 0; k < 3; k++) {
					int ny = i + dyx[k][0];
					int nx = j + dyx[k][1];
					
					if (0 <= ny && ny < N && 0 <= nx && 0 < M) {
						if(dp[i][j] < dp[ny][nx] + board[i][j]) {
							dp[i][j] = dp[ny][nx] + board[i][j];
						}
					}
				}
			}
		}
		System.out.println(dp[N-1][M-1]);
	}

}
