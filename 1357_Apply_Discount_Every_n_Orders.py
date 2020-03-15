class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.target = n
        self.count = 0
        self.discount = discount
        self.products = {}
        for i, p in zip(products, prices):
            self.products[i] = p
        

    def getBill(self, product: List[int], amount: List[int]) -> float:
        res = 0
        for p, n in zip(product, amount):
            res += self.products[p] * n
        self.count += 1
        if self.count % self.target == 0:
            res = res - (self.discount * res) / 100
        return res


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)
