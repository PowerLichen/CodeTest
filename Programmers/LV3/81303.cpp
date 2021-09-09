// 2021 īī�� ä�뿬�� ����
// ǥ ����

#include <string>
#include <vector>
#include <set>
#include <stack>

using namespace std;
stack<int> del_log;

void command(string cmd, set<int>::iterator& cur_it, set<int>& userlist) {
    char cmd_char = cmd[0];
    //�̵� ��ɾ�
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
    //���� �� ����
    else if (cmd[0] == 'C') {
        //���� �� ���� ���� it
        int deleted_num = *cur_it;
        del_log.push(deleted_num);
        set<int>::iterator next_it = userlist.erase(cur_it);
        if (next_it == userlist.end())
            next_it--;
        cur_it = next_it;
    }
    //���� �ֱ� ������ �� ����
    // cmd[0] == 'Z'
    else {
        userlist.insert(del_log.top());
        del_log.pop();
    }
}

string solution(int n, int k, vector<string> cmd) {
    set<int> userlist;
    //list �ʱ�ȭ
    for (int i = 0; i < n; i++) {
        userlist.insert(i);
    }
    //ù ��ġ ����
    auto it = userlist.begin();
    for (int i = 0; i < k; i++)
        it++;

    //Ŀ�ǵ� ����
    for (string c : cmd) {
        command(c, it, userlist);
    }

    //���ڿ� ��ȯ
    string answer(n, 'X');
    for (auto iter : userlist) {
        answer[iter] = 'O';
    }
    return answer;
}