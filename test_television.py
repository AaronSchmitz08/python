import unittest
from television import Television


class testTelevision(unittest.TestCase):
    def testPower(self):
        tv1 = Television()
        self.assertEqual(tv1.__str__(), "Power = False, Channel = 0, Volume = 0")
        tv1.power()
        self.assertEqual(tv1.__str__(),"Power = True, Channel = 0, Volume = 0")
        tv1.power()
        self.assertEqual(tv1.__str__(), "Power = False, Channel = 0, Volume = 0")

    def testMute(self):
        tv1 = Television()
        tv1.power()
        tv1.volume_up()
        self.assertEqual(tv1.__str__(), "Power = True, Channel = 0, Volume = 1")
        tv1.mute()
        self.assertEqual(tv1.__str__(), "Power = True, Channel = 0, Volume = 0")
        tv1.mute()
        self.assertEqual(tv1.__str__(), "Power = True, Channel = 0, Volume = 1")
        tv1.power()
        tv1.mute()
        self.assertEqual(tv1.__str__(), "Power = False, Channel = 0, Volume = 1")
        tv1.power()
        self.assertEqual(tv1.__str__(), "Power = True, Channel = 0, Volume = 1")
        tv1.mute()
        tv1.volume_up()
        self.assertEqual(tv1.__str__(), "Power = True, Channel = 0, Volume = 2")

    def testVolumeUp(self):
        tv1 = Television()
        tv1.volume_up()
        self.assertEqual(tv1.__str__(), "Power = False, Channel = 0, Volume = 0")
        tv1.power()
        tv1.volume_up()
        self.assertEqual(tv1.__str__(), "Power = True, Channel = 0, Volume = 1")
        tv1.volume_up()
        tv1.volume_up()
        self.assertEqual(tv1.__str__(), "Power = True, Channel = 0, Volume = 2")
        tv1.mute()
        tv1.volume_up()
        self.assertEqual(tv1.__str__(), "Power = True, Channel = 0, Volume = 2")

    def testVolumeDown(self):
        tv1 = Television()
        tv1.power()
        tv1.volume_up()
        tv1.volume_up()
        tv1.volume_down()
        self.assertEqual(tv1.__str__(), "Power = True, Channel = 0, Volume = 1")
        tv1.volume_down()
        tv1.volume_down()
        self.assertEqual(tv1.__str__(), "Power = True, Channel = 0, Volume = 0")
        tv1.volume_up()
        tv1.mute()
        tv1.volume_down()
        self.assertEqual(tv1.__str__(), "Power = True, Channel = 0, Volume = 0")
        tv1.volume_up()
        tv1.power()
        tv1.volume_down()
        self.assertEqual(tv1.__str__(), "Power = False, Channel = 0, Volume = 1")
        tv1.power()

    def testChannelUp(self):
        tv1 = Television()
        tv1.channel_up()
        self.assertEqual(tv1.__str__(), "Power = False, Channel = 0, Volume = 0")
        tv1.power()
        tv1.channel_up()
        self.assertEqual(tv1.__str__(), "Power = True, Channel = 1, Volume = 0")
        tv1.channel_up()
        tv1.channel_up()
        tv1.channel_up()
        self.assertEqual(tv1.__str__(), "Power = True, Channel = 0, Volume = 0")

    def testChannelDown(self):
        tv1 = Television()
        tv1.channel_down()
        self.assertEqual(tv1.__str__(), "Power = False, Channel = 0, Volume = 0")
        tv1.power()
        tv1.channel_down()
        self.assertEqual(tv1.__str__(), "Power = True, Channel = 3, Volume = 0")
        tv1.channel_down()
        tv1.channel_down()
        tv1.channel_down()
        self.assertEqual(tv1.__str__(), "Power = True, Channel = 0, Volume = 0")


if __name__ == "__main__":
    unittest.main()