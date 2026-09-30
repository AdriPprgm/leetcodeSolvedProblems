class Solution {
public:
    int hammingWeight(int n) {
        if (n / 2 == 0){
            return n;
        }
        else{
            return hammingWeight(n / 2) + hammingWeight(n % 2);
        }
    }
};