from typing import List

def reverseString(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    s[:] = s[::-1]