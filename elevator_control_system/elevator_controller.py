import ElevatorControllerFactory
from elevator import Elevator

import heapq


class ElevatorController(ElevatorControllerFactory):
    """
    Controller for an elevator
    """
    MAX_ELEVATORS = 16
    num_of_elevators = 0
    num_of_floors = 0
    elevator_list = []
    pick_up_locations = []

    def __init__(self, num_of_elevators, num_of_floors):
        # All elevators start from lobby at first floor.
        self.currrent_floor = 1
        self.num_of_elevators = (
            num_of_elevators if num_of_elevators < self.MAX_ELEVATORS else
            self.MAX_ELEVATORS)
        self.num_of_floors = num_of_floors
        self.__initialize_elevators()
        # Requests from floors will be added by Central Elevator controller
        # also. This is heapq as we need sorted min from current floor as
        # we are moving in one direction and new tasks are being added.
        self.request_queue = []
        self.pick_up_locations = get_linked_list()

    def __initialize_elevators(self):
        for elevator_id in xrange(1, self.num_of_elevators+1):
            self.elevators.append(Elevator(elevator_id))

    def get_elevators(self):
        return self.elevator_list

    def pick_up(self, pick_up_floor):
        self.pick_up_locations.append(pick_up_floor)

    def next_destination(self):
        return heapq.heappop(self.request_queue)

    def add_destination(self):
        """
        adds destination to request queue
        """
        pass

    def move_up(self):
        self.current_floor += 1

    def move_down(self):
        self.current_floor -= 1

    def get_elevator_direction(self):
        pass

    def get_elevator_status(self):
        pass
