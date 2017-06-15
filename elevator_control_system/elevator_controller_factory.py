import abc


class ElevatorControllerFactory(object):
    """
    ABC for generating elevator classes
    """
    __metaclass__ = abc.ABCMeta

    def pick_up(self, pick_up_floor):
        raise NotImplementedError

    def destination(self, elevator_id, destination_floor):
        raise NotImplementedError

    def scheduling_request_to_elevator(self):
        raise NotImplementedError
