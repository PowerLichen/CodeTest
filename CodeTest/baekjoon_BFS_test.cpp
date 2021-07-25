#include <iostream>
#include <utility>
#include <queue>

using namespace std;

int n, m;
int dx[] = { 0,0,1,-1 };
int dy[] = { 1, -1, 0, 0 };


void bfs(vector<vector<int>> &maze, vector<vector<int>> &path, vector<vector<pair<int, int>>> &pathlog, int x, int y) {	

	path[x][y] = 1;
	queue<pair<int, int>> q;
	q.push(make_pair(x, y));
	while (!q.empty()) {
		int cur_x = q.front().first;
		int cur_y = q.front().second;
		q.pop();
		for (int i = 0; i < 4; i++) {
			int next_x = cur_x + dx[i];
			int next_y = cur_y + dy[i];
			if (next_x >= 0 && next_x < n && next_y >= 0 && next_y < m) {
				if (maze[next_x][next_y] == 1 && path[next_x][next_y] == 0) {
					q.push(make_pair(next_x, next_y));
					path[next_x][next_y] = path[cur_x][cur_y] + 1;
					
					pathlog[next_x][next_y].first = cur_x;
					pathlog[next_x][next_y].second = cur_y;
				}
			}
		}
	}
}

int main() {
	cin >> n >> m;

	vector<vector<int>> maze(n, vector<int>(m, 0));
	vector<vector<int>> path(n, vector<int>(m, 0));
	vector<vector<pair<int, int>>> pathlog(n, vector<pair<int, int>>(m, pair<int, int>(0, 0)));
	// 1이 이동 가능한 칸, 0은 이동 불가능한 칸.
	for (int i = 0; i < n; i++){
		for (int j = 0; j < m; j++) {
			scanf_s("%1d", &maze[i][j],sizeof(int));
		}
	}

	bfs(maze, path, pathlog, 0, 0);

	cout << endl << path[n - 1][m - 1] << endl;


	vector<pair<int, int>> correct_path;
	int cur_x = n - 1;
	int cur_y = m - 1;
	while (true) {
		correct_path.push_back(make_pair(cur_x, cur_y));
		if (cur_x == 0 && cur_y == 0)
			break;
		int next_x = pathlog[cur_x][cur_y].first;
		int next_y = pathlog[cur_x][cur_y].second;
		cur_x = next_x;
		cur_y = next_y;
	}

	//correct_path.push_back(make_pair(cur_x, cur_y));
	for (vector<pair<int, int>>::reverse_iterator it = correct_path.rbegin(); it != correct_path.rend(); it++) {
		maze[(*it).first][(*it).second] = 9;
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cout << path[i][j] << " ";
		}
		cout << endl;
	}
}