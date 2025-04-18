# Language: Python 3.13.2

from enum import Enum

class Status(Enum):
    PENDING= "Pending"
    IN_TRANSIT= "InTransit"
    DELIVERED= "Delivered"    