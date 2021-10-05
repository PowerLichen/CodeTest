//#11659: 구간 합 구하기 4
//풀이법: 누적 합을 미리 구해두고 구간 부분을 서로 빼면 풀이 완료됨.
//cin이 입출력이 느리므로, C의 stdio를 이용.

#include <stdio.h>
#include <vector>

using namespace std;


int main() {
	//수의 개수 len, 계산 횟수 n
	int len, n;
	scanf("%d %d", &len, &n);
	
	//누적합 초기화
	vector<int> sum_arr(len + 1, 0);
	for (int i = 1; i <= len; i++) {
		scanf("%d", &sum_arr[i]);
		sum_arr[i] += sum_arr[i - 1];
	}

	//구간 입력
	int start, end;
	for (int i = 0; i < n; i++) {
		scanf("%d %d", &start, &end);
		printf("%d\n",sum_arr[end] - sum_arr[start - 1]);
	}	
}