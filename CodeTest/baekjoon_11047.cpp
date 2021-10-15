//#11047: 동전 0
//풀이법: 큰 동전부터 target 금액을 소진하도록 구현

#include <iostream>
#include <vector>

using namespace std;

int main() {
	int result = 0;
	int n, target;
	cin >> n >> target;

	vector<int> coins(n);

	for (int i = n - 1; i >= 0; i--)
		cin >> coins[i];

	//동전 세기
	for (int i = 0; i < n; i++) {
		if (target == 0) break;
		if (target >= coins[i]) {
			int count_coin = target / coins[i];
			target -= count_coin * coins[i];
			result += count_coin;
		}
	}

	cout << result << endl;
}