class ProductOfNumbers:

    def __init__(self):
        #initialize the opbject with empty stream 
        self.prefix_product = [1]
        self.size = 0

    def add(self, num: int) -> None:
        #append the integer num to the stream
        #if the num is 0, reset the cumulative products since multiplication with 0 invalidates previous products 
        if num == 0:
            self.prefix_product = [1]
            self.size = 0 
        else:
            #append the cumulative product of the current number with the last product
            self.prefix_product.append(self.prefix_product[self.size] * num)
            self.size += 1

    def getProduct(self, k: int) -> int:
        #return the product of the last k numbers in the current list. You can assume that always the current list has at least k numbers 
        if k > self.size:
            return 0
        return (
            self.prefix_product[self.size] // self.prefix_product[self.size - k]
        )
            


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)