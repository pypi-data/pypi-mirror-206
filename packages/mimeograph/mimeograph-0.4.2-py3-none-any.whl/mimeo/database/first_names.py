"""The First Names module.

It exports classes related to forenames CSV data:
    * FirstName
        DTO class representing a single row in forenames CSV data.
    * FirstNamesDB
        Class exposing READ operations on forenames CSV data.
"""
from typing import List

import pandas

from mimeo import tools
from mimeo.database.exc import InvalidIndex, InvalidSex


class FirstName:
    """DTO class representing a single row in forenames CSV data.

    Attributes
    ----------
    name : str
        A first name
    sex : str
        A sex value
    """

    def __init__(self, name: str, sex: str):
        """Initialize FirstName class.

        Parameters
        ----------
        name : str
            A first name
        sex : str
            A sex value
        """
        self.name = name
        self.sex = sex

    def __str__(self) -> str:
        """Stringify the FirstName instance.

        Returns
        -------
        str
            A stringified `dict` representation of the FirstName instance
        """
        return str({
            "name": self.name,
            "sex": self.sex
        })

    def __repr__(self) -> str:
        """Represent the FirstName instance.

        Returns
        -------
        str
            A python representation of the FirstName instance
        """
        return f"FirstName('{self.name}', '{self.sex}')"


class FirstNamesDB:
    """Class exposing READ operations on forenames CSV data.

    Attributes
    ----------
    NUM_OF_RECORDS : int
        A number of rows in forenames CSV data

    Methods
    -------
    get_first_names() -> List[FirstName]
        Get all first names.
    get_first_names_by_sex(sex: str) -> List[FirstName]
        Get first names for a specific sex.
    get_first_name_at(index: int) -> FirstName
        Get a first name at `index` position.
    """

    NUM_OF_RECORDS = 7455
    __SUPPORTED_SEX = ("M", "F")
    __FIRST_NAMES_DB = "forenames.csv"
    __FIRST_NAMES_DF = None
    __FIRST_NAMES = None
    __NAMES_FOR_SEX = {}

    def get_first_name_at(self, index: int) -> FirstName:
        """Get a first name at `index` position.

        Parameters
        ----------
        index : int
            A first name row index

        Returns
        -------
        FirstName
            A specific first name

        Raises
        ------
        InvalidIndex
            If the provided `index` is out of bounds
        """
        first_names = self.__get_first_names()
        try:
            return first_names[index]
        except IndexError:
            raise InvalidIndex(index, FirstNamesDB.NUM_OF_RECORDS-1)

    def get_first_names_by_sex(self, sex: str) -> List[FirstName]:
        """Get first names for a specific sex.

        Parameters
        ----------
        sex : str
            A sex value to filter first names

        Returns
        -------
        List[FirstName]
            List of first names filtered by sex

        Raises
        ------
        InvalidSex
            If the provided `sex` value is not supported
        """
        if sex in FirstNamesDB.__SUPPORTED_SEX:
            return self.__get_first_names_by_sex(sex).copy()
        else:
            raise InvalidSex(FirstNamesDB.__SUPPORTED_SEX)

    @classmethod
    def get_first_names(cls) -> List[FirstName]:
        """Get all first names.

        Returns
        -------
        List[FirstName]
            List of all first names
        """
        return cls.__get_first_names().copy()

    @classmethod
    def __get_first_names_by_sex(cls, sex: str) -> List[FirstName]:
        """Get first names for a specific sex from cache.

        The first names list for sex is initialized for the first time
        and cached in internal class attribute.

        Parameters
        ----------
        sex : str
            A sex value to filter first names

        Returns
        -------
        List[FirstName]
            List of first names filtered by sex
        """
        if sex not in cls.__NAMES_FOR_SEX:
            first_names = cls.__get_first_names()
            cls.__NAMES_FOR_SEX[sex] = list(filter(lambda first_name: first_name.sex == sex, first_names))
        return cls.__NAMES_FOR_SEX[sex]

    @classmethod
    def __get_first_names(cls) -> List[FirstName]:
        """Get all first names from cache.

        The first names list is initialized for the first time and
        cached in internal class attribute.

        Returns
        -------
        List[FirstName]
            List of all first names
        """
        if cls.__FIRST_NAMES is None:
            cls.__FIRST_NAMES = [FirstName(row.NAME, row.SEX)
                                 for row in cls.__get_first_names_df().itertuples()]
        return cls.__FIRST_NAMES

    @classmethod
    def __get_first_names_df(cls) -> pandas.DataFrame:
        """Load forenames CSV data and save in internal class attribute."""
        if cls.__FIRST_NAMES_DF is None:
            cls.__FIRST_NAMES_DF = pandas.read_csv(tools.get_resource(FirstNamesDB.__FIRST_NAMES_DB))
        return cls.__FIRST_NAMES_DF
