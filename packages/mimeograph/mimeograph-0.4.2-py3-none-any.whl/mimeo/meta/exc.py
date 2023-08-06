"""The Mimeo Meta Exceptions module.

It contains all custom exceptions related to useful abstract classes:
    * InstanceNotAlive
        A custom Exception class for using non-alive instance.
"""


class InstanceNotAlive(Exception):
    """A custom Exception class for using non-alive instance.

    Raised when using OnlyOneAlive class that is not alive.
    """

    def __init__(self):
        """Initialize InstanceNotAlive exception with details.

        Extends Exception constructor with a constant message.
        """
        super().__init__("The instance is not alive!")
