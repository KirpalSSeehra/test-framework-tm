class Utils:

    def assert_list_item_text(self, list, value):
        for device in list:
            print("The device text is " + device.text)
            assert device.text == value
            print("assert pass")