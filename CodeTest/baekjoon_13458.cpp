#include <iostream>
#include <vector>
using namespace std;
int main() {
	long int result = 0;
	long int room, head, sub;
	cin >> room;

	vector<int> students(room);

	for (int i = 0; i < room; i++) {
		long int temp;
		cin >> temp;
		students[i] = temp;
	}
	cin >> head >> sub;

	for (int i = 0; i < room; i++) {
		if (students[i] <= head) {
			result++;
			continue;
		}
		long int temp = students[i] - head;
		result++;
		result += temp / sub;
		if (temp % sub > 0)
			result++;
	}

	cout << result;
}