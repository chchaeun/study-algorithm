package boj2056;

import java.io.*;
import java.util.*;

public class Main_2056 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int N = Integer.parseInt(br.readLine());
        ArrayList<Integer> dp = new ArrayList<>(){{add(0);}};
        HashMap<Integer, ArrayList<Integer>> previous = new HashMap();

        for (int i = 1; i < N + 1; i++){
            st = new StringTokenizer(br.readLine());
            dp.add(Integer.parseInt(st.nextToken()));
            int P = Integer.parseInt(st.nextToken());
            ArrayList<Integer> temp = new ArrayList<>();
            for (int j = 0; j < P; j++){
                temp.add(Integer.parseInt(st.nextToken()));
            }
            previous.put(i, temp);
        }
        System.out.println(dp);
        System.out.println(previous);
        int answer = 0;
        for (int i = 1; i < N + 1; i++){
            int max = 0;
            int maxIndex = 0;
            for (int p : previous.get(i)){
                if (max < dp.get(p)){
                    max = dp.get(p);
                    maxIndex = p;
                }
            }
            dp.set(i, dp.get(maxIndex) + dp.get(i));

            if (answer < dp.get(i)){
                answer = dp.get(i);
            }
        }

        System.out.println(answer);
    }
}