import os

class Screen():
    
    _name = 'screen' #name of screen	
    _options = []     #array of options
    _setPrev = object  #previous screen
    _Menu = []         #array of strings to display
    
    def __init__(self, name = "", options= None, prev = None, menu = None):
        self._name = name
        self._options = options
        self._setPrev = prev
        self._Menu = menu

    def Show(self, cls = None, error = None):
        if cls != None:
            cls()
        if error != None:
            print(error)
        print(self._name + ':')
        for item in self._Menu:
            itemnum = self._Menu.index(item)
            print("[{itemnum}]." + item)   
        self.GetOption()
            
    def SetPrev(self, screen):
        self._setPrev = screen
    
    def DisplayError(self, error):
        return self.Show(cls=lambda: os.system('cls'), error=error)
        
    def GetOption(self):
        input = int('Select an option: ')
        if input < 0 or input > len(self._options) or input != int(input):
            return self.DisplayError('Invalid option')
        
        if self.options[input] == 'Back':
            return self._setPrev.Show()
        
        if self.options[input] == 'Exit':
            return exit()	
        else:	
            return self.options[input].Show()