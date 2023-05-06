import java.util.*;
import java.io.*;

public class Main_2138_김채은 {

  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

  static int N;
  static char[] want;
  static char[] init;
  static char[] now;
  static int count;
  static int answer;

  public static void switching(int index){
    if (now[index] == '1'){
      now[index] = '0';
    }else{
      now[index] = '1';
    }
  }
  
  public static boolean check(){

    for (int i = 1; i < N; i++){
      if (want[i - 1] != now[i - 1]){
        switching(i-1);
        switching(i);
        if (i+1 < N){
          switching(i+1);
        }
        count++;
      }
    }

    if (want[N-1] == now[N-1]){
      return true;
    }
    
    return false;
  }

  public static void main(String[] args) throws IOException{
    N = Integer.parseInt(br.readLine());
    want = br.readLine().toCharArray();
    init = br.readLine().toCharArray();
    now = init.clone();
    answer = (int)1e9;
    count = 0;
    if (check()){
      answer = Math.min(answer, count);
    }
    
    now = init.clone();
    switching(0);
    switching(1);

    count = 1;
    if (check()){
      answer = Math.min(answer, count);
    }

    if (answer == (int)1e9){    
      System.out.println(-1);
    }else{
      System.out.println(answer);
    }
  }
}
