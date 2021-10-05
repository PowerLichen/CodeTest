//#1541 잃어버린 괄호
// 0-9와 +,-로만 이루어진 식


#include <iostream>
#include <vector>
#include <string>

using namespace std;


int main() {
	//1. -가 나올 때 까지 result에 수를 더함
	//2. -가 나오면, 다음 -가 나올때까지 temp에 더함
	//3. 위를 반복

	int result = 0;
	int cur_num = 0;

	string str;
	cin >> str;

	bool minus_chk = false;

	for (char ch : str) {
		//문자인 경우
		if (ch == '+' || ch == '-') {
			result += (minus_chk) ? -cur_num : cur_num;
			if(!minus_chk && ch == '-') minus_chk = true;

			cur_num = 0;
		}
		//숫자인 경우
		else {
			cur_num *= 10;
			cur_num += ch - '0';
		}
	}

	result += (minus_chk) ? -cur_num : cur_num;

	cout << result;
}