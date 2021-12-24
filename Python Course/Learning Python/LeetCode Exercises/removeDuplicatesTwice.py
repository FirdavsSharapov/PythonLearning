def removeMostDuplicates(nums):    
        i = 1
        count = 1
        while i < len(nums):    
            if nums[i] == nums[i - 1]:
                count += 1
                if count > 2:
                    nums.pop(i)
                    i-= 1
            else:
                count = 1
            i += 1
        return nums

nums = [0,0,1,1,1,1,2,3,3,3,3,3,3]
print (removeMostDuplicates(nums))



def sun_angle(time):
   hours = int(time[:2]) + int(time[3:]) / 60
   if (hours < 6) or (hours > 18):
       return "I don't see the sun!"
   else:
       return (hours - 6)/12 * 180
