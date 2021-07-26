#include <iostream>
#include <vector>
#include <queue>
#define MIN(a,b) (a<b ? a:b)

using namespace std;

int default_channel = 100;

int distCheck(int dest, int num) {
	//dest까지 거리
	if (dest > num) return dest - num;
	return num - dest;
}

int getDigit(int num) {
	if (num == 0) return 1;
	int cnt = 0;
	while (true) {
		if (num == 0) break;
		num /= 10;
		cnt++;
	}
	return cnt;
}

int main() {
	int n, broken_cnt;
	int ans = 0;

	cin >> n >> broken_cnt;

	ans = distCheck(n, default_channel);

	vector<bool> broken(10, true);
	vector<int> live;
	queue<int> q;

	// Check broken button
	for (int i = 0; i < broken_cnt; i++) {
		int temp;
		cin >> temp;
		broken[temp] = false;
	}

	for (int i = 0; i < 10; i++) {
		if (broken[i]) {
			ans = MIN(ans, distCheck(n, i) + getDigit(i));
			q.push(i);
		}
	}
	int pushNum;
	bool end_flag = false;
	while (!q.empty() && !end_flag) {
		int temp = q.front();
		q.pop();
		ans = MIN(ans, distCheck(n, temp) + getDigit(temp));
		for (int i = 0; i < 10; i++) {
			if (broken[i]) {
				pushNum = temp * 10 + i;
				if (pushNum != 0)
					q.push(pushNum);
			}
			if (pushNum > n) {
				end_flag = true;
				break;
			}
		}
	}
	while (!q.empty()) {
		int temp = q.front(); q.pop();
		ans = MIN(ans, distCheck(n, temp) + getDigit(temp));
	}

	cout << ans << endl;
	return 0;
}