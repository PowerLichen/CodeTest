//#9935: 문자열 폭발
//풀이법: 폭발 문자열의 마지막과 동일한 문자가 result에 들어오면, 폭발을 체크

#include <iostream>
#include <string>

using namespace std;

int main() {
	string str, boom;
	string result = "";

	cin >> str >> boom;

	char lastword = *boom.rbegin();

	for (int i = 0; i < str.size(); i++) {
		//단어 더하기
		result += str[i];

		//폭발 체크
		if (str[i] == lastword) {
			if (result.size() < boom.size())
				continue;

			int idx = result.size() - boom.size();
			int count = 1;
			for (int j = 0; j < boom.size() - 1; j++) {
				if (result[idx + j] == boom[j]) count++;
			}
			if (boom.size() == count) {
				for (int j = 0; j < boom.size(); j++)
					result.pop_back();
			}
		}
	}

	cout << ((result.size() > 0) ? result : "FRULA") << endl;
}