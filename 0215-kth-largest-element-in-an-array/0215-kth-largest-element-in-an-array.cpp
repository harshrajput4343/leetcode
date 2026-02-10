#include <vector>
#include <queue>
using namespace std;


class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        // min heap
        priority_queue<int ,vector<int>, greater<int>> minHeap;

        //Insert first k element
        for (int i = 0 ; i < k ; i++){
            minHeap.push(nums[i]);
        }

        //check and process reamining element

        for(int i = k ; i < nums.size(); i++){
            if(nums[i] > minHeap.top()){
                minHeap.pop();
                minHeap.push(nums[i]);
            }
        }
        return minHeap.top();
    }
};

