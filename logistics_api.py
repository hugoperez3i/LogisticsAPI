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

class ShipmentManager():

    # CONSTRUCTOR FOR THE CLASS

    def __init__(self) -> None:
        self.dict_shipments: dict[str,Shipment] = {}

    def _is_valid_string(self, string:str) -> bool:
        return len(string) != 0
    
    def _is_valid_weight(self, weight:float) -> bool:
        return weight > 0
    
    def _is_id_used(self, tracking_id:str) -> bool:
        return tracking_id in self.dict_shipments
    
    def create(self, tracking_id:str, destination:str, weight:float) -> bool:
        """Create a new shipment with the given information
        
        Will return True on shipment creation, False if any of the provided data is invalid,
        or if the given tracking_id is already used.
        """
        if( (not self._is_valid_string(tracking_id)) or (not self._is_valid_string(destination))): # Check for invalid strings
            return False
        
        if not self._is_valid_weight(weight): # Check taht weight is positive, non-zero
            return False
        
        if self._is_id_used(tracking_id): # Ensure that the id is free
            return False

        self.dict_shipments[tracking_id]=Shipment(tracking_id,destination,Status.PENDING,weight)
        return True
        
