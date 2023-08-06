"""The Mimeo Iteration module.

It exports only one class:
    * MimeoIteration
        A class representing a single iteration in a Mimeo Template.
"""
import uuid
from typing import Union

from mimeo.context.exc import (InvalidSpecialFieldName,
                               InvalidSpecialFieldValue, SpecialFieldNotFound)


class MimeoIteration:
    """A class representing a single iteration in a Mimeo Template.

    Each iteration has its own id (an ordinal number in a context),
    a key being a unique value across all iterations, and
    it stores special fields that could be ingested in other fields.

    Attributes
    ----------
    id : int
        An ordinal number in a Mimeo Context
    key : str
        An UUID value unique across all templates

    Methods
    -------
    add_special_field(self, field_name: str, field_value: Union[str, int, bool])
        Put a special field entry to memory.
    get_special_field(self, field_name: str) -> Union[str, int, bool]
        Get a special field value from memory.
    """

    def __init__(self, identifier: int):
        """Initialize MimeoIteration class.

        Parameters
        ----------
        identifier : int
            An ordinal number in a Mimeo Context
        """
        self.id = identifier
        self.key = str(uuid.uuid4())
        self._special_fields = {}

    def add_special_field(self, field_name: str, field_value: Union[str, int, bool]):
        """Put a special field entry to memory.

        Parameters
        ----------
        field_name : str
            A special field name
        field_value : Union[str, int, bool]
            A special field value

        Raises
        ------
        InvalidSpecialFieldName
            If the special field name is not a string
        InvalidSpecialFieldValue
            If the special field value is dict or list
        """
        if not isinstance(field_name, str):
            raise InvalidSpecialFieldName()
        if isinstance(field_value, dict) or isinstance(field_value, list):
            raise InvalidSpecialFieldValue(field_value)

        self._special_fields[field_name] = field_value

    def get_special_field(self, field_name: str) -> Union[str, int, bool]:
        """Get a special field value from memory.

        Parameters
        ----------
        field_name : str
            A special field name

        Returns
        -------
        Union[str, int, bool]
            A special field value

        Raises
        ------
        SpecialFieldNotFound
            If the special field does not exist.
        """
        if field_name not in self._special_fields:
            raise SpecialFieldNotFound(field_name)

        return self._special_fields.get(field_name)
