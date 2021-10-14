//#9461: 집합
//풀이법: bool값으로 값의 유무를 저장하고 연산을 수행

#include <iostream>
#include <string>
#include <cstring>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	
	int count, num;
	string command;
	bool check[21] = { false, };

	//연산 갯수 입력
	cin >> count;

	for (int i = 0; i < count; i++) {
		cin >> command;
		switch (command[0]) {
		case 'a':
			//add 연산
			if (command[1] == 'd') {
				cin >> num;
				check[num] |= true;
			}
			//all 연산
			else
				memset(check, true, 21);
			break;
			//remove 연산
		case 'r':
			cin >> num;
			check[num] &= false;
			break;
			//check 연산
		case 'c':
			cin >> num;
			cout << ((check[num]) ? '1' : '0') << '\n';
			break;
			//toggle 연산
		case 't':
			cin >> num;
			check[num] = !check[num];
			break;
			// empty 연산
		case 'e':
			memset(check, false, 21);
			break;
		}
	}
}