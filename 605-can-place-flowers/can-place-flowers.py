class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            #check the current is empty
            if flowerbed[i] == 0:
                #check the left is empty
                empty_left_plot = (i == 0) or (flowerbed[i-1] == 0)
                empty_right_plot = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
                #check the right is empty 
                #if it is empty, plant it 
                if empty_left_plot and empty_right_plot:
                    flowerbed[i] = 1
                    count += 1
        return count >= n
