#include <iostream>
#include <vector>
#define MIN(a,b) (a<b?a:b)

using namespace std;

bool checkDia(vector<vector<bool>>& mine, int i, int j, int num) {
	num--;
	for (int n = 0; n < num; n++) {		
		if (mine[++i][--j] == false)
			return false;
	}
	for (int n = 0; n < num; n++) {
		if (mine[++i][++j] == false)
			return false;
	}
	for (int n = 0; n < num; n++) {
		if (mine[--i][++j] == false)
			return false;
	}
	for (int n = 0; n < num; n++) {
		if (mine[--i][--j] == false)
			return false;
	}
	return true;
}
int main() {
	int r, c;
	cin >> r >> c;
	vector<vector<bool>> mine(r, vector<bool>(c, false));

	// 광산 초기화
	for (int i = 0; i < r; i++) {
		for (int j = 0; j < c; j++) {
			char s;
			cin >> s;
			if (s == '1')
				mine[i][j] = true;
		}
	}

	//배열 내 들어갈 수 있는 가장 큰 다이아 크기
	int num = (MIN(r, c) + 1) / 2;
	for (; num > 0; num--) {
		//다이아의 가로세로 크기
		int size = 2 * num - 1;
		for (int i = 0; i <= r-size; i++) {
			for (int j = num - 1; j <= c - num; j++) {
				if (mine[i][j] && checkDia(mine, i, j, num)) {
					cout << num << endl;
					return 0;
				}
			}
		}
	}
}