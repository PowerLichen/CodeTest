// 괄호 변환

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(string p) {
    if (p.size() == 0)
        return "";
    string u, v;
    int count = 0;
    int len=0;
    //p를 u,v로 나누기
    for (char c : p) {
        if (c == '(')
            count++;
        else
            count--;
        len++;
        if (count == 0) {
            u = p.substr(0, len);
            v = p.substr(len);
            break;
        }
    }
    //u에 대한 작업 수행
    for (char c : u) {
        if (c == '(')
            count++;
        else
            count--;
        if (count < 0) {
            string temp = u.substr(1, u.size() - 2);
            for (int i = 0; i < temp.size(); i++) {
                if (temp[i] == '(') temp[i] = ')';
                else temp[i] = '(';
            }
            return "(" + solution(v) + ")" + temp;
        }
    }
    return u + solution(v);
}