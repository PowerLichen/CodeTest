#include <iostream>
#include <string>

using namespace std;

int main() {
	int num;
	string data;
	cin >> num;

	for (int i = 0; i < num; i++) {
		int result = 0;
		int score = 1;
		cin >> data;
		for (int j = 0; j < data.length(); j++) {
			if (data[j] == 'O') {
				result += score++;
			}
			else if (data[j] == 'X') {
				score = 1;
			}
		}
		cout << result << endl;
	}
}