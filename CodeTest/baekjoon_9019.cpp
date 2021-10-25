//#9019: DSLR
//풀이법: 각 명령어에 대해 BFS 수행.
// 이미 한번 연산된 수에 대해서는 queue에 해당 연산을 push하지 않음.

#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <utility>
#define MAX 10000

using namespace std;

int after_cmd(int num, char dir) {
	int result = 0;
	if (dir == 'D')
		result = (num * 2) % MAX;
	else if (dir == 'S')
		result = (num == 0) ? 9999 : num - 1;
	else if (dir == 'L')
		result = (num % 1000) * 10 + num / 1000;
	else
		result = (num % 10)* 1000 + (num / 10);	

	return result;
}

string calc_bfs(int num, int result, bool* check) {

	char cmds[4] = { 'D','S','L','R' };

	queue<pair<int, string>> pair_q;
	pair_q.push(make_pair(num, ""));
	check[num] = true;

	while (!pair_q.empty()) {
		auto current = pair_q.front();
		string cmd_list = current.second;
		pair_q.pop();		

		for (int i = 0; i < 4; i++) {
			//각 명령어 연산 후 결과
			int nextNum = after_cmd(current.first, cmds[i]);

			if (nextNum == result)
				return cmd_list + cmds[i];

			if (check[nextNum] == false) {
				check[nextNum] = true;
				pair_q.push(make_pair(nextNum, cmd_list + cmds[i]));
			}
		}
	}

	return "";
}


int main() {
	int count;
	int input, result;

	cin >> count;
	for (int n = 0; n < count; n++) {
		bool check[MAX] = { false, };
		cin >> input >> result;
		cout << calc_bfs(input, result, check) << endl;
	}
}