// 그래프
// 순위

#include <string>
#include <vector>
#include <utility>
#include <queue>

using namespace std;

int solution(int n, vector<vector<int>> results) {
    int answer = 0;
    //first는 상위, second는 하위
    vector<pair<vector<int>, vector<int>>> graphs(n + 1,make_pair(vector<int>(), vector<int>()));
    for (vector<int> data : results) {
        graphs[data[0]].second.push_back(data[1]);
        graphs[data[1]].first.push_back(data[0]);
    }

    for (int i = 1; i <= n; i++) {
        pair<vector<int>, vector<int>> target = graphs[i];
        queue<int> tasks;
        vector<bool> check(n + 1, false);
        check[i] = true;
        int count = 1;

        //upper check
        tasks.push(i);
        while (!tasks.empty()) {
            int next = tasks.front();
            tasks.pop();
            for (int k : graphs[next].first) {
                if (!check[k]) {
                    count++;
                    check[k] = true;
                    tasks.push(k);
                }
            }
        }
        
        //lower check
        tasks.push(i);
        while (!tasks.empty()) {
            if (count == n)
                break;
            int next = tasks.front();
            tasks.pop();
            for (int k : graphs[next].second) {
                if (!check[k]) {
                    count++;
                    check[k] = true;
                    tasks.push(k);
                }
            }
        }

        if (count == n)
            answer++;
    }
    return answer;
}