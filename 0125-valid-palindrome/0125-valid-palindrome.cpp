class Solution {
public:
    bool isPalindrome(string s) {
        int l = 0 , r = s.size() - 1 ;

        while( l < r){

            // skip non-alphanumeric from left
            while ( l < r &&  !isalnum(s[l])) l++;


            // skip non-alphanumeric from right
            while( l < r && !isalnum(s[r])) r--;

             // compare after normalizing case
            if(tolower(s[l]) != tolower(s[r])){
                return false;
            }
            l++;
            r--;

        }
        return true;
    }
};