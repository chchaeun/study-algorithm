package practice;

import java.util.Scanner;

public class Main_17478_김채은 {
	public static String underbar = "____";

	public static String init = "어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.";
	public static String answer1[] = {"\"재귀함수가 뭔가요?\"",
			"\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.",
			"마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.",
			"그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\""};
	public static String answer2[] = {"\"재귀함수가 뭔가요?\"", "\"재귀함수는 자기 자신을 호출하는 함수라네\""};
	public static String answer3 = "라고 답변하였지.";
	
	// 현재 depth에 따라 underbar를 출력하는 함수
	public static void printUnderbar(int current) {
		for(int i = 0; i < current; i++) {
			System.out.print("____");
		}
	}
	
	// 재귀 호출을 진행하는 함수
	public static void recursion(int depth, int current) {
		
		if (depth > current) {
			// 아직 depth에 다다르지 않은 경우, 첫 질문을 출력하고 재귀를 호출한다.
			for (String a: answer1){
				printUnderbar(current);
				System.out.println(a);
			}
			
			recursion(depth, current + 1);
		} else if (depth == current) {
			// depth에 다다른 경우, 답변을 출력한다.
			for (String a: answer2) {
				printUnderbar(current);
				System.out.println(a);
			}
		}
		
		// 함수를 빠져나오며 "라고 답변하였지." 를 출력한다.
		printUnderbar(current);
		System.out.println(answer3);
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		
		System.out.println(init);
		
		recursion(N, 0);
	}
}
