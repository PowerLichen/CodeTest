#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <algorithm>

using namespace std;


void DFS(int start, int n, vector<vector<int>>& graph) {
	//기본으로 사용할 변수 초기화
	vector<bool> check(n + 1, false);
	vector<int> result;
	result.reserve(n);
	stack<int> stack;

	stack.push(start);
	check[start] = true;
	result.push_back(start);

	while (!stack.empty()) {
		if (result.size() == n)
			break;
		int cur = stack.top();
		stack.pop();
		for (int next : graph[cur]) {
			if (check[next] == false) {
				result.push_back(next);
				check[next] = true;
				stack.push(cur);
				stack.push(next);
				break;
			}
		}
	}
	//결과 출력
	cout << result[0];
	for (int i = 1; i < result.size(); i++) {
		cout << ' ' << result[i];
	}
}

void BFS(int start, int n, vector<vector<int>>& graph) {
	//기본으로 사용할 변수 초기화
	vector<bool> check(n + 1, false);
	vector<int> result;
	result.reserve(n);
	queue<int> q;

	q.push(start);
	check[start] = true;

	while (!q.empty()) {
		int cur = q.front();
		q.pop();
		result.push_back(cur);
		if (result.size() == n)
			break;
		for (int next : graph[cur]) {
			if (check[next] == false) {
				check[next] = true;
				q.push(next);
			}
		}
	}

	cout << result[0];
	for (int i = 1; i < result.size(); i++) {
		cout << ' ' << result[i];
	}
}

int main() {
	int n, m, v;
	//정점 개수, 간선 개수, 탐색 시작 위치 초기화
	cin >> n >> m >> v;

	vector<vector<int>> graph(n + 1, vector<int>());
	//그래프 구성
	for (int i = 0; i < m; i++) {
		int node1, node2;
		cin >> node1 >> node2;
		graph[node1].push_back(node2);
		graph[node2].push_back(node1);
	}
	for (int i = 0; i < graph.size(); i++) {
		sort(graph[i].begin(), graph[i].end());
	}


	//DFS
	DFS(v, n, graph);
	cout << endl;
	BFS(v, n, graph);
}