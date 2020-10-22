
import pandas as pd
import numpy as np
import matplotlib.pyplot as pl
import yfinance as yf # access to the market


def findMaxConsecutiveOnes(nums) -> int:
    final_result = 0
    result = 0
    for x in nums:
        if x == 1:
            result += 1
        else:
            if final_result < result:
                final_result = result
            result = 0
            
    return final_result

 def duplicateZeros(self, arr: List[int]) -> None:
     array_len = len(arr)
     for x in range(array_len):
         if arr[x] == 0:
             for y in 

test = [0,1]

print(findMaxConsecutiveOnes(test))
