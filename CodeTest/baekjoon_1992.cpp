//#1992: 쿼드 트리
//풀이법: 분할정복으로 쪼개어 같은 숫자가 연속일 경우 합치는 방향으로 작성

#include <iostream>
#include <vector>
#include <string>

using namespace std;

string quad_check(vector<vector<bool>>& img, int r,int c,int len) {
	if (len == 1) {
		return (img[r][c]) ? "1" : "0";
	}

	int next_len = len / 2;

	int p_row[4] = { r,r,r+next_len,r + next_len };
	int p_col[4] = { c,c+next_len,c,c + next_len };

	string value[4] = {};
	
	int length = 0;
	int number_count = 0;
	for (int i = 0; i < 4; i++) {
		value[i] = quad_check(img, p_row[i], p_col[i], next_len);
		length += value[i].size();
		if (value[i].size() == 1)
			number_count += value[i][0] - '0';

	}

	if (length == 4) {
		if (number_count == 0) return "0";
		if (number_count == 4) return "1";
	}

	return "(" + value[0] + value[1] + value[2] + value[3] + ")";
}

int main() {
	//입력
	int n;
	cin >> n;

	//데이터 입력
	vector<vector<bool>> img(n, vector<bool>(n, false));
	char data;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> data;
			if (data == '1') img[i][j] = true;
		}
	}

	cout << quad_check(img, 0, 0, n);

}