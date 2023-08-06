import unittest
import glob
import time
from django import test
from pathlib import Path
from . import xml
from . import items
from . import views


class TestParse(test.SimpleTestCase):
    def test_parse(self):
        """All xml presets must be valid for import"""
        parent = Path(__file__).parent
        xml_files = glob.glob(str(parent.joinpath('tests', '*', '*.xml')))
        xml_files.sort()
        for filename in xml_files:
            print('Start parse file:', filename)
            start_1 = time.time_ns()

            el = xml.XmlElement.parse(filename)

            start_2 = time.time_ns()

            items.Packet.parse_xml(el)

            end = time.time_ns()
            xml_time = (start_2 - start_1) / 1_000_000_000
            parse_time = (end - start_2) / 1_000_000_000
            print('End:', 'xml_time:', xml_time, 'parse_time:', parse_time)


class TestImport(unittest.TestCase):

    # Change `import_section` default value to switch test case
    def test_import(self, import_section='04*'):
        """
        All import presets should be valid for import catalogue or offer
        Change `import_section` default value to switch import presets
        """

        parent = Path(__file__).parent
        if not import_section:
            import_section = '??_import*'
        xml_files = glob.glob(str(parent.joinpath('tests', import_section, '*.xml')))
        xml_files.sort()

        for filename in xml_files:

            # Important: Set test import folder before creating `pv`
            buf_bp = items.FileRef.base_path
            items.FileRef.base_path = Path(filename).parent
            pv = views.ProtocolView()

            print('Start import file:', filename)
            start_1 = time.time_ns()

            x = xml.XmlElement.parse(filename)
            pack = items.Packet.parse_xml(x)

            start_2 = time.time_ns()

            pv.import_pack(pack)

            end = time.time_ns()
            xml_time = (start_2 - start_1) / 1_000_000_000
            parse_time = (end - start_2) / 1_000_000_000
            print('End:', 'parse_time:', xml_time, 'import_time:', parse_time)

            # Restore
            items.FileRef.base_path = buf_bp
