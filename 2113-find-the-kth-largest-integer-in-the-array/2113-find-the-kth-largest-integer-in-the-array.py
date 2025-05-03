class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        st=[]
        for i in nums:
            st.append(int(i))
        st.sort()
        return str(st[-k])