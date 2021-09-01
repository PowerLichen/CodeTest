// 행렬 테두리 회전

#include <vector>

using namespace std;

void init_matrix(vector<vector<int>>& matrix) {
    int count = 1;
    for (int i = 1; i < matrix.size(); i++)
        for (int j = 1; j < matrix[0].size(); j++)
            matrix[i][j] = count++;
}

vector<int> solution(int rows, int columns, vector<vector<int>> queries) {
    vector<vector<int>> matrix(rows + 1, vector<int>(columns + 1, 0));
    vector<int> answer;

    init_matrix(matrix);

    for (vector<int> query : queries) {
        int x1 = query[0], y1 = query[1], x2 = query[2], y2 = query[3];

        int temp = matrix[x1][y1];
        int min_value = temp;

        for (int i = x1; i < x2; i++) {
            matrix[i][y1] = matrix[i + 1][y1];
            if (min_value > matrix[i][y1])
                min_value = matrix[i][y1];
        }

        for (int i = y1; i < y2; i++) {
            matrix[x2][i] = matrix[x2][i + 1];
            if (min_value > matrix[x2][i])
                min_value = matrix[x2][i];

        }
        for (int i = x2; i > x1; i--) {
            matrix[i][y2] = matrix[i - 1][y2];
            if (min_value > matrix[i][y2])
                min_value = matrix[i][y2];
        }
        for (int i = y2; i > y1; i--) {
            matrix[x1][i] = matrix[x1][i - 1];
            if (min_value > matrix[x1][i])
                min_value = matrix[x1][i];
        }
        matrix[x1][y1 + 1] = temp;

        answer.push_back(min_value);
    }

    return answer;
}