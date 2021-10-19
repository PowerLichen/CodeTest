//#17144: 미세먼지 안녕!
//풀이법: 문제의 설명대로 구현

#include <iostream>
#include <vector>

using namespace std;
// 출력
int count_dust(vector<vector<int>>& room) {
	int result=0;
	for (int i = 0; i < room.size(); i++) {
		for (int j = 0; j < room[0].size(); j++) {
			result += room[i][j];
		}
	}

	return result + 2;
}

int main() {
	int row, col, time;
	int cleaner_r = 0, cleaner_c = 0;
	int nr[4] = { 0,0,1,-1 };
	int nc[4] = { 1,-1,0,0 };

	cin >> row >> col >> time;


	vector<vector<int>> room(row, vector<int>(col, 0));

	// 방 초기화
	for (int i = 0; i < row; i++) {
		for (int j = 0; j < col; j++) {
			cin >> room[i][j];
			if (room[i][j] == -1) {
				cleaner_r = i;
				cleaner_c = j;
			}
		}
	}
	cleaner_r--;


	//공기 청정기 작동
	for (int n = 0; n < time; n++) {
		vector<vector<int>> dust(row, vector<int>(col, 0));
		//미세먼지 확산
		for (int i = 0; i < row; i++) {
			for (int j = 0; j < col; j++) {
				int count = 0;
				for (int k = 0; k < 4; k++) {
					int next_r = i + nr[k];
					int next_c = j + nc[k];
					if (next_r < 0 || next_r == row || next_c < 0 || next_c == col)
						continue;
					if (room[next_r][next_c] == -1)
						continue;
					dust[next_r][next_c] += room[i][j] / 5;
					count++;
				}
				dust[i][j] -= (room[i][j] / 5) * count;
			}
		}

		for (int i = 0; i < row; i++)
			for (int j = 0; j < col; j++)
				room[i][j] += dust[i][j];


		//공기청정기 작동
		//위 공기순환
		int cur_r = cleaner_r, cur_c = cleaner_c;
		int temp = 0, before = temp;
		cur_c++;
		while (cur_c < (col - 1)) {
			temp = room[cur_r][cur_c];
			room[cur_r][cur_c] = before;
			before = temp;
			cur_c++;
		}
		while (cur_r > 0) {
			temp = room[cur_r][cur_c];
			room[cur_r][cur_c] = before;
			before = temp;
			cur_r--;

		}
		while (cur_c > 0) {
			temp = room[cur_r][cur_c];
			room[cur_r][cur_c] = before;
			before = temp;
			cur_c--;
		}
		while (cur_r < cleaner_r) {
			temp = room[cur_r][cur_c];
			room[cur_r][cur_c] = before;
			before = temp;
			cur_r++;
		}
		//아래 공기순환
		cleaner_r++;
		cur_r = cleaner_r, cur_c = cleaner_c;
		temp = 0, before = temp;
		cur_c++;
		while (cur_c < (col - 1)) {
			temp = room[cur_r][cur_c];
			room[cur_r][cur_c] = before;
			before = temp;
			cur_c++;
		}
		while (cur_r < (row - 1)) {
			temp = room[cur_r][cur_c];
			room[cur_r][cur_c] = before;
			before = temp;
			cur_r++;

		}
		while (cur_c > 0) {
			temp = room[cur_r][cur_c];
			room[cur_r][cur_c] = before;
			before = temp;
			cur_c--;
		}
		while (cur_r > cleaner_r) {
			temp = room[cur_r][cur_c];
			room[cur_r][cur_c] = before;
			before = temp;
			cur_r--;
		}

		cleaner_r--;
	}

	cout << count_dust(room) << endl;
}