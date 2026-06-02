from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from login.login_screen import LoginScreen
from login.register_screen import RegisterScreen
from login.profile_screen import ProfileScreen
from auth.auth_manager import AuthManager


class TesoePopApp(App):
    def build(self):
        # Configurar color de fondo de la ventana
        Window.clearcolor = (1, 1, 1, 1)  # Blanco
        
        # Crear instancia compartida de AuthManager
        auth_manager = AuthManager()
        
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login', auth_manager=auth_manager))
        sm.add_widget(RegisterScreen(name='register', auth_manager=auth_manager))
        sm.add_widget(ProfileScreen(name='profile', auth_manager=auth_manager))
        
        return sm


if __name__ == '__main__':
    TesoePopApp().run()
