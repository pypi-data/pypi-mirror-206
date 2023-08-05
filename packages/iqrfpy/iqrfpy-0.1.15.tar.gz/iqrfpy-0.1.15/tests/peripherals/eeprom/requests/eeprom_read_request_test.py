import unittest
from parameterized import parameterized
from iqrfpy.peripherals.eeprom.requests.read import ReadRequest


class ReadRequestTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.dpa = b'\x05\x00\x03\x00\xff\xff\x0a\x05'
        self.json = {
            'mType': 'iqrfEmbedEeprom_Read',
            'data': {
                'msgId': 'readTest',
                'req': {
                    'nAdr': 5,
                    'hwpId': 65535,
                    'param': {
                        'address': 10,
                        'length': 5
                    }
                },
                'returnVerbose': True
            }
        }

    @parameterized.expand([
        [5, 10, 5, b'\x05\x00\x03\x00\xff\xff\x0a\x05'],
        [0, 5, 22, b'\x00\x00\x03\x00\xff\xff\x05\x16'],
    ])
    def test_to_dpa(self, nadr: int, address: int, length: int, expected):
        request = ReadRequest(nadr=nadr, address=address, length=length)
        self.assertEqual(
            request.to_dpa(),
            expected
        )

    @parameterized.expand([
        [5, 10, 5],
        [0, 5, 22],
    ])
    def test_to_json(self, nadr: int, address: int, length: int):
        request = ReadRequest(nadr=nadr, address=address, length=length, msgid='readTest')
        self.json['data']['req']['nAdr'] = nadr
        self.json['data']['req']['param']['address'] = address
        self.json['data']['req']['param']['length'] = length
        self.assertEqual(
            request.to_json(),
            self.json
        )
