package personal;

import java.io.IOException;

import java.util.*;

public class Solution {
    private static Scanner sc;
    private static UserSolution usersolution = new UserSolution();

    static final int MAX_N = 25;
    static final int MAX_L = 10;

    static final int CMD_INIT = 100;
    static final int CMD_DESTROY = 200;
    static final int CMD_ALLY = 300;
    static final int CMD_ATTACK = 400;
    static final int CMD_RECRUIT = 500;

    static int [][] Sol= new int [MAX_N][MAX_N];
    static char [][][] Monarch = new char [MAX_N][MAX_N][MAX_L+1];

    private static void String2Char(char[] buf, String str) {
        Arrays.fill(buf, (char)0);
        for (int i = 0; i < str.length(); ++i)
            buf[i] = str.charAt(i);
        buf[str.length()] = '\0';
    }

    private static int run() throws IOException {
        int isOK = 0;

        int mN;
        char[] mMonarchA = new char [MAX_L + 1];
        char[] mMonarchB = new char [MAX_L + 1];
        char[] mGeneral = new char [MAX_L + 1];
        int mOption;
        int num;

        int N = sc.nextInt();
        int cmd, result, check;

        for (int c = 0; c < N; ++c) {

            cmd =  sc.nextInt();
            switch (cmd) {
            case CMD_INIT:
            	System.out.println("#" + (c + 1));
                mN = sc.nextInt();
                for (int j = 0; j < mN; j++)
                    for (int i = 0; i < mN; i++)
                        Sol[j][i] =  sc.nextInt();

                for (int j = 0; j < mN; j++)
                    for (int i = 0; i < mN; i++)
                        String2Char(Monarch[j][i], sc.next());

                usersolution.init(mN, Sol, Monarch);
                isOK = 1;
                break;

            case CMD_ALLY:

                String2Char(mMonarchA,  sc.next());
                String2Char(mMonarchB,  sc.next());
                result = usersolution.ally(mMonarchA, mMonarchB);
                System.out.println("#" + (c + 1) + ": " + result);
                check = sc.nextInt();
                if (result != check) {
                	System.out.println(check);
                	isOK = 0;
//                	System.out.println("error");
	                	
	                usersolution.printMon();
//	                usersolution.printSol();
//	                usersolution.printAlly();
                }
                
                break;

            case CMD_ATTACK:

                String2Char(mMonarchA,  sc.next());
                String2Char(mMonarchB,  sc.next());
                String2Char(mGeneral,  sc.next());
                result = usersolution.attack(mMonarchA, mMonarchB, mGeneral);
                System.out.println("#" + (c + 1) + ": " + result);
               

                check = sc.nextInt();
                if (result != check) {
                	isOK = 0;

                	System.out.println(check);
	                usersolution.printMon();
//	                usersolution.printSol();
//	                usersolution.printAlly();
                }
                break;

            case CMD_RECRUIT:
                String2Char(mMonarchA,  sc.next());
                num = sc.nextInt();
                mOption = sc.nextInt();
                result = usersolution.recruit(mMonarchA, num, mOption);
                System.out.println("#" + (c + 1) + ": " + result);
               
                
                check = sc.nextInt();
                if (result != check) {
                	isOK = 0;
                	System.out.println(check);
	                usersolution.printMon();
//	                usersolution.printSol();
//	                usersolution.printAlly();
                }
                break;
            }
        }
        usersolution.destroy();
        return isOK;
    }

    public static void main(String[] args) throws Exception {
        int T, MARK;
        System.setIn(new java.io.FileInputStream("src/personal/test.txt"));
        sc = new Scanner(System.in);

        T = sc.nextInt();
        MARK = sc.nextInt();
        for (int tc = 1; tc <= T; tc++) {
            if (run() == 1)
                System.out.println("#" + tc + " " + MARK);
            else
                System.out.println("#" + tc + " 0");
        }
        sc.close();
    }
}

class UserSolution {
	static int[] army;
	static boolean[][] enemy;
	static Map<String, Integer> nameIndex;
	
	String join(char[] name) {
		return new String(name);
	}
	
    int[] getPointByIndex(int idx) {
    	return new int[] {idx / Solution.MAX_N, idx % Solution.MAX_N};
    }
    
    int getIndexByPoint(int y, int x) {
    	return y * Solution.MAX_N + x;
    }
    
    boolean inRange(int y, int x) {
    	return 0 <= y && y < Solution.MAX_N && 0 <= x && x < Solution.MAX_N;
    }
    

	void union(int x, int y) {
		x = army[x];
		y = army[y];
		
		if (x < y) {
			army[y] = find(x);
		}else {
			army[x] = find(y);
		}
	}
	
	int find(int x) {
		if (army[x] != x) {
			army[x] = find(army[x]);
			return army[x];
		}
		
		return x;
	}
	
	void init(int N, int mSoldier[][], char mMonarch[][][]){
		army = new int[Solution.MAX_N * Solution.MAX_N];
		enemy = new boolean[Solution.MAX_N * Solution.MAX_N][Solution.MAX_N * Solution.MAX_N];
		nameIndex = new HashMap<>();
		
		int idx = 0;
		for (int i = 0; i < Solution.MAX_N; i++) {
			for(int j = 0; j < Solution.MAX_N; j++) {
				if (mMonarch[i][j][0] >= 'a') {		
					army[idx] = idx;
					nameIndex.put(join(mMonarch[i][j]), idx);
				}else {
					army[idx] = -1;
				}				
				idx++;
			}
		}
		
    }
	void destroy(){

    }

	boolean isArmy(int a, int b) {
		if (army[a] == -1 || army[b] == -1) {
			return false;
		}
		int pa = find(a);
		int pb = find(b);
		
		return pa == pb;
	}
	
	boolean isEnemy(int a, int b) {
		if (army[a] == -1 || army[b] == -1) {
			return false;
		}
		
		int pa = find(a);
		int pb = find(b);
		
		return enemy[pa][pb];
	}
	
    int ally(char mMonarchA[], char mMonarchB[]){
    	int a = nameIndex.get(join(mMonarchA));
    	int b = nameIndex.get(join(mMonarchB));

    	// 동맹 확인
    	if (isArmy(a, b)) {
    		return -1;
    	}
    	
    	// 적대 확인
    	if (isEnemy(a, b)) {
    		return -2;
    	}
    	
    	// 동맹 맺기
    	union(a, b);

        return 1;
    }
    
    void setEnemy(int a, int b) {
    	int pa = find(a);
    	int pb = find(b);
    	
    	enemy[pa][pb] = true;
    	enemy[pb][pa] = true;
    }
    
    void cutAlly(int a) {
    	int newParent = (int)1e9;
    	
		for (int i = 0; i < Solution.MAX_N * Solution.MAX_N; i++) {
			if (army[i] == a && i != a) {
				if(newParent > i) {
					newParent = i;
				}
				army[i] = newParent;
			}
			
		}
    	
		army[a] = a;
    }
    
    boolean isNearBy(int a, int b) {
    	int[] dys = {-1, -1, -1, 0, 0, 1, 1, 1};
    	int[] dxs = {-1, 0, 1, -1, 1, -1, 0, 1};
    	
    	int[] bPoint = getPointByIndex(b);
    	
    	for (int i = 0; i < 8; i++) {
    		int ny = bPoint[0] + dys[i];
    		int nx = bPoint[1] + dxs[i];
    		
    		if (inRange(ny, nx) && isArmy(getIndexByPoint(ny, nx), a)) {
    			return true;
    		}
    	}
    	
    	return false;
    }
    
    int fight(int a, int b) {
    	int attacker = 0;
    	int defender = 0;
    	
    	int[] dys = {-1, -1, -1, 0, 0, 1, 1, 1};
    	int[] dxs = {-1, 0, 1, -1, 1, -1, 0, 1};
    	

    	int[] bPoint = getPointByIndex(b);
    	defender += Solution.Sol[bPoint[0]][bPoint[1]];
    	
    	for (int i = 0; i < 8; i++) {
    		int ny = bPoint[0] + dys[i];
    		int nx = bPoint[1] + dxs[i];
    		
    		int newIdx = getIndexByPoint(ny, nx);
    		
    		if (inRange(ny, nx)) {
    			if (isArmy(newIdx, a)){
    				attacker += Solution.Sol[ny][nx] / 2;
    				Solution.Sol[ny][nx] -= Solution.Sol[ny][nx] / 2;
    			}else if (isArmy(newIdx, b)) {
    				defender += Solution.Sol[ny][nx] / 2;
    				Solution.Sol[ny][nx] -= Solution.Sol[ny][nx] / 2;
    			}
    		}
    	}
    	
    	Solution.Sol[bPoint[0]][bPoint[1]] = Math.abs(attacker - defender);

    	if (attacker > defender) {
    		return 1;
    	}else {
    		return 0;
    	}
    }
    int attack(char mMonarchA[], char mMonarchB[], char mGeneral[]){
    	int a = nameIndex.get(join(mMonarchA));
    	int b = nameIndex.get(join(mMonarchB));
    	
    	if (isArmy(a, b)) {
    		return -1;
    	}
    	
    	if (!isNearBy(a, b)) {
    		return -2;
    	}
    	
    	setEnemy(a, b);

    	int[] bPoint = getPointByIndex(b);
    	if (fight(a, b) == 1) {
    		// 새로운 군주
    		Solution.Monarch[bPoint[0]][bPoint[1]] = mGeneral.clone();
    		nameIndex.remove(join(mMonarchB));
    		nameIndex.put(join(mGeneral), b);

    		cutAlly(b);
    		for (int i = 0; i < Solution.MAX_N * Solution.MAX_N; i++) {
    			enemy[i][b] = false;
    			enemy[b][i] = false;
    		}
    		
    		ally(mMonarchA, mGeneral);
    		
    		return 1;
    	}else {
    		return 0;
    	}
    }
    
    int recruit(char mMonarch[], int mNum, int mOption){
    	int index = nameIndex.get(join(mMonarch));
    	
    	if (mOption == 0) {
    		int[] point = getPointByIndex(index);
    		Solution.Sol[point[0]][point[1]] += mNum;

    		return Solution.Sol[point[0]][point[1]];
    		
    	}else {
        	int parent = find(index);
  
    		int total = 0;
    		for (int i = 0; i < Solution.MAX_N * Solution.MAX_N; i++) {
    			if (army[i] == -1) {
    				continue;
    			}
    			if (find(i) == parent) {
    				int[] aPoint = getPointByIndex(i);
    				Solution.Sol[aPoint[0]][aPoint[1]] += mNum;
    				total += Solution.Sol[aPoint[0]][aPoint[1]];
    			}
    		}
    		return total;
    	}

    }
    
    void printSol() {
    	System.out.println("현재 군인 수");
    	for (int i = 0; i < Solution.MAX_N; i++) {
    		for (int j = 0; j < Solution.MAX_N; j++) {
    			if (Solution.Monarch[i][j][0] < 'a') {
    				continue;
    			}
    			System.out.print(Solution.Sol[i][j] + " ");
    		}
    		if (Solution.Monarch[i][0][0] < 'a') {
    			break;
    		}
    		System.out.println();
    	}
    	System.out.println();
    }
    
    void printMon() {
    	System.out.println("현재 군주");
    	for (int i = 0; i < Solution.MAX_N; i++) {
    		for (int j = 0; j < Solution.MAX_N; j++) {
    			if (Solution.Monarch[i][j][0] < 'a') {
    				continue;
    			}
    			System.out.print(Arrays.toString(Solution.Monarch[i][j]) + " ");
    		}
    		if (Solution.Monarch[i][0][0] < 'a') {
    			break;
    		}
    		System.out.println();
    	}
    	System.out.println();
    }
    
    void printAlly() {
    	System.out.println("현재 동맹");

    	for (int i = 0; i < Solution.MAX_N; i++) {
    		for (int j = 0; j < Solution.MAX_N; j++) {
    			if (Solution.Monarch[i][j][0] < 'a') {
    				continue;
    			}
    			System.out.print(find(getIndexByPoint(i, j)) + " ");
    		}
    		if (Solution.Monarch[i][0][0] < 'a') {
    			break;
    		}
    		System.out.println();
    	}
    	System.out.println();
    }
}
