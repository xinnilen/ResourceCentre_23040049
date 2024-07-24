from inventory.inventory import Inventory

 ############### Test view camera ######################
class Test_US_04:

    def test_view_empty_camera_list(self):
        test_inventory = Inventory()

        tested_text = test_inventory.getAvailableCamera()
        
        actual_text = "{:<10}{:<30}{:<10}{:<12}{:<10}\n".format(
            "AssetTag", "Description", "Available", "Due Date", "Zoom")
        actual_text += "There is no camera to display."
        assert tested_text == actual_text

    def test_view_camera(self):
        test_inventory = Inventory()
        result = test_inventory.addCamera("C001", "Test camera 1", 5)
        result = test_inventory.addCamera("C002", "Test camera 2", 10)

        tested_text = test_inventory.getAvailableCamera()

        actual_text = "{:<10}{:<30}{:<10}{:<12}{:<10}\n".format(
            "AssetTag", "Description", "Available", "Due Date", "Zoom")
        actual_text += "{:<10}{:<30}{:<10}{:<12}{:<10}\n".format(
            "C001", "Test camera 1", "Yes", "", 5)
        actual_text += "{:<10}{:<30}{:<10}{:<12}{:<10}\n".format(
            "C002", "Test camera 2", "Yes", "", 10)
        assert tested_text == actual_text

    def test_view_camera_only_available(self):
        test_inventory = Inventory()
        result = test_inventory.addCamera("C001", "Test camera 1", 5)
        result = test_inventory.addCamera("C002", "Test camera 2", 10)
        result = test_inventory.addCamera("C003", "Test camera 3", 6)
        test_inventory.cameraList[2].setIsAvailable(False)
        
        tested_text = test_inventory.getAvailableCamera()

        actual_text = "{:<10}{:<30}{:<10}{:<12}{:<10}\n".format(
            "AssetTag", "Description", "Available", "Due Date", "Zoom")
        actual_text += "{:<10}{:<30}{:<10}{:<12}{:<10}\n".format(
            "C001", "Test camera 1", "Yes", "", 5)
        actual_text += "{:<10}{:<30}{:<10}{:<12}{:<10}\n".format(
            "C002", "Test camera 2", "Yes", "", 10)
        assert tested_text == actual_text

    ############### Test view laptop ######################
    def test_view_empty_laptop_list(self):
        test_inventory = Inventory()

        tested_text = test_inventory.getAvailableLaptop()
        
        actual_text = "{:<10}{:<30}{:<10}{:<12}{:<10}\n".format("AssetTag", 
                    "Description", "Available", "Due Date", "OS")
        actual_text += "There is no laptop to display."
        assert tested_text == actual_text

    def test_view_laptop(self):
        test_inventory = Inventory()
        result = test_inventory.addLaptop("L001", "Test Laptop 1", "WINXP")
        result = test_inventory.addLaptop("L002", "Test Laptop 2", "MACOS")

        tested_text = test_inventory.getAvailableLaptop()

        actual_text = "{:<10}{:<30}{:<10}{:<12}{:<10}\n".format("AssetTag", 
                    "Description", "Available", "Due Date", "OS")
        actual_text += "{:<10}{:<30}{:<10}{:<12}{:<10}\n".format(
            "L001", "Test Laptop 1", "Yes", "", "WINXP")
        actual_text += "{:<10}{:<30}{:<10}{:<12}{:<10}\n".format(
            "L002", "Test Laptop 2", "Yes", "", "MACOS")
        assert tested_text == actual_text

    def test_view_laptop_only_available(self):
        test_inventory = Inventory()
        result = test_inventory.addLaptop("L001", "Test Laptop 1", "WINXP")
        result = test_inventory.addLaptop("L002", "Test Laptop 2", "MACOS")
        result = test_inventory.addLaptop("L003", "Test Laptop 3", "WINXP")
        test_inventory.laptopList[2].setIsAvailable(False)
        
        tested_text = test_inventory.getAvailableLaptop()

        actual_text = "{:<10}{:<30}{:<10}{:<12}{:<10}\n".format("AssetTag", 
                    "Description", "Available", "Due Date", "OS")
        actual_text += "{:<10}{:<30}{:<10}{:<12}{:<10}\n".format(
            "L001", "Test Laptop 1", "Yes", "", "WINXP")
        actual_text += "{:<10}{:<30}{:<10}{:<12}{:<10}\n".format(
            "L002", "Test Laptop 2", "Yes", "", "MACOS")
        assert tested_text == actual_text

    def getAvailableCamera(self):
        output = ""
        output += "{:<10}{:<30}{:<10}{:<12}{:<10}\n".format("AssetTag", 
                    "Description", "Available", "Due Date", "Zoom")
        if len(self.cameraList) == 0:
            output += "There is no camera to display."
        else:
            for i in self.cameraList:
                if i.getIsAvailable() == "Yes":
                    # Refactor (D): Extract duplicate code as __str__()
                    # If __str__() already created, use it.
                    output += "{:<10}{:<30}{:<10}{:<12}{:<10}\n".format( 
                        i.getAssetTag(), i.getDescription(),  
                        i.getIsAvailable(), i.getDueDate(), 
                        i.getOpticalZoom() )
            
        return output

    def getAvailableLaptop(self):
        output = ""
        output += "{:<10}{:<30}{:<10}{:<12}{:<10}\n".format("AssetTag", 
                    "Description", "Available", "Due Date", "OS")
        if len(self.laptopList) == 0:
            output += "There is no laptop to display."
        else:
            for i in self.laptopList:
                if i.getIsAvailable() == "Yes":
                    # Refactor (D): Extract duplicate code as __str__()
                    # If __str__() already created, use it.
                    output += "{:<10}{:<30}{:<10}{:<12}{:<10}\n".format(
                        i.getAssetTag(), i.getDescription() , 
                        i.getIsAvailable(), i.getDueDate(), 
                        i.getOS() )
        return output
