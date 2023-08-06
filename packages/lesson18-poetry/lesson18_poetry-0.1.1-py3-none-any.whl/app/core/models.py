from abc import abstractmethod, ABC


class BaseModel(ABC):

    @abstractmethod
    def get(self, *args, **kwargs):
        pass

    @abstractmethod
    def create(self, *args, **kwargs):
        pass

    @abstractmethod
    def filter(self, *args, **kwargs):
        pass
