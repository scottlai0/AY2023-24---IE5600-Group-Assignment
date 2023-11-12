class Order:
    def __init__(self, order_id, orderCustomer, address: str = None):
        self.id = order_id
        self.orderer = orderCustomer.getID()
        self.destination = orderCustomer.getAddress() if not address else address
        