// 2021 카카오 채용연계 인턴
// 표 편집

#include <string>
#include <vector>
#include <set>
#include <stack>

using namespace std;
stack<int> del_log;

void command(string cmd, set<int>::iterator& cur_it, set<int>& userlist) {
    char cmd_char = cmd[0];
    //이동 명령어
    if (cmd_char == 'U' || cmd_char == 'D') {
        int num = stoi(cmd.substr(2));
        if (cmd_char == 'U') {
            for (int i = 0; i < num; i++)
                cur_it--;
        }
        else {
            for (int i = 0; i < num; i++)
                cur_it++;
        }
    }
    //현재 행 삭제
    else if (cmd[0] == 'C') {
        //삭제 후 다음 원소 it
        int deleted_num = *cur_it;
        del_log.push(deleted_num);
        set<int>::iterator next_it = userlist.erase(cur_it);
        if (next_it == userlist.end())
            next_it--;
        cur_it = next_it;
    }
    //가장 최근 삭제된 행 복구
    // cmd[0] == 'Z'
    else {
        userlist.insert(del_log.top());
        del_log.pop();
    }
}

string solution(int n, int k, vector<string> cmd) {
    set<int> userlist;
    //list 초기화
    for (int i = 0; i < n; i++) {
        userlist.insert(i);
    }
    //첫 위치 지정
    auto it = userlist.begin();
    for (int i = 0; i < k; i++)
        it++;

    //커맨드 실행
    for (string c : cmd) {
        command(c, it, userlist);
    }

    //문자열 변환
    string answer(n, 'X');
    for (auto iter : userlist) {
        answer[iter] = 'O';
    }
    return answer;
}