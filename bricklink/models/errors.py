from .base import BaseModel

class Error(BaseModel):

    def __init__(self,
        message=None,
        description=None,
        code=None
    ):

        self.message = message
        self.description = description
        self.code = code