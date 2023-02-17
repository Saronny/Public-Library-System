import screens.screen as Screen
import screens.loginScreen as LoginScreen

class MainScreen(Screen):
    
    _loginScreen = LoginScreen.LoginScreen()
    
    def __init__(self):
        Screen.__init__(self, 'Main Screen', [ _loginScreen, 'Exit'], None)
    
    
        