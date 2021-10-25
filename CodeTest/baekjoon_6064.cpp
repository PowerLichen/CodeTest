//#6064: 카잉 달력!
//풀이법: x값이 되는 경우의 수를 찾고, 이 때 y값을 구하여 풀이.

#include <iostream>

using namespace std;

int main() {
	int n;
	int M, N, x, y;

	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> M >> N >> x >> y;

		int curNum = 0;
		for (curNum = x; curNum < M * N; curNum += M) {
			int nextY = (curNum - 1) % N + 1;
			if (y == nextY) {
				cout << curNum<<endl;
				break;
			}
		}
		if (curNum >= M * N)
			cout << -1 << endl;
	}
}