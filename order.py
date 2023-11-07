class Order:
    def __init__(self, orderCustomer, address: str = None):
        self.madeBy = orderCustomer.getName()
        self.destination = orderCustomer.getAddress() if not address else address
        
    
        

