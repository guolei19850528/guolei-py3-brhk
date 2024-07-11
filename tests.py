import unittest

from guolei_py3_brhk.speaker import Api as SpeakerApi


class MyTestCase(unittest.TestCase):
    def test_something(self):
        speaker_api = SpeakerApi(
            base_url="https://speaker.17laimai.cn",
            token="",
            id="",
            version=1
        )
        state = speaker_api.notify(message="测试推送通知")
        if state:
            print("发送成功")
        self.assertTrue(state, "test failed")  # add assertion here


if __name__ == '__main__':
    unittest.main()
