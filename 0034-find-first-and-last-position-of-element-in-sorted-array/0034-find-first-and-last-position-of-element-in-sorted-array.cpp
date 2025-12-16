class Solution {
public:
    int firstOcc(vector<int>& arr, int n, int key) {
        int s = 0, e = n - 1, ans = -1;
        while (s <= e) {
            int mid = s + (e - s) / 2;
            if (arr[mid] == key) {
                ans = mid;
                e = mid - 1;
            } else if (key > arr[mid]) {
                s = mid + 1;
            } else {
                e = mid - 1;
            }
        }
        return ans;
    }

    int lastOcc(vector<int>& arr, int n, int key) {
        int s = 0, e = n - 1, ans = -1;
        while (s <= e) {
            int mid = s + (e - s) / 2;
            if (arr[mid] == key) {
                ans = mid;
                s = mid + 1;
            } else if (key > arr[mid]) {
                s = mid + 1;
            } else {
                e = mid - 1;
            }
        }
        return ans;
    }

    vector<int> searchRange(vector<int>& nums, int target) {
        int n = nums.size();
        return {
            firstOcc(nums, n, target),
            lastOcc(nums, n, target)
        };
    }
};
