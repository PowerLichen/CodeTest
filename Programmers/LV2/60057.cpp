// KAKAO BLIND 2020
// 문자열 압축

#include <string>

using namespace std;

int compress(string& s, int d) {
    int len = 0;
    int n=1;
    string temp = "";
    for (int i = 0; i < s.length(); i += d) {
        string target = s.substr(i, d);
        if (temp == target) {
            n++;
        }
        else {
            len += temp.length();
            if (n > 1)
                len += to_string(n).length();
            n = 1;
            temp = target;
        }
    }

    len += temp.length();
    if (n > 1)
        len += to_string(n).length();

    return len;
}

int solution(string s) {
    int answer = s.length();
    int len;
    for (int i = 1; i < s.size(); i++) {
        len = compress(s, i);
        if (len < answer)
            answer = len;
    }
    return answer;
}