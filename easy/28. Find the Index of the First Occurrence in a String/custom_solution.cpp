
class Solution {
public:
    int strStr(string haystack, string needle) {
        ssize_t index = -1;
        int coincidences = 0;
        for (size_t i = 0; i < haystack.length(); i++){
            size_t local_i = i;
            for (size_t j = 0; j < needle.length(); j++){
                if (coincidences == needle.length())
                      return index;
                else if (haystack[local_i] == needle[j]){
                    if (index == -1){
                        index = local_i;
                    }
                    local_i++;
                    coincidences++;
                }
                else{
                    index = -1;
                    coincidences = 0;
                    break;
                }
            }
        }
        if (coincidences == needle.length())
            return index;
        return -1;
    }
};
