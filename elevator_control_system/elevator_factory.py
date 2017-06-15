import abc


class ElevatorFactory(object):
    """
    Factory/Abstract base class for elevators
    https://pymotw.com/2/abc/
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def move_up(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def move_down(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def elevator_direction(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def elevator_status(self):
        raise NotImplementedError()
