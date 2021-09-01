// 힙
// 더 맵게

#include <vector>
#include <set>

using namespace std;

int solution(vector<int> scoville, int K) {
    // C++의 멀티셋은 중복된 값을 오름차순으로 저장.
    // 우선순위 큐 처럼 사용
    multiset<int> sco_set(scoville.begin(), scoville.end());
    int num;
    for (int i = 0; sco_set.size() > 1; i++) {
        num = *sco_set.begin();
        num += *sco_set.erase(sco_set.begin()) * 2;
        sco_set.erase(sco_set.begin());
        sco_set.insert(num);
        if (*sco_set.begin() > K)
            return i+1;
    }
    return -1;
}