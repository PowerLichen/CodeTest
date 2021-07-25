#include <iostream>
#include <vector>
#include <queue>
#include <utility>
using namespace std;

void check_map(vector<vector<int>> &map, int x, int y, int n, int m) {
	int dx[] = { 0,0,1,-1 };
	int dy[] = { 1, -1, 0, 0 };

	vector<vector<int>> visit(n, vector<int>(m, 0));

	queue<pair<int, int>> q;
	q.push(make_pair(x, y));
	visit[x][y] = 1;
	while (!q.empty()) {
		auto current = q.front();
		q.pop();
		map[current.first][current.second] = 0;
		for (int i = 0; i < 4; i++) {
			int next_x = current.first + dx[i];
			int next_y = current.second + dy[i];
			if (next_x < 0 || next_y<0 || next_x >=n || next_y >= m)
				continue;
			
			if (map[next_x][next_y] == 1 && visit[next_x][next_y] == 0) {
				q.push(make_pair(next_x, next_y));
				visit[next_x][next_y] = 1;
			}
		}
	}
}

int main() {
	int t, m, n, k;
	cin >> t;
	for (int num = 0; num < t; num++) {
		cin >> m >> n >> k;
		vector<vector<int>> map(n, vector<int>(m, 0));

		for (int i = 0; i < k; i++) {
			int x, y;
			cin >> x >> y;
			map[y][x] = 1;
		}

		int count = 0;

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (map[i][j] == 1) {
					check_map(map, i, j, n, m);
					count++;
				}
			}
		}

		cout << count << endl;
	}	
}