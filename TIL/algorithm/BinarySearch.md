# BinarySearch
LC-35. Search Insert Position

```
class Solution {
public:
    int swap_mum (vector<int>& nums, int mid,int pin){
        return pin = mid;
    }

    int loop(vector<int>& nums, int quick_pin,int slow_pin,int target){
        //排除沒有
        if (nums.empty()) return 0;
        //排除最小
        if (nums[slow_pin]>target){
            return 0;
        }
        //排除最大
        if (nums[quick_pin] < target){
            return quick_pin +1 ;
        }

        //要保證掃完最後一個數字，所以不能用 !=
        while(slow_pin <= quick_pin){
            //這邊不能寫 快指針+慢指針/2  ，要防止大數報錯
            int mid = (quick_pin + (quick_pin - slow_pin)) / 2 ; 

            if(nums[mid] == target){
                return mid;
            }
            else if(nums[mid] < target){
                slow_pin = mid + 1;

            }
            else {
                                quick_pin = mid -1;

            }
        }
        return slow_pin;

    }

    int searchInsert(vector<int>& nums, int target) {
        int quick_pin = nums.size() - 1; 
        int slow_pin = 0 ;
        int rseult;

        rseult = loop(nums,quick_pin ,slow_pin ,target);
        return rseult;
    }
};
```