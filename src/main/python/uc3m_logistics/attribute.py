from abc import ABC, abstractmethod
class Attribute(ABC):

    def __init__(self,value):
        self.__value = self.validate(value)

    @abstractmethod
    def validate(self,value):
        pass
    @property
    @abstractmethod
    def value(self):
        pass