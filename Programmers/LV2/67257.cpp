//2020 카카오 인턴십
//수식 최대화

#include <string>
#include <vector>

using namespace std;

void find_calc(vector<long long>& nums, vector<char>& opcode, int d) {
    char op_char[3] = { '+','-', '*' };
    for (int i = 0; i < opcode.size(); i++) {
        if (opcode[i] == op_char[d]) {
            long long result = 0;
            long long num1 = nums[i];
            long long num2 = nums[i + 1];
            //연산
            switch (d) {
            case 0:
                result = num1 + num2;
                break;
            case 1:
                result = num1 - num2;
                break;
            case 2:
                result = num1 * num2;
                break;
            }
            //배열 변환
            nums[i] = result;
            nums.erase(nums.begin() + i + 1);
            opcode.erase(opcode.begin() + i);
            i--;
        }
    }
}

long long solution(string expression) {
    long long answer = 0;
    //연산자 순서
    int order[6][3] = {
        {0,1,2},
        {0,2,1},
        {1,0,2},
        {1,2,0},
        {2,0,1},
        {2,1,0}
    };
    vector<long long> nums;
    vector<char> opcode;
    long long temp = 0;
    //숫자, 연산자 초기화
    for (char ch : expression) {
        if (ch == '+' || ch == '-' || ch == '*') {
            nums.push_back(temp);
            temp = 0;
            opcode.push_back(ch);
        }
        else {
            temp *= 10;
            temp += ch - '0';
        }
    }
    nums.push_back(temp);

    // 계산    
    for (int i = 0; i < 6; i++) {
        vector<long long> t_nums(nums);
        vector<char> t_opcode(opcode);
        for (int j = 0; j < 3; j++) {            
            find_calc(t_nums, t_opcode, order[i][j]);
        }

        if (answer < abs(t_nums[0]))
            answer = abs(t_nums[0]);
        
    }
    return answer;
}