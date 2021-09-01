// 2021 카카오 채용인턴
// 거리두기 확인하기

#include <string>
#include <vector>
#include <utility>

using namespace std;

int dX[] = { 1,-1,0,0 };
int dY[] = { 0,0,1,-1 };

bool getCheckPlace(vector<string>& room, pair<int,int> h) {
    vector<int> directions;
    int check = false;
    int nX, nY;
    //초기위치에서 4방향에 대한 확인
    for (int i = 0; i < 4; i++) {
        nX = h.first + dX[i];
        nY = h.second + dY[i];
        if (nX < 0 || nY < 0 || nX >= 5 || nY >= 5)
            continue;
        //해당 방향에 사람이 앉아있는 경우
        if (room[nX][nY] == 'P')
            return true;
        //해당 방향이 빈 자리인 경우.
        else if (room[nX][nY] == 'O')
            directions.push_back(i);
    }
    //초기 4방향 중 파티션으로 안 막혀있는 자리에 대해 4방향 체크
    for (int d : directions) {
        //이미 온 방향을 계산해서, 해당 위치는 계산하지 않음.
        int from = (d % 2 == 0) ? d + 1 : d - 1;
        for (int i = 0; i < 4; i++) {
            if (i == from)
                continue;
            nX = h.first + dX[d] + dX[i];
            nY = h.second + dY[d] + dY[i];
            if (nX < 0 || nY < 0 || nX >= 5 || nY >= 5)
                continue;

            if (room[nX][nY] == 'P')
                return true;
        }
    }
    return false;
}

vector<int> solution(vector<vector<string>> places) {
    vector<int> answer;
    for (vector<string> room : places) {
        bool check = false;
        vector<pair<int, int>> human;
        for (int i = 0; i < 5; i++)
            for (int j = 0; j < 5; j++)
                if (room[i][j] == 'P')
                    human.push_back(make_pair(i, j));
        for (auto& h : human) {
            if (getCheckPlace(room, h)) {
                check = true;
                break;
            }
        }
        (check) ? answer.push_back(0) : answer.push_back(1);
    }

    return answer;
}