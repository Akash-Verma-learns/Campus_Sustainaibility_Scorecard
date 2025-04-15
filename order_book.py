class Order:
    def __init__(self, user, side, quantity, price):
        self.user = user
        self.side = side  # 'buy' or 'sell'
        self.quantity = quantity
        self.price = price

class OrderBook:
    def __init__(self):
        self.buys = []
        self.sells = []

    def add_order(self, order):
        if order.side == 'buy':
            self.buys.append(order)
            self.buys.sort(key=lambda x: -x.price)
        else:
            self.sells.append(order)
            self.sells.sort(key=lambda x: x.price)

    def match_orders(self):
        trades = []
        while self.buys and self.sells and self.buys[0].price >= self.sells[0].price:
            buy = self.buys[0]
            sell = self.sells[0]
            quantity = min(buy.quantity, sell.quantity)
            trades.append((buy.user, sell.user, quantity, sell.price))
            buy.quantity -= quantity
            sell.quantity -= quantity
            if buy.quantity == 0: self.buys.pop(0)
            if sell.quantity == 0: self.sells.pop(0)
        return trades
