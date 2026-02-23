class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
      //map use karenge 
      unordered_map<int,int> mp; // map assign karenge
        for(int i = 0 ; i < nums.size(); i++){  //loop iterate karenge array ke all element me
            int need = target - nums[i];        // set target - nums[i] and search it in map 
            if(mp.count(need)){ // check weather it is available in map and retrun its index and i ie index of current element
                return{mp[need],i};
            }
            mp[nums[i]]=i; // if need is not available in map then insert it
        }  
        return{};
    }
};


