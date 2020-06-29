import abc


class AbstractPLayer(abc.ABC):
    def __init__(self):
        pass

    @abc.abstractmethod
    def ask_card(self):
        pass


class Player(AbstractPLayer):
    pass


class Dealer(AbstractPLayer):
    pass


class Bot(AbstractPLayer):
    pass