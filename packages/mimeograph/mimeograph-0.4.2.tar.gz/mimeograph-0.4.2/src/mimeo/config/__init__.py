"""The Mimeo Configuration package.

It contains the following modules:
* mimeo_config
    The Mimeo Configuration module
* exc
    The Mimeo Configuration Exceptions module

The Mimeo Configuration package exports a class representing
root Mimeo Configuration component:
* MimeoConfig
    A MimeoDTO class representing Mimeo Configuration

To use this package, simply import it:
    from mimeo.config import MimeoConfig
    from mimeo.config.exc import UnsupportedPropertyValue
"""
from .mimeo_config import MimeoConfig
