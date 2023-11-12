import random
import pickle
import time
import os

from linear_data_structures import Queue
from order import Order
from people import Customer, Courier
from graph import Graph, Vertex
from pathfinder import getShortestDistance

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
        
        self.orderQueue = Queue()
        self.courierQueue = Queue()

        try:
            with open('../data/couriers.dat','rb') as f:
                self.list_of_couriers = pickle.load(f)
                print('> Last saved Couriers data has been loaded.')
                f.close()
                self.num_of_couriers = len(self.list_of_couriers)
                
            for courier in self.list_of_couriers:
                self.courierQueue.enqueue(courier)
                
        except FileNotFoundError:
            self.list_of_couriers = []
            self.num_of_couriers = 0

        
        try:
            with open('../data/customers.dat','rb') as f:
                self.list_of_customers = pickle.load(f)
                print('> Last saved Customers data has been loaded.')
                f.close()
                self.num_of_customers = len(self.list_of_customers)
        except FileNotFoundError:
            self.list_of_customers = []
            self.num_of_customers = 0
                    
        
        self.vertices = []
        
        try:
            with open('../data/sample_graph.map','rb') as f:
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
                'command': 'Add Order',
                'function': self.addOrder
            },
            8: {
                'command': 'Delete Order',
                'function': self.deleteOrder
            },
            9: {
                'command': 'Generate Sample Couriers \t[For testing only]',
                'function': self.generateCouriers
            },
            10: {
                'command': 'Generate Sample Customers \t[For testing only]',
                'function': self.generateCustomers
            },
            11: {
                'command': 'Generate Orders \t\t\t[For testing only]',
                'function': self.generateOrderQueue
            },
            12: {
                'command': 'View All Couriers',
                'function': self.viewAllCouriers
            },
            13:{
                'command': 'View All Customers',
                'function': self.viewAllCustomers
            },
            14: {
                 'command': 'View Order Queue',
                 'function': self.viewOrders
            },
            15: {
                'command': 'View Graph Adjacency List',
                'function': self.viewMap
            },
            16: {
                'command': 'Generate Dispatching Schedule',
                'function': self.generateDispatchingSchedule
            },
            17: {
                'command': 'View Dispatching Schedules',
                'function': self.viewDispatchingSchedules
            },
            18:{
                'command': 'Save All Changes',
                'function': self.saveAllChanges
            },
            0: {
                'command': 'Exit'
            }
        }
        
        print('-' * (len(title_str) + (2*side_spaces)))
     
    def addCourier(self) -> None:
        try:
            name = input('Enter Name: ')
            courier_id = 'D' + str(max([int(c.getID()[1:]) for c in self.list_of_couriers]) + 1)
            gender = input('Enter Gender: ')
            age = int(input('Enter Age: '))
            max_order_capacity = int(input('Enter max carrying capacity: '))
            
            newCourier = Courier(courier_id, name, gender, age, max_order_capacity)
            self.list_of_couriers.append(newCourier)
            self.num_of_couriers += 1
            
            print(f"[{newCourier.toString()}] added.")
                
        except ValueError:
            print('> ERROR: Invalid input.')
            
        print('-' * (len(title_str) + (2*side_spaces)))
        return
    
    def deleteCourier(self) -> None:
        courier_id = input('Enter Courier ID to be deleted: ')
        for courier in self.list_of_couriers:
            if str(courier.getID()) == str(courier_id):
                self.list_of_couriers.remove(courier)
                self.courierQueue._items.remove(courier)
                
                print(f"{courier} deleted.")
                print('-' * (len(title_str) + (2*side_spaces)))
                return
            
        print('ERROR: Courier ID does not exist!')
        print('-' * (len(title_str) + (2*side_spaces)))
        return
    
    def modifyCourierDetails(self) -> None:
        courier_id = input('Enter Courier ID: ')
        success = False
        for courier in self.list_of_couriers:
            if courier.getID() == courier_id:
                edit = input(f"Enter attribute to edit (Name, Gender, Age, Capacity) for [Courier ID: {courier_id}]: ").lower()
                if edit == 'name':
                    new_name = input('Enter Name: ')
                    courier.name = new_name
                elif edit == 'gender':
                    new_gender = input('Enter Gender: ')
                    courier.gender = new_gender
                elif edit == 'age':
                    try:
                        new_age = int(input('Enter Age: '))
                        courier.age = new_age
                    except ValueError:
                        print('? ERROR: Age must be an interger.')
                elif edit == 'capacity':
                    try:
                        new_cap = int(input('Enter Max Carrying Capacity: '))
                        courier.max_order_capacity = new_cap
                    except ValueError:
                        print('> ERROR: Max Carrying Capacity must be an interger.')
                success = True
                print(f"{courier_id} modified.")
                break
        if not success:
            print('ERROR: Courier ID does not exist.')
            
        print('-' * (len(title_str) + (2*side_spaces)))
        return
    
    def generateCouriers(self) -> None:
        try:
            num_of_couriers = int(input('Enter number of couriers to generate: '))
        except ValueError:
            print('> ERROR: Input is not an integer!')
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
            exec(f"""courier{i} = Courier(id='D{i}', name='D{i}_name', gender='{genders[rnd_gender_idx]}', age={rnd_age}, max_order_capacity={rnd_order_capacity})""")
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
                print(courier.toString())
                
        print('-' * (len(title_str) + (2*side_spaces)))
        return

    def addCustomer(self) -> None:

        name = input('Enter Name: ')
        customer_id = 'C' + str(max([int(c.getID()[1:]) for c in self.list_of_customers]) + 1)
        gender = input('Enter Gender: ')
        address = input('Enter Address (Vertex Name): ')
        
        for vertex in self.currentMap.vertices.values():
            if vertex.name == address:
                address_vertex = vertex
                
                new_customer = Customer(customer_id, name, gender, address_vertex)
                self.list_of_customers.append(new_customer)
                self.num_of_customers += 1
                print(f"[{new_customer.toString()}] added.")
                print('-' * (len(title_str) + (2*side_spaces)))
                return
        
        print('ERROR: Invalid Address.')
        print('-' * (len(title_str) + (2*side_spaces)))
        return
    
    def deleteCustomer(self) -> None:
        customer_id = input('Enter Customer ID to be deleted: ')
        for customer in self.list_of_customers:
            if str(customer.getID()) == str(customer_id):
                self.list_of_customers.remove(customer)
                
                self.orderQueue._items = [order for order in self.orderQueue._items if order.orderer != customer_id]
                print(f"[{customer.toString()}] deleted.")
                print('-' * (len(title_str) + (2*side_spaces)))
                return
        
        print('> ERROR: Courier does not exist.')
        return

    def modifyCustomerDetails(self) -> None:
        customer_id = input('Enter Customer ID: ')
        success = False
        for customer in self.list_of_customers:
            if customer.getID() == customer_id:
                edit = input(f"Enter attribute to edit (Name, Gender, Address) for [Customer ID: {customer_id}]: ").lower()
                if edit == 'name':
                    new_name = input('Enter Name: ')
                    customer.name = new_name
                elif edit == 'gender':
                    new_gender = input('Enter Gender: ')
                    customer.gender = new_gender
                elif edit == 'address':
                    new_address = input('Enter Address (Vertex Name): ')
                    for vertex in self.currentMap.vertices.values():
                        if vertex.name == new_address:
                            customer.address = vertex
                    if customer.getAddress != vertex.name:
                        print('> ERROR: Vertex {new_address} does not exist.')
                        break
               
                success = True
                print(f"{customer_id} modified.")
                break
            
        if not success:
            print('ERROR: Customer ID does not exist.')
            
        print('-' * (len(title_str) + (2*side_spaces)))
        return
    
    def addOrder(self) -> None:
        customer_check = input('Is customer a member (Y/N)?: ').lower()
        order_id = max([x.id for x in self.orderQueue._items]) + 1 if self.orderQueue.getQueueSize() > 0 else 1
        if customer_check == 'y':
            customer_check_passed = False
            customer_id = input('Input customer ID: ').upper()
            for customer in self.list_of_customers:
                if customer.getID() == customer_id:
                    self.orderQueue.enqueue(Order(order_id, customer))
                    print(f"Order #{order_id} added for Customer ID: {customer_id}.")
                    customer_check_passed = True
                    break
            
            if not customer_check_passed:
                print(f"> ERROR: Customer ID {customer_id} does not exist.")
                print('-' * (len(title_str) + (2*side_spaces)))
                return
            
        else:
            vertex_check_passed = False
            #try:
            address = input('Enter Address (Vertex Name): ').upper()
            for vertex in self.currentMap.vertices.values():
                if vertex.name == address:
                    vertex_check_passed = True
                    break
            if not vertex_check_passed:
                print(f"> ERROR: Vertex {address} does not exist.")
                print('-' * (len(title_str) + (2*side_spaces)))
                return
                    
            customer_id = 'Guest'
            customer = Customer(id = customer_id, name = 'Guest', gender = 'NA', address = vertex)
            self.orderQueue.enqueue(Order(order_id, customer))
            print(f"Order #{order_id} added for Guest to deliver to Address: Vertex {vertex.name}.")

            

        print('-' * (len(title_str) + (2*side_spaces)))
        return
    
    def deleteOrder(self) -> None:
        order_id = int(input('Enter Order ID: '))
        
        try:
            for order in self.orderQueue._items:
                if order.id == order_id:
                    self.orderQueue._items.remove(order)
                    print(f"Order #{order.id} removed from queue.")
                    break
            
            print('> ERROR: Order ID does not exist!')
        except ValueError:
            print('> ERROR: Input is not an integer!')
            
        print('-' * (len(title_str) + (2*side_spaces)))
        return
    
    def generateCustomers(self) -> None:
        try:
            num_of_customers = int(input('Enter number of customers to generate: '))
        except ValueError:
            print('> ERROR: Input is not an integer!')
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
            exec(f"""customer{i} = Customer(id='C{i}', name='C{i}_name', gender='{genders[rnd_gender_idx]}', address=rnd_vertex)""")
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

    def generateOrderQueue(self) -> None:
        try:
            if self.orderQueue.getQueueSize() > 0:
                replace_check = input('Append to or Replace existing orders (Append/Replace)?: ').lower()
                if replace_check not in ['replace','append']:
                    raise ValueError
        
                if replace_check == 'replace':
                    self.orderQueue.empty()
                    
                max_order_id = self.orderQueue._items[0].id
                
            else:
                max_order_id = 0
                
            queue_size = int(input('Enter Order Queue size: '))
            for i in range(queue_size):
                rnd_choice = random.choice(self.list_of_customers)
                order_id = max_order_id + 1 + i
                order = Order(order_id = order_id, orderCustomer = rnd_choice)
                self.orderQueue.enqueue(order)
                print(f"[#{order_id}: Customer ID - {rnd_choice.getID()}, Address: Vertex {rnd_choice.getAddress().name}] added to queue")
         
        except ValueError:
            print('> ERROR: Invalid Input!')
            
        print('-' * (len(title_str) + (2*side_spaces)))
        return
      
    def viewOrders(self) -> None:
        if len(self.orderQueue._items) == 0:
            print('Order queue is empty!')
        else:
            for order in self.orderQueue._items[::-1]:
                print(f"#{order.id}: Customer ID - {order.orderer}, Address - Vertex {order.destination.name}")
                
            
        print('-' * (len(title_str) + (2*side_spaces)))
        return
        
    def viewMap(self) -> None:
        for v in self.currentMap.vertices.values():
            print(v.toString())
            
        print('-' * (len(title_str) + (2*side_spaces)))
        return
        
    
    def saveAllChanges(self) -> None:
        with open('../data/customers.dat','wb+') as f:
            pickle.dump(self.list_of_customers, f)
            print('> Customer data saved in /data/customers.dat.')
            f.close()
            
        with open('../data/couriers.dat','wb+') as f:
            pickle.dump(self.list_of_couriers, f)
            print('> Courier data saved in /data/couriers.dat.')
            f.close()
        
        print('-' * (len(title_str) + (2*side_spaces)))
        return
    
    def generateDispatchingSchedule(self) -> None:
        if self.orderQueue.getQueueSize() == 0:
            print('Order Queue is empty!')
        else:
            to_print = ''
            dispatch_id = 1
            while self.orderQueue.getQueueSize() > 0:
                courier = self.courierQueue.dequeue()
                
                orders = []
                for i in range(courier.getMaxOrderCapacity()):
                    order = self.orderQueue.dequeue()
                                        
                    if not order: break
                    orders.append(order)
                
                delivery_vertices_names = [x.destination.name for x in orders]
                
                
                to_print += f"Dispatch #{dispatch_id}:\n"
                to_print += f"> Assigned Courier: {courier.getID()} ({courier.getName()}); Max Order Capacity: {courier.getMaxOrderCapacity()}\n"
                to_print += '> Dispatch Address (Vertex Name)\n:'
                for order in orders:
                    to_print += f"  - Order #{order.id}; Address: Vertex {order.destination.name}\n"
                
                
                shortest_path, total_distance = getShortestDistance(graph = self.currentMap, vertices = delivery_vertices_names)
                
                to_print += f"> {' -> '.join([x + str('*') if x in delivery_vertices_names else x for x in shortest_path])}\n"
                to_print += f"> Total Distance: {total_distance}\n"
                to_print += '\n'
                self.courierQueue.enqueue(courier)
                dispatch_id += 1
        
            print(to_print)
            curr_time = time.ctime().replace(' ','_').replace(':','')
            with open(f"../data/schedules/{curr_time}.txt",'w+') as f:
                f.write(to_print)
                print(f"Dispatch Schedule saved to /data/schedules/{curr_time}.txt")
                f.close()
        
        print('-' * (len(title_str) + (2*side_spaces)))
        return
    
    def viewDispatchingSchedules(self):
        schedules_path = os.path.dirname(os.path.abspath(__file__ + "/../")) + "\data\schedules"
        schedules = {id: filename for id, filename in enumerate(os.listdir(schedules_path), 1)}

        if len(schedules) == 0: 
            print('/data/schedules directory is empty.')
            print('-' * (len(title_str) + (2*side_spaces)))
            return
        
        for s in schedules.items():
            print(f"{s[0]}: {s[1]}")
        
        print()
        selection = int(input('Enter the schedule number to view: '))
        print('-' * (len(title_str) + (2*side_spaces)))
        try:
            with open(f"../data/schedules/{schedules[selection]}",'r') as f:
                contents = f.read()
                print(contents)
                f.close()
        except KeyError:
            print('ERROR: Invalid Input.')
            
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
        try:
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
                
        except ValueError:
            print('-' * (len(title_str) + (2*side_spaces)))
            print('ERROR: Invalid Input. Only input the numbers from the list above.')
            print('-' * (len(title_str) + (2*side_spaces)))
            