import softest


class Utils(softest.TestCase):
    def assert_in_list_item_text(self, list, value):
        for device in list:
            print("The device text is " + device.text)
            self.soft_assert(self.assertIn, value, device.text)
            if value in device.text:
                print("assert pass")
            else:
                print("assert failed")
        self.assert_all()