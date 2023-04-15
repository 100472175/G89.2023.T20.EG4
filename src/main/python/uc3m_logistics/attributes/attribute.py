from abc import ABC, abstractmethod
class Attribute(ABC):

    @abstractmethod
    def validate(self, value):
        pass

    #@abstractproperty
    @property
    def value(self):
        pass