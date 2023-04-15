"""Abstract class for validating attributes"""
from abc import ABC, abstractmethod
class Attribute(ABC):
    """Abstract class for validating attributes"""

    @abstractmethod
    def validate(self, value):
        """method for validating a attribute"""


    #@abstractproperty
    @property
    def value(self):
        """method for getting a attribute"""
