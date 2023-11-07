from linear_data_structures import Queue
from order import Order
from people import Customer, Courier
from graph import Graph, Vertex
import random

title_str = 'PyDispatcher CLI'
side_spaces = 30
title_formatted = f"{' ' * side_spaces}{title_str}{' ' * side_spaces}"
genders = ['M','F']

class Dispatcher:
    num_of_couriers: int
    list_of_couriers: list
    
    num_of_customers: int
    list_of_customers: list
    
    currentMap: Graph
    
    orderQueue: Queue
    courierQueue: Queue
    
    def __init__(self):
        self.num_of_couriers = 0
        self.num_of_customers = 0
        
        self.list_of_customers = []
        self.list_of_couriers = []
        
        self.orderQueue = Queue()
        self.courierQueue = Queue()
        
        self.currentMap = Graph()
        
        self.commands = {
            1: {
                'command': 'Add Courier',
                'function': self.addCourier
            }, 
            2: {
                'command': 'Delete Courier',
                'function': self.deleteCourier
            },
            3: {
                'command': 'Modify Courier Details',
                'function': self.modifyCourierDetails
            },
            4: {
                'command': 'Generate Sample Couriers',
                'function': self.generateCouriers
            },
            5: {
                'command': 'Add Customer',
                'function': self.addCustomer
            },
            6: {
                'command': 'Delete Customer',
                'function': self.deleteCustomer
            },
            7: {
                'command': 'Modify Customer Details',
                'function': self.modifyCustomerDetails
            },
            8: {
                'command': 'Generate Sample Customers',
                'function': self.generateCouriers
            },
            9: {
                'command': 'View Order Queue',
                'function': None
            },
            10: {
                 'command': 'Generate Orders',
                 'function': None
            },
            11: {
                'command': 'View Area of Coverage (Map)',
                'function': self.viewMap
            },
            12: {
                'command': 'View Dispatching Schedule',
                'function': None
            },
            0: {
                'command': 'Exit'
            }
        }
     
    def addCourier(self, name: str, gender: str, age: int, max_order_capacity: int) -> None:
        if len(self.list_of_couriers) == 0 or name not in [x.getName() for x in self.list_of_couriers]:
            newCourier = Courier(name, gender, age, max_order_capacity)
            self.list_of_couriers.append(newCourier)
            self.num_of_couriers += 1
        else:
            print('ERROR: Courier name already exists. Please use a different name.')
        return
    
    def deleteCourier(self, courier_name: str) -> None:
        for courier in self.list_of_couriers:
            if courier.getName() == courier_name:
                self.list_of_couriers.remove(courier)                
                return
        
        print('ERROR: Courier does not exist.')
        return
    
    def modifyCourierDetails(self) -> None:
        return
        
    
    def generateCouriers(self, num_of_couriers: int) -> None:
        if self.num_of_couriers > 0:
            cfm = input('This will overwrite existing courier data. Continue (Y/N)?').lower()
            
            if cfm == 'N': return
            
        self.num_of_couriers = num_of_couriers
        
        for i in range(1, num_of_couriers+1):
            rnd_gender_idx = random.randint(0,1)
            rnd_age = random.randrange(18, 50)
            rnd_order_capacity = random.randrange(2,5)
            print(f"Courier {i} created:")
            exec(f"""courier{i} = Courier(name='D{i}', gender='{genders[rnd_gender_idx]}', age={rnd_age}, max_order_capacity={rnd_order_capacity})""")
            exec(f"""print(courier{i}.toString())""")
            exec(f"self.list_of_couriers.append(courier{i})")
            print() 
        return


    def addCustomer(self, name: str, gender: str, address: Vertex) -> None:
        if len(self.list_of_customers) == 0 or name not in [x.getName() for x in self.list_of_customers]:
            newCustomer = Customer(name, gender, address)
            self.list_of_customers.append(newCustomer)
            self.num_of_customers += 1
        else:
            print('ERROR: Customer name already exists. Please use a different name.')
        return
    
    def deleteCustomer(self, customer_name: str) -> None:
        for customer in self.list_of_customers:
            if customer.getName() == customer_name:
                self.list_of_customers.remove(customer)                
                return
        
        print('ERROR: Courier does not exist.')
        return

    def modifyCustomerDetails(self) -> None:
        return
    
    def generateCustomers(self, num_of_customers):
        if self.num_of_customers > 0:
            cfm = input('This will overwrite existing customer data. Continue (Y/N)?').lower()
            if cfm == 'N': return
            
        self.num_of_customers = num_of_customers
        for i in range(1, num_of_customers+1):
            rnd_gender_idx = random.randint(0,1)
            print(f"Customer {i} created:")
            exec(f"""customer{i} = Customer(name='C{i}', gender='{genders[rnd_gender_idx]}', address=None)""")
            exec(f"""print(customer{i}.toString())""")
            exec(f"""list_of_customers.append(customer{i})""")
            print()
    
    def generateOrderQueue(self, queue_size: int):
        for i in range(queue_size):
            rnd_choice = random.choice(self.list_of_customers)
            self.orderQueue.enqueue(rnd_choice)
            print(f" {i+1}: {rnd_choice.getName()} - {rnd_choice.getAddress().name} added to queue")
    
    def viewMap(self) -> None:
        return
        
if __name__ == "__main__":
    # Title
    print('=' * len(title_formatted))
    print(title_formatted)
    print('=' * len(title_formatted))
    

    # Set seed for generation purposes
    random.seed(42)
    
    # Dispatcher instance
    dp = Dispatcher()
           
    while True:
        cmds = {x: dp.commands[x]['command'] for x in dp.commands}
        for k, v in zip(cmds.keys(), cmds.values()):
            print(f"{k}: {v}")
            
        keys = list(cmds.keys())
      
        cmd = int(input('> Input command number from the list above: '))
        print('-' * (len(title_str) + (2*side_spaces)))

        if cmd not in keys: 
            raise ValueError           
        
        if cmd == 0: 
            print('Exiting...')
            break
        
        else:
            print(f">> {dp.commands[cmd]['command']}")
            data = dp.commands[cmd]['function']()