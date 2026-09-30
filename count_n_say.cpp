class Solution {
public:
    string countAndSay(int n) {
        if (n <= 0) return "";

        string base = "1";

        for (int i = 1; i < n; ++i) {
            string next = "";
            int count = 1;

            for (int j = 1; j < base.size(); ++j) {
                if (base[j] == base[j - 1]) {
                    count++;
                } else {
                    next += to_string(count) + base[j - 1];
                    count = 1;
                }
            }

            next += to_string(count) + base.back();
            base = next;
        }

        return base;
    }
};