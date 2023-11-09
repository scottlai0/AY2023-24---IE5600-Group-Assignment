from linear_data_structures import Queue
from order import Order
from people import Customer, Courier
from graph import Graph, Vertex
import random
import pickle

title_str = 'PyDispatcher CLI'
side_spaces = 30
title_formatted = f"{' ' * side_spaces}{title_str}{' ' * side_spaces}"
genders = ['M','F']

class Dispatcher:
    num_of_couriers: int
    list_of_couriers: list
    
    num_of_customers: int
    list_of_customers: list
    
    vertices: list
    currentMap: Graph
    
    orderQueue: Queue
    courierQueue: Queue
    
    def __init__(self):
        print('> Intializing...')
        
        try:
            with open('./saved_data/couriers.dat','rb') as f:
                self.list_of_couriers = pickle.load(f)
                print('> Last saved Couriers data has been loaded.')
                f.close()
                self.num_of_couriers = len(self.list_of_couriers)
        except FileNotFoundError:
            self.list_of_couriers = []
            self.num_of_couriers = 0

        
        try:
            with open('./saved_data/customers.dat','rb') as f:
                self.list_of_customers = pickle.load(f)
                print('> Last saved Customers data has been loaded.')
                f.close()
                self.num_of_customers = len(self.list_of_customers)
        except FileNotFoundError:
            self.list_of_customers = []
            self.num_of_customers = 0
                    
        self.orderQueue = Queue()
        self.courierQueue = Queue()
        
        self.vertices = []
        
        try:
            with open('./saved_data/sample_graph.map','rb') as f:
                self.currentMap = pickle.load(f)
                print('> Last saved Graph data has been loaded.')
                f.close()
                
        except FileNotFoundError:
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
                'command': 'Add Customer',
                'function': self.addCustomer
            },
            5: {
                'command': 'Delete Customer',
                'function': self.deleteCustomer
            },
            6: {
                'command': 'Modify Customer Details',
                'function': self.modifyCustomerDetails
            },
            7: {
                'command': 'Generate Sample Couriers',
                'function': self.generateCouriers
            },
            8: {
                'command': 'Generate Sample Customers',
                'function': self.generateCustomers
            },
            9: {
                'command': 'Generate Orders',
                'function': self.generateOrderQueue
            },
            10: {
                'command': 'View All Couriers',
                'function': self.viewAllCouriers
            },
            11:{
                'command': 'View All Customers',
                'function': self.viewAllCustomers
            },
            12: {
                 'command': 'View Order Queue',
                 'function': None
            },
            13: {
                'command': 'View Graph Adjacency List',
                'function': self.viewMap
            },
            14: {
                'command': 'View Dispatching Schedule',
                'function': None
            },
            15:{
                'command': 'Save All Changes',
                'function': self.saveAllChanges
            },
            0: {
                'command': 'Exit'
            }
        }
        
        print('-' * (len(title_str) + (2*side_spaces)))
     
    def addCourier(self, name: str, gender: str, age: int, max_order_capacity: int) -> None:
        if len(self.list_of_couriers) == 0 or name not in [x.getID() for x in self.list_of_couriers]:
            newCourier = Courier(name, gender, age, max_order_capacity)
            self.list_of_couriers.append(newCourier)
            self.num_of_couriers += 1
        else:
            print('ERROR: Courier name already exists. Please use a different name.')
        return
    
    def deleteCourier(self) -> None:
        courier_name = input('Enter Courier ID to be deleted: ')
        for courier in self.list_of_couriers:
            if courier.getID() == courier_name:
                self.list_of_couriers.remove(courier)                
                return
        
        print('ERROR: Courier does not exist.')
        return
    
    def modifyCourierDetails(self) -> None:
        courer = input('> Enter Courier ID ')
        
    
    def generateCouriers(self) -> None:
        try:
            num_of_couriers = int(input('Enter number of couriers to generate: '))
        except ValueError:
            print('ERROR: Input is not an integer!')
            return
        
        if self.num_of_couriers > 0:
            cfm = input('This will overwrite existing courier data. Continue (Y/N)? ').lower()
            
            if cfm == 'N': return
            
        self.num_of_couriers = num_of_couriers
        self.list_of_couriers = []
        
        for i in range(1, num_of_couriers+1):
            rnd_gender_idx = random.randint(0,1)
            rnd_age = random.randrange(18, 50)
            rnd_order_capacity = random.randrange(2,5)
            print(f"Courier {i} created:")
            exec(f"""courier{i} = Courier(id='D{i}', gender='{genders[rnd_gender_idx]}', age={rnd_age}, max_order_capacity={rnd_order_capacity})""")
            exec(f"""print(courier{i}.toString())""")
            exec(f"self.list_of_couriers.append(courier{i})")
            print() 
            
        print('-' * (len(title_str) + (2*side_spaces)))
        return
    
    def viewAllCouriers(self) -> None:
        if self.num_of_couriers == 0:
            print('> NO DATA FOUND.')
        else:            
            for courier in self.list_of_couriers:
                print(courier.toString(),'\n')
                
        print('-' * (len(title_str) + (2*side_spaces)))
        return

    def addCustomer(self, name: str, gender: str, address: Vertex) -> None:
        if len(self.list_of_customers) == 0 or name not in [x.getID() for x in self.list_of_customers]:
            newCustomer = Customer(name, gender, address)
            self.list_of_customers.append(newCustomer)
            self.num_of_customers += 1
        else:
            print('ERROR: Customer name already exists. Please use a different name.')
        return
    
    def deleteCustomer(self, customer_name: str) -> None:
        for customer in self.list_of_customers:
            if customer.getID() == customer_name:
                self.list_of_customers.remove(customer)                
                return
        
        print('ERROR: Courier does not exist.')
        return

    def modifyCustomerDetails(self) -> None:
        return
    
    def generateCustomers(self) -> None:
        try:
            num_of_customers = int(input('Enter number of customers to generate: '))
        except ValueError:
            print('ERROR: Input is not an integer!')
            return
        
        if self.num_of_customers > 0:
            cfm = input('This will overwrite existing customer data. Continue (Y/N)? ').lower()
            if cfm == 'N': return
        
        self.num_of_customers = num_of_customers
        self.list_of_customers = []
        
        all_vertices = list(self.currentMap.vertices.values())[1:]
        
        self.num_of_customers = num_of_customers
        for i in range(1, num_of_customers+1):
            rnd_gender_idx = random.randint(0,1)
            rnd_vertex = random.choice(all_vertices)
            print(f"Customer {i} created:")
            exec(f"""customer{i} = Customer(id='C{i}', gender='{genders[rnd_gender_idx]}', address=rnd_vertex)""")
            exec(f"""print(customer{i}.toString())""")
            exec(f"""self.list_of_customers.append(customer{i})""")
            print()
            
        print('-' * (len(title_str) + (2*side_spaces)))
        return

    def viewAllCustomers(self) -> None:
        if self.num_of_customers == 0:
            print('> NO DATA FOUND.')
        else:            
            for customer in self.list_of_customers:
                print(customer.toString())

        print('-' * (len(title_str) + (2*side_spaces)))
        return

    def generateOrderQueue(self):
        try:
            queue_size = int(input('> Enter Order Queue size: '))
            for i in range(queue_size):
                rnd_choice = random.choice(self.list_of_customers)
                self.orderQueue.enqueue(rnd_choice)
                print(f" {i+1}: {rnd_choice.getID()} - Vertex {rnd_choice.getAddress().name} added to queue")
        except ValueError:
            print('ERROR: Input is not an integer!')
            
        print('-' * (len(title_str) + (2*side_spaces)))
        return
    
    def viewMap(self) -> None:
        for v in self.currentMap.vertices.values():
            print(v.toString())
            
        print('-' * (len(title_str) + (2*side_spaces)))
        return
        
    
    def saveAllChanges(self) -> None:
        with open('./saved_data/customers.dat','wb+') as f:
            pickle.dump(self.list_of_customers, f)
            print('> Customer data saved in /saved_data/customers.dat.')
            f.close()
            
        with open('./saved_data/couriers.dat','wb+') as f:
            pickle.dump(self.list_of_couriers, f)
            print('> Courier data saved in /saved_data/couriers.dat.')
            f.close()
        
        print('-' * (len(title_str) + (2*side_spaces)))
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