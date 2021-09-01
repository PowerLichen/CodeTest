//탐욕법
//큰 수 만들기

#include <string>
#include <vector>

using namespace std;

string solution(string number, int k) {
    
    vector<char> numset;
    int idx = 0;
    bool get_index = true;
    int nums[10] = { 0, };

    for (int i = 9; i >= 0 && k>0; i--) {
        if (get_index) {
            for (int j = 0; j < 10; j++) {
                nums[j] = -1;
            }
            for (int j = idx; j < number.size(); j++) {
                int digit = number[j] - '0';
                if (nums[digit] < 0)
                    nums[digit] = j-idx;
            }
            get_index = false;
        }
        if (nums[i] >= 0 && nums[i] <= k) {
            numset.push_back(i+'0');
            k -= nums[i];
            idx = nums[i] + idx + 1;
            get_index = true;
            i = 10;
        }
    }
    
    return string(numset.begin(), numset.end()-k) + number.substr(idx);
}