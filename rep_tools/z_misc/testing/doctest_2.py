import doctest
from collections import deque


class TicketQueue(object):
    def __init__(self):
        self.deque = deque()

    def add_person(self, name):
        """
        >>> queue = TicketQueue()
        >>> queue.add_person("Jack")
        Jack has been added to the queue
        """
        self.deque.append(name)
        print(f"{name} has been added to the queue")

    def service_person(self):
        """
        >>> queue = TicketQueue()
        >>> queue.add_person("Jack")
        Jack has been added to the queue
        >>> queue.service_person()
        Jack has been serviced
        """
        name = self.deque.popleft()
        print(f"{name} has been serviced")

    def bypass_queue(self, name):
        """
        >>> queue = TicketQueue()
        >>> queue.add_person("Jack")
        Jack has been added to the queue
        >>> queue.bypass_queue("Jill")
        Jill has bypassed the queue
        """
        self.deque.appendleft(name)
        print(f"{name} has bypassed the queue")


doctest.testmod(name="TicketQueue", verbose=True)
