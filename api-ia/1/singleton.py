class Borg:
    _shared_data = {}
    def __init__(self) -> None:
        self.__dict__ = self._shared_data
        

class SingleTon(Borg):
    def __init__(self, **kwargs):
        Borg.__init__(self)
        self._shared_data.update(kwargs)
        
    def __str__(self):
        return str(self._shared_data)
    

x = SingleTon(HTTP = "Hyper text transfer protocols")

print(x)
y = SingleTon(SNP = "Simple netword")
print(y)