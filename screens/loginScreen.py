import screens.screen as Screen
import screens.mainScreen as MainScreen


class LoginScreen(Screen):
    def __init__(self, prev = MainScreen.MainScreen, cls = None, menu = ["Username: ", "Password: ", "Back"], options = None, name = None):
        super().__init__(name, options, prev, menu)
        
    
    def Show(self, cls = None, error = None):
        if cls != None:
            cls()
        if error != None:
            print(error)
        print(self._name + ':')
        for item in self._Menu:
            itemnum = self._Menu.index(item)
            print("[{itemnum}]." + item)
        super().GetOption()
    
