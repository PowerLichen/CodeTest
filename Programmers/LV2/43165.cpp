// DFS/BFS
// 타겟 넘버

#include <string>
#include <vector>

using namespace std;

int ans=0;
int t;

void t_num(vector<int>& numbers, int size, int num){
    if (size < 0) {
        if (num == t)
            ans++;
        return;
    }

    t_num(numbers, size - 1, num + numbers[size]);
    t_num(numbers, size - 1, num - numbers[size]);
    return;
}

int solution(vector<int> numbers, int target) {
    t = target;
    t_num(numbers, numbers.size()-1, 0);
    return ans;
}

//다른 풀이

int solution_other(vector<int> numbers, int target) {
    int answer = 0;
    int size = 1 << numbers.size();

    for(int i = 1 ; i < size ; i++){
        int temp = 0;
        for(int j = 0 ; j < numbers.size() ; j++)
        {  
            if(i &(1 << j)){
                temp -= numbers[j];
            }
            else temp += numbers[j];
        }
        if(temp == target) answer++;
    }
    return answer;
}