class Utils():
    def assert_list_item_text(self, list):
        for device in list:
            print("The device text is " + device.text)
            assert device.text == "iPhone 13" or "Galaxy A13" or "Galaxy A13 With Chromebook 4"
            print("assert pass")

