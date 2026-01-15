class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();

        vector<int>answer(n);

        //prefix pass
        answer[0] = 1;
    
        for (int i = 1 ;i < n ; i++){
            answer[i]= answer[i-1] * nums[ i - 1];
        }

        //suffix pass
        int suffix = 1 ;
        for (int i = n-1 ; i>= 0 ; i--){
            answer[i]*= suffix;
            suffix *= nums[i];
        }
        return answer;
    }
};