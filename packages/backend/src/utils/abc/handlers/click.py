# === Core ===
import ipaddress

# === Utils ===
from pydantic import BaseModel
from utils.abc.handlers.base import WrapperModel

# === Database ===
from pymongo.collection import Collection
from utils.mongo.Client import MongoClient

# === Types ===
from typing import ClassVar


class ClickMeta(WrapperModel):
    __collection__: ClassVar[Collection] = MongoClient.clicks
    
    
    class RootModel(BaseModel):
        count: int = 0
        
        class Config:
            extra = "allow"
            
    @property
    def root_callback(self) -> RootModel:
        """
        Returns a root pydantic model holding a count type
        """
        
        response = self.__collection__.find_one({"_id": "root"})
        if response is None:
            response = {"_id": "root", "count": 0}
            self.__collection__.insert_one(response)
                
        return self.RootModel(**response)
    

class Clicks:
    
    def __init__(self) -> None:
        pass
    
    def addCount(self, amount: int = 1, host: str | None = None) -> None:
        """
        Updates the counter within the root document. Also if the host variable is a valid ipv4 address, iterates that as well
        """
        self.discover.update({"_id": "root"}, "$inc", {"count": amount})
        
        try:
            # If valid ip address, continue
            ipaddress.IPv4Address(host)        
            
            # Insert ip count as well
            if self.discover.exists(_id=host):
                self.discover.update({"_id": host}, "$inc", {"count": amount})
            else:
                self.discover.__collection__.insert_one({"_id": host, "count": amount})
                
        except ipaddress.AddressValueError:
            pass
    
    @property
    def root(self) -> ClickMeta.RootModel:
        """
        Returns the root object in the clicks database, which holds information
        such as the total amount of clicks
        """
        return ClickMeta().root_callback
    
    @property
    def discover(self) -> ClickMeta:
        """
        Returns a clicks discoverable object, able to locate a user
        who clicked or sort the top ip clicks
        """
        return ClickMeta()
    
clicks = Clicks()

