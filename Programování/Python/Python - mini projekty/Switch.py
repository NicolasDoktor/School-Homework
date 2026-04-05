from abc import ABC, abstractmethod
import re

class PDU(ABC):
    "Abstraktní třída PDU"
    def __init__(self, payload: str):
        self._payload = payload
        
    @property
    def payload(self) -> str:
        return self._payload
        
    @payload.setter
    def payload(self, val: str):
        self._payload = val
        
    @abstractmethod
    def isValid(self) -> bool:
        pass


