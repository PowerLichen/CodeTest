//Summer/Winter Coding(다익스트라)
//배달

#include <vector>
#include <queue>
#define MAX_DIST 10001
#define START_NUM 1

using namespace std;

void init_data(int N, vector<vector<int>>& road, vector<vector<pair<int, int>>>& graph) {
    for (auto info : road) {
        graph[info[0]].push_back(make_pair(info[1], info[2]));
        graph[info[1]].push_back(make_pair(info[0], info[2]));
    }
}

vector<int> dijkstra(int N, vector<vector<pair<int, int>>>& graph) {
    vector<int> dist(N + 1, MAX_DIST*50);
    dist[START_NUM] = 0;
    priority_queue<pair<int, int>> pq;
    pq.push(make_pair(START_NUM,0));
    while (!pq.empty()) {
        int cur = pq.top().first;
        int distance = -pq.top().second;
        pq.pop();
        if (dist[cur] < distance) continue;
        for (auto roadSet : graph[cur]) {
            int next_v = roadSet.first;
            int next_dist = distance + roadSet.second;
            if (next_dist < dist[next_v]) {
                dist[next_v] = next_dist;
                pq.push(make_pair(next_v, -next_dist));
            }
        }        
    }
    return dist;
}

int solution(int N, vector<vector<int> > road, int K) {
    int answer = 0;
    vector<vector<pair<int, int>>> graph(N + 1);

    init_data(N, road, graph);
    vector<int> result = dijkstra(N, graph);

    for (int i = 1; i <= N; i++)
        if (result[i] <= K) answer++;

    return answer;
}