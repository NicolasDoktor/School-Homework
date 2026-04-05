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

class EthFrame(PDU):
    "Konkrétní model Ethernetového rámce"
    def __init__(self, dmac: str, smac: str, type: int, payload: str, fcs: int = None):
        if not (self.isValidMac(dmac) and self.isValidMac(smac)):
            raise ValueError("Neplatný formát MAC adresy.")
            
        super().__init__(payload)
        self._dmac = dmac
        self._smac = smac
        self._type = type
        self._fcs = fcs if fcs is not None else self.calculateFcs()

