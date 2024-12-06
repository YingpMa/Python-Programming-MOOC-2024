
class Task:
    id = 1
    def __init__(self, description: str, programmer: str, workload: int):
        self.id = Task.id
        Task.id += 1
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.finished = False

    def is_finished(self):
        return self.finished
    
    def mark_finished(self):
        self.finished = True
        return self.finished
    
    def __str__(self):
        if self.finished:
            status = "FINISHED"
        else:
            status = "NOT FINISHED"
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {status}"

class OrderBook:
    def __init__(self):
        self.__all_orders = []
        self.__programmers = []

    def add_order(self, description: str, programmer: str, workload: int):
        order = Task(description, programmer, workload)
        self.__all_orders.append(order)
        if order.programmer not in self.__programmers:
            self.__programmers.append(order.programmer)

    def all_orders(self):
        return self.__all_orders
    
    def programmers(self):
        return self.__programmers
    
    def mark_finished(self, id: int):
        for order in self.__all_orders:
            if order.id == id:
                order.mark_finished()
                return True
        raise ValueError
 
    def finished_orders(self):
        finished = [order for order in self.__all_orders if order.finished]
        return finished
    
    def unfinished_orders(self):
        unfinished = [order for order in self.__all_orders if not order.finished]
        return unfinished

    def status_of_programmer(self, programmer: str):
        programmer_status = [0, 0, 0, 0]
        for order in self.finished_orders():
            if order.programmer == programmer:
                programmer_status[0] += 1
                programmer_status[2] += order.workload
        for order in self.unfinished_orders():
            if order.programmer == programmer:
                programmer_status[1] += 1
                programmer_status[3] += order.workload
        if programmer_status == [0, 0, 0, 0]:
            raise ValueError
        return tuple(programmer_status)

class OrderBookApplication:
    def __init__(self):
        self.__orderbook = OrderBook()

    def help(self):
        print("commands:")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer")

    def add_order(self):
        description = input("description: ")
        programmer_and_workload = input("programmer and workload estimate: ")
        try:
            parts = programmer_and_workload.split(" ")
            if len(parts) != 2:
                raise ValueError
            parts[1] = int(parts[1])
        except:
            print("erroneous input")
            return
        self.__orderbook.add_order(description, parts[0], int(parts[1]))
        print("added!")

    def list_finished_tasks(self):
        if self.__orderbook.finished_orders() == []:
            print("no finished tasks")
        else:
            for order in self.__orderbook.finished_orders():
                print(order)

    def list_unfinished_tasks(self):
        if self.__orderbook.unfinished_orders() == []:
            print("no unfinished tasks")
        else:
            for order in self.__orderbook.unfinished_orders():
                print(order)

    def mark_finished(self):
        try:
            id = int(input("id: "))
            if self.__orderbook.mark_finished(id):
                print("marked as finished")
            else:
                print("erroneous input")
        except:
            print("erroneous input")
            return
    
    def programmers(self):
        for programmer in self.__orderbook.programmers():
            print(programmer)

    def status_of_programmer(self):
        programmer = input("programmer: ")
        try:
            tasks = self.__orderbook.status_of_programmer(programmer)
            print(f"tasks: finished {tasks[0]} not finished {tasks[1]}, hours: done {tasks[2]} scheduled {tasks[3]}")
        except:
            print("erroneous input")

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_order()
            elif command == "2":
                self.list_finished_tasks()
            elif command == "3":
                self.list_unfinished_tasks()
            elif command == "4":
                self.mark_finished()
            elif command == "5":
                self.programmers()
            elif command == "6":
                self.status_of_programmer()
            else:
                self.help()

application = OrderBookApplication()
application.execute()