//2019 카카오 개발자 겨울 인턴십
//불량 사용자

#include <string>
#include <vector>
#include <set>

using namespace std;

set<vector<int>> result_set;

vector<int> matchCheck(string& bid, vector<string>& user_id) {
    vector<int> result;
    for (int i = 0; i < user_id.size(); i++) {
        string uid = user_id[i];
        if (bid.size() != uid.size())
            continue;

        bool check = true;
        for (int j = 0; j < uid.size(); j++)
            if (bid[j] != '*' && (bid[j] != uid[j])) {
                check = false;
                break;
            }
        if (check)
            result.push_back(i);
    }
    return result;
}

void combList(int idx, vector<vector<int>>& banned_list, vector<bool>& is_selected) {
    if (idx == banned_list.size()) {
        vector<int> temp;
        temp.reserve(banned_list.size());
        for (int i = 0; i < is_selected.size(); i++)
            if (is_selected[i])
                temp.push_back(i);

        result_set.insert(temp);
        return;
    }
    for (int i = 0; i < banned_list[idx].size(); i++) {
        if (is_selected[banned_list[idx][i]])
            continue;
        is_selected[banned_list[idx][i]] = true;
        combList(idx + 1, banned_list, is_selected);
        is_selected[banned_list[idx][i]] = false;
    }
}


int solution(vector<string> user_id, vector<string> banned_id) {
    vector<vector<int>> banned_list;
    vector<bool> is_selected(user_id.size(), false);

    for (string bid : banned_id) {
        banned_list.push_back(matchCheck(bid, user_id));
    }
    combList(0, banned_list, is_selected);

    return result_set.size();
}