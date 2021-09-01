// 짝지어 제거하기

#include <string>
#include <stack>
using namespace std;

int solution(string s)
{
    stack<char> stk;
    for (char c : s) {
        if (stk.empty()) {
            stk.push(c);
        }
        else {
            if (stk.top() == c)
                stk.pop();
            else
                stk.push(c);
        }
    }

    if (stk.empty())
        return 1;
    return 0;
}