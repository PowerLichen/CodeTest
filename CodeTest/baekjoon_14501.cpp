#include <iostream>
#include <vector>
using namespace std;

int max(int a, int b) {
	return (a > b) ? a : b;
}

int main() {
	int dday;
	cin >> dday;
	int result = 0;

	vector<int> time(dday+1, 0);
	vector<int> pay(dday+1, 0);
	vector<int> dp(dday+1, 0);
	int tempTime, tempPay;

	for (int i = 0; i < dday; i++) {		
		cin >> time[i] >> pay[i];
	}

	for (int i = 0; i < dday; i++) {
		if (i + time[i] <= dday) {
			dp[i + time[i]] = max(dp[i + time[i]], dp[i] + pay[i]);
			result = max(result, dp[i + time[i]]);
		}
		dp[i + 1] = max(dp[i + 1], dp[i]);
		result = max(result, dp[i + 1]);
	}
	cout << result;
}