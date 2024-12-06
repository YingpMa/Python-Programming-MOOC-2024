# Write your solution here:
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

            

if __name__ == "__main__":
    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Adele", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)
    orders.add_order("program the next facebook", "Eric", 1000)

    orders.mark_finished(1)
    orders.mark_finished(2)

    status = orders.status_of_programmer("Adele")
    print(status)