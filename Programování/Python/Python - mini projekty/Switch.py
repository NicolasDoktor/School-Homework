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

    @staticmethod
    def isValidMac(mac: str) -> bool:
        return bool(re.match(r'^([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}$', mac))

    @property
    def dmac(self) -> str: return self._dmac
    @dmac.setter
    def dmac(self, val: str):
        if not self.isValidMac(val): raise ValueError("Neplatný formát MAC.")
        self._dmac = val; self._recalculateFcs()

    @property
    def smac(self) -> str: return self._smac
    @smac.setter
    def smac(self, val: str):
        if not self.isValidMac(val): raise ValueError("Neplatný formát MAC.")
        self._smac = val; self._recalculateFcs()

    @property
    def type(self) -> int: return self._type
    @type.setter
    def type(self, val: int):
        self._type = val; self._recalculateFcs()

    @property
    def payload(self) -> str: return super().payload
    @payload.setter
    def payload(self, val: str):
        self._payload = val
        self._recalculateFcs()

    @property
    def fcs(self) -> int: return self._fcs

    def calculateFcs(self) -> int:
        return sum(ord(c) for c in f"{self._dmac}{self._smac}{self._type}{self.payload}")

    def _recalculateFcs(self):
        self._fcs = self.calculateFcs()

    def isValid(self) -> bool:
        return self._fcs == self.calculateFcs()

    def __str__(self) -> str:
        return f"[EthFrame] SRC: {self._smac} DST: {self._dmac} DATA: {self.payload}"

    def corruptData(self):
        self._payload = "ERROR_CORRUPTED"
        self._fcs = 999999999
