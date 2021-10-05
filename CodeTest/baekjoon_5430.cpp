//#5430: AC
//풀이법: 현재 범위를 나타내는 인덱스인 front와 rear를 사용하여
//최종결과를 출력한다.

#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<int> read_array(int rear) {
	vector<int> arr;
	string temp;
	cin >> temp;

	int buf = 0;
	for (char ch : temp) {
		if (isdigit(ch)) {
			buf *= 10;
			buf += ch - '0';
		}
		else {
			arr.push_back(buf);
			buf = 0;
		}
	}
	return arr;
}

void run_test() {
	//arr의 첫 값에 0이 들어가므로, rear는 입력받은 길이 그대로 사용
	string commands;
	int front = 1, rear;
	bool isReverse = false;

	cin >> commands;
	cin >> rear;

	vector<int> arr = read_array(rear);

	//커맨드 수행
	for (char f : commands) {
		//뒤집기
		if (f == 'R') {
			isReverse = !isReverse;
		}
		//버리기
		else {
			if (front > rear) {
				cout << "error" << endl;
				return;
			}
			(isReverse) ? rear-- : front++;
		}
	}

	//출력
	cout << '[';
	while (front <= rear) {
		if (isReverse) cout << arr[rear--];
		else cout << arr[front++];

		if (front > rear)
			break;

		cout << ',';
	}
	cout << ']' << endl;
	return;
}


int main() {
	//테스트 케이스 t(<=100)
	int t;
	cin >> t;

	//arr의 첫 값에 0이 들어가므로, rear는 입력받은 길이 그대로 사용
	for (int i = 0; i < t; i++) {
		run_test();
	}
}