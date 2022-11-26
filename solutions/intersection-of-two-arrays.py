# https://leetcode.com/problems/intersection-of-two-arrays/submissions/

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set1.intersection(nums2))

        # return list(set(nums1) & set(nums2))

# function intersections(l1, l2) {
#     l1.sort((a, b) => a - b) // assume sorted
#     l2.sort((a, b) => a - b) // assume sorted
#     const intersections = []
#     let l = 0, r = 0;
#     while ((l2[l] && l1[r]) !== undefined) {
#        const left = l1[r], right = l2[l];
#         if (right === left) {
#             intersections.push(right)
#             while (left === l1[r]) r++;
#             while (right === l2[l]) l++;
#             continue;
#         }
#         if (right > left) while (left === l1[r]) r++;
#          else while (right === l2[l]) l++;
        
#     }
#     return intersections;
# }