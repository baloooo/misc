from elevator_factory import ElevatorFactory


class Elevator(ElevatorFactory):
    """
    Concrete class for ElevatorFactory ABC
    """
    def __init__(self, elevator_id):
        self.elevator_id = elevator_id

    def move_up(self):
        pass

    def move_down(self):
        pass

    def elevator_direction(self):
        pass

    def elevator_status(self):
        pass
