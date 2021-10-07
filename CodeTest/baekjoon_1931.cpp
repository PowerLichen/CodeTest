//#1931: 회의실 배정
//풀이법: 각 task에 대해 빨리 끝나는 순서대로 정렬하고
//그리디 알고리즘으로 해결

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool cmp(pair<int, int>& a, pair<int, int>& b) {
	if (a.second == b.second)
		return a.first < b.first;
	return a.second < b.second;
}

int main() {
	//회의 예약 값 Load
	int n;
	cin >> n;
	vector<pair<int,int>> arr(n);

	//회의 정보를 보고 정렬
	for (int i = 0; i < n; i++)
		cin >> arr[i].first >> arr[i].second;

	sort(arr.begin(), arr.end(),cmp);

	int count_max = 0;
	int time = 0;

	for (int i = 0; i < arr.size(); i++) {
		if (time <= arr[i].first) {
			time = arr[i].second;
			count_max++;
		}
	}

	cout << count_max << endl;
}