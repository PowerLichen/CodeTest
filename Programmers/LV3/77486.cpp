#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

vector<int> solution(vector<string> enroll, vector<string> referral, vector<string> seller, vector<int> amount) {
    vector<int> result(enroll.size(), 0);
    unordered_map<string, int> idx_data;

    //init name data
    idx_data["-"] = -1;
    for (int i = 0; i < enroll.size(); i++) {
        idx_data[enroll[i]] = i;
    }

    //sell data calc
    for (int i = 0; i < seller.size(); i++) {
        int money = amount[i] * 100;
        string seller_nm = seller[i];
        int seller_idx = idx_data[seller_nm];
        string referral_nm;

        while (seller_idx >= 0) {
            referral_nm = referral[seller_idx];
            int fees = money / 10;
            result[seller_idx] += money - fees;
            money = fees;
            if (money == 0)
                break;
            seller_nm = referral_nm;
            seller_idx = idx_data[seller_nm];
        }
    }

    return result;
}