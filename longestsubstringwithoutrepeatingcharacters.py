class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == None or s == '':
            return 0
        max_num = 0
        l = 0
        char_set = set()
        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l +=1
            char_set.add(s[r])
            max_num = max(r-l+1, max_num)
                
        return max_num
        
        
        ## OLD ATTEMPT SAM 2
        # sub=""
        # window = [] 
        # front_w = 0
        # back_w = 0

        # bound=(len(str)-1)

        # for i in range(bound): 
        #     front_w=i
        #     if (s[i] != s[i+1]): 
        #         back_w=i+1
        #         window = s[i:i+1]
        #         sub=window
        #     else: 
                

        
    ## OLD ATTEMPT SAM 
        # ret = ""
        # curr = s

        # i = 0 
        
        # if s == "" or s == None: 
        #     return 0 

        # for ch in s:
        #     if len(ret) > len(curr): 
        #         return len(ret)

        #     print (f'for char: {ch}')
        #     if ch not in ret: 
        #         ret += ch 
        #         i +=1 
        #         print (f'if ret: {ret}')
        #         # curr=s[i:]
        #     else: 
        #         curr = s[i:]
        #         s = curr 
        #         print(f'else ret: {ret}')
        #         ret = ""
        #         i=0

        # print (f'return ret: {ret}')
        # return len(ret)
        
