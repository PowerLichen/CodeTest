//#1260: 1로 만들기

#include <iostream>
#include <vector>

using namespace std;

int result[1000001];

int main() {
	//1<=num<=10^6
	int num;
	cin >> num;
	
	result[1] = 0, result[2] = 1, result[3] = 1, result[4] = 2, result[5] = 3;

	for (int i = 6; i <= num; i++) {
		vector<int> data;
		if (i % 3 == 0) data.push_back(result[i / 3] + 1);
		if(i%2==0) data.push_back(result[i / 2] + 1);
		data.push_back(result[i - 1] + 1);

		int min_value = data[0];
		switch (data.size()) {
		case 3:
			min_value = min(min_value, min(data[1], data[2]));
		case 2:
			min_value = min(min_value, data[1]);
		}

		result[i] = min_value;
	}

	cout << result[num];
}