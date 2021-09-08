// DP
// 정수 삼각형

#include <string>
#include <vector>
#define MAX(a,b) (a>b)?a:b;

using namespace std;

int solution(vector<vector<int>> triangle) {
    int depth = triangle.size();

    for (int i = depth - 2; i >= 0; i--) {
        for (int j = 0; j < triangle[i].size(); j++) {
            triangle[i][j] += MAX(triangle[i + 1][j], triangle[i + 1][j + 1]);
        }
    }
    return triangle[0][0];
}