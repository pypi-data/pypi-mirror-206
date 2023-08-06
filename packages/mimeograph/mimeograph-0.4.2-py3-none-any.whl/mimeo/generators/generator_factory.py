"""The Mimeo Generator Factory module.

It exports only one class:
    * GeneratorFactory
        A Factory class instantiating a Generator based on Mimeo Config.
"""
from mimeo.config.exc import UnsupportedPropertyValue
from mimeo.config.mimeo_config import MimeoConfig
from mimeo.generators import Generator, XMLGenerator


class GeneratorFactory:
    """A Factory class instantiating a Generator based on Mimeo Config.

    Implementation of the Generator class depends on the output format
    configured.

    Attributes
    ----------
    XML
        The 'xml' output format

    Methods
    -------
    get_generator(mimeo_config: MimeoConfig) -> Generator
        Initialize a Generator based on the Mimeo Output Format.
    """

    XML = MimeoConfig.OUTPUT_FORMAT_XML

    @staticmethod
    def get_generator(mimeo_config: MimeoConfig) -> Generator:
        """Initialize a Generator based on the Mimeo Output Format.

        Parameters
        ----------
        mimeo_config : MimeoConfig
            A Mimeo Configuration

        Returns
        -------
        Generator
            A Generator's implementation instance

        Raises
        ------
        UnsupportedPropertyValue
            If the output format is not supported
        """
        output_format = mimeo_config.output_details.format
        if output_format == GeneratorFactory.XML:
            return XMLGenerator(mimeo_config)
        else:
            raise UnsupportedPropertyValue(MimeoConfig.OUTPUT_DETAILS_FORMAT_KEY,
                                           output_format,
                                           MimeoConfig.SUPPORTED_OUTPUT_FORMATS)
