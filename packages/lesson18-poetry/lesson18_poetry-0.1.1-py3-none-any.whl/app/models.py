from .core.models import BaseModel


class User(BaseModel):
    name: str
    password: str

    def get(self, *args, **kwargs):
        pass

    def create(self, *args, **kwargs):
        pass

    def filter(self, *args, **kwargs):
        pass
