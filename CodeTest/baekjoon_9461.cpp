//#9461: 파도반 수열
//풀이법: 다이나믹 프로그래밍으로 이전 값을 저장하여 출력

#include <iostream>
#define MAX 111
#define LL long long

using namespace std;

LL seq[MAX];

LL getSeq(int n) {
	if (seq[n] > 0)
		return seq[n];
	seq[n] += getSeq(n - 1) + getSeq(n - 5);
	return seq[n];
}

int main() {
	ios_base::sync_with_stdio(false);
	//입력
	int t,n;
	cin >> t;

	//데이터 입력
	seq[1] = seq[2] = seq[3] = 1;
	seq[4] = seq[5] = 2;

	for (int i = 0; i < t; i++) {
		cin >> n;
		cout << getSeq(n) << endl;
	}
}