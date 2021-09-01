//2018 KAKAO BLIND
//뉴스 클러스터링

#include <string>
#include <queue>

using namespace std;

struct datas {
    char first, second;
};

bool operator==(const datas& a, const datas& b) {
    return a.first == b.first && a.second == b.second;
}
bool operator<(const datas& a, const datas& b) {
    if (a.first == b.first)
        return a.second < b.second;
    return a.first < b.first;
}

struct cmp {
    bool operator()(datas& a, datas& b) {
        if (a.first == b.first)
            return a.second > b.second;
        return a.first > b.first;
    }
};

int solution(string str1, string str2) {
    priority_queue<datas, vector<datas>, cmp> arr1;
    priority_queue<datas, vector<datas>, cmp> arr2;
    
    int cnt_union = 0;
    int cnt_inter = 0;
    // 두 글자씩 끊어서 저장.
    for (int i = 0; i < str1.length() - 1; i++) {
        if (!isalpha(str1[i]) || !isalpha(str1[i + 1])) {
            continue;
        }
        datas temp;
        temp.first = tolower(str1[i]);
        temp.second = tolower(str1[i + 1]);
        arr1.push(temp);
    }
    for (int i = 0; i < str2.length() - 1; i++) {
        if (!isalpha(str2[i]) || !isalpha(str2[i + 1])) {
            continue;
        }
        datas temp;
        temp.first = tolower(str2[i]);
        temp.second = tolower(str2[i + 1]);
        arr2.push(temp);
    }

    while (!arr1.empty() && !arr2.empty()) {
        if (arr1.top() == arr2.top()) {
            arr1.pop();
            arr2.pop();
            cnt_inter++;
            cnt_union++;
        }
        else if (arr1.top()<arr2.top()) {
            arr1.pop();
            cnt_union++;
        }
        else {
            arr2.pop();
            cnt_union++;
        }
    }

    cnt_union += arr1.size() + arr2.size();

    return (cnt_union != 0) ? 65536 * cnt_inter / cnt_union : 65536;
}