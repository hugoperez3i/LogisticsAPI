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

    # VALIDATION METHODS FOR INTERNAL CHECKS

    def _is_valid_string(self, string:str) -> bool:
        return len(string) != 0
    
    def _is_valid_weight(self, weight:float) -> bool:
        return weight > 0
    
    def _is_id_used(self, tracking_id:str) -> bool:
        return tracking_id in self.dict_shipments
    
    def _is_valid_status(self, new_status:Status) -> bool:
        return isinstance(new_status, Status)
    
    # CLASS METHODS THAT IMPLEMENT FUNCTIONALITY
    
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
        
    def get(self, tracking_id:str) -> Shipment | None:
        """Retrieves a shipment by the given tracking id

        Returns a shipment object correspondign to the given tracking ID,
        or None if the given ID is invalid or there's no associated shipment
        """
        if not self._is_valid_string(tracking_id): # Check for invalid strings
            return None
        
        if not self._is_id_used(tracking_id): # Return None if the ID isn't used
            return None
        
        return self.dict_shipments[tracking_id]
    
    def update_status(self, tracking_id:str, new_status:Status) -> bool:
        """Updates the status of a shipment
        
        Enforces that the given status is a member of the Status enum.
        <br>Returns True on successful update of the status, False if any of the given paramenters is invalid
        """
        if not self._is_valid_status(new_status): # Enforce status enum usage
            return False
        
        shipment = self.get(tracking_id) # Uses get to obtain the shipment to modify
        if shipment is None: 
            return False # Exit if no valid shipment was retrieved
        
        shipment.status=new_status
        return True
    
