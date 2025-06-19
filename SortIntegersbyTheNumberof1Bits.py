class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort(key = lambda num: (num.bit_count(), num))
        return arr 

## OLD SAM ATTEMPT
        # num_ones={} 
        # oblist=[]

        # for num in arr: 
        #     bv=bin(num)[2:] 
        #     ob=str(bv).count('1')
        #     oblist.append(ob)

        # li = [bin(num) for num in arr]
        # print(li)
        # print( num_ones )
        # print(oblist)
