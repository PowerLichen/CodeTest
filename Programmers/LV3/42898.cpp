//동적 계획법
//등굣길

#include <string>
#include <vector>
#define MAX(a,b) (a>b)?a:b;

using namespace std;

int solution(int m, int n, vector<vector<int>> puddles) {
    int answer = 0;
    vector<vector<int>> map(n + 1, vector<int>(m + 1, 0));
    for (vector<int> puddle : puddles) {
        map[puddle[1]][puddle[0]] = -1;
    }
    //가로 초기화
    for (int i = 1; i <= m && map[1][i] >= 0; i++)
        map[1][i] = 1;
    //세로 초기화
    for (int i = 1; i <= n && map[i][1] >= 0; i++)
        map[i][1] = 1;

    //계산
    for (int i = 2; i <= n; i++) {
        for (int j = 2; j <= m; j++) {
            if (map[i][j] < 0)
                continue;
            if (map[i - 1][j] > 0)
                map[i][j] += map[i - 1][j];
            if (map[i][j - 1] > 0)
                map[i][j] += map[i][j - 1];

            map[i][j] %= 1000000007;
        }
    }

    return map[n][m];
}