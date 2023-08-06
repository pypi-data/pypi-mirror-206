from pydantic import BaseModel
from typing import Literal, get_args

class MetadataGroup(BaseModel):
    _atom = False

    def __hash__(self):
        return hash((type(self),) + tuple(self.__dict__.values()))


class FreeText(str):
    _help_description = "Free text"
    _atom = True

# Intended only for use inside bia_models
# value wrapped in a literal required by pydantic,
#   can not be built in the model definition by wrapping a variable
_version_l = Literal["1.5"]

# Inded for external use
# string argument of the literal above,
#   intended for use outside 
_version = get_args(_version_l)[0]