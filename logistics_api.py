# Language: Python 3.13.2

from enum import Enum
from dataclasses import dataclass

class Status(Enum):
    PENDING= "Pending"
    IN_TRANSIT= "InTransit"
    DELIVERED= "Delivered"    

@dataclass
class Shipment():
    """Internal data storage class for each shipment"""
    tracking_id: str
    destination: str
    status: Status
    weight: float