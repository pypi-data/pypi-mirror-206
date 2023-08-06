
import shutil
from os import path

import pytest

from mimeo import Mimeograph
from mimeo.config import MimeoConfig
from mimeo.context import MimeoContextManager


@pytest.fixture(autouse=True)
def teardown():
    yield
    # Teardown
    shutil.rmtree("test_mimeograph-dir")


def test_produce():
    config = {
        "output_details": {
            "direction": "file",
            "format": "xml",
            "indent": 4,
            "xml_declaration": True,
            "directory_path": "test_mimeograph-dir",
            "file_name": "output"
        },
        "_templates_": [
            {
                "count": 10,
                "model": {
                    "SomeEntity": {
                        "ChildNode1": 1,
                        "ChildNode2": "value-2",
                        "ChildNode3": True
                    }
                }
            }
        ]
    }
    mimeo_config = MimeoConfig(config)
    with MimeoContextManager(mimeo_config):
        mimeo = Mimeograph(mimeo_config)

        assert not path.exists("test_mimeograph-dir")
        mimeo.process()
        assert path.exists("test_mimeograph-dir")
        for i in range(1, 11):
            file_path = f"test_mimeograph-dir/output-{i}.xml"
            assert path.exists(file_path)

            with open(file_path, "r") as file_content:
                assert file_content.readline() == '<?xml version="1.0" encoding="utf-8"?>\n'
                assert file_content.readline() == '<SomeEntity>\n'
                assert file_content.readline() == '    <ChildNode1>1</ChildNode1>\n'
                assert file_content.readline() == '    <ChildNode2>value-2</ChildNode2>\n'
                assert file_content.readline() == '    <ChildNode3>true</ChildNode3>\n'
                assert file_content.readline() == '</SomeEntity>\n'




