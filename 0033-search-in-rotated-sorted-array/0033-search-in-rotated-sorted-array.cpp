class Solution {
public:
    int search(vector<int>& nums, int target) {
        int start = 0 ;
        int n = nums.size();
        int end = n - 1;

        while(start <= end ){
            int mid = start + (end - start)/2 ;

            if(nums[mid] == target ){
                return mid;
            }

            // check if left part is sorted
            if(nums[mid] >= nums[start]){
                if(target >= nums[start] && target < nums[mid]){
                    end = mid - 1 ; // move left on 1st / slope
                }
                else{
                    start = mid + 1; // move right in 1st / slope
                }
            }
            // check if right part is sorted 
            else{
                if(target > nums[mid] && target <= nums[end]){
                    start = mid + 1; // move right on 3rd / slope
                }
                else{
                    end = mid - 1; // move left on 3rd / slope
                }
            }
        }

        return -1 ;

    }
};