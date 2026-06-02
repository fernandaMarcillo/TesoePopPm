from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from auth.auth_manager import AuthManager


class LoginScreen(Screen):
    # Colores - Fondo blanco con botones rosados
    BACKGROUND_COLOR = "#FFFFFF"  # Blanco
    CARD_COLOR = "#FFE4E1"  # Rosa muy claro
    PRIMARY_COLOR = "#FF69B4"  # Rosa
    BUTTON_COLOR = "#FF69B4"  # Rosa
    TEXT_PRIMARY = "#333333"  # Gris oscuro
    TEXT_SECONDARY = "#666666"  # Gris medio
    BORDER_COLOR = "#FF69B4"

    def __init__(self, auth_manager=None, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.auth_manager = auth_manager or AuthManager()
        self.username = None
        self.password = None
        self.build_ui()

    def build_ui(self):
        # Main layout
        main_layout = BoxLayout(orientation='vertical')
        
        # Header section
        header_layout = BoxLayout(orientation='vertical', size_hint_y=0.3, padding='50dp', spacing='20dp')
        
        title_label = Label(
            text='Tesoe Pop',
            font_size='40sp',
            color=(1, 0.41, 0.71, 1),  # Rosa
            size_hint_y=None,
            height='60dp',
            bold=True
        )
        
        subtitle_label = Label(
            text='Panadería y Postres',
            font_size='20sp',
            color=(0.4, 0.4, 0.4, 1),  # Gris oscuro
            size_hint_y=None,
            height='40dp'
        )
        
        header_layout.add_widget(title_label)
        header_layout.add_widget(subtitle_label)
        
        # Form section
        form_layout = BoxLayout(orientation='vertical', size_hint_y=0.7, padding='50dp', spacing='20dp')
        
        # Input fields container
        input_container = BoxLayout(orientation='vertical', size_hint_y=None, height='180dp', spacing='10dp')
        
        username_label = Label(
            text='Usuario',
            font_size='16sp',
            color=(1, 0.41, 0.71, 1),  # Rosa
            size_hint_y=None,
            height='30dp'
        )
        
        self.username = TextInput(
            size_hint_y=None,
            height='50dp',
            multiline=False,
            hint_text='Ingrese su usuario',
            background_color=(1, 0.89, 0.88, 1),  # Rosa muy claro
            foreground_color=(0.2, 0.2, 0.2, 1),  # Gris oscuro
            cursor_color=(1, 0.41, 0.71, 1)  # Rosa
        )
        
        password_label = Label(
            text='Contraseña',
            font_size='16sp',
            color=(1, 0.41, 0.71, 1),  # Rosa
            size_hint_y=None,
            height='30dp'
        )
        
        self.password = TextInput(
            size_hint_y=None,
            height='50dp',
            multiline=False,
            password=True,
            hint_text='Ingrese su contraseña',
            background_color=(1, 0.89, 0.88, 1),  # Rosa muy claro
            foreground_color=(0.2, 0.2, 0.2, 1),  # Gris oscuro
            cursor_color=(1, 0.41, 0.71, 1)  # Rosa
        )
        
        input_container.add_widget(username_label)
        input_container.add_widget(self.username)
        input_container.add_widget(password_label)
        input_container.add_widget(self.password)
        
        # Login button
        login_button = Button(
            text='Iniciar Sesión',
            font_size='18sp',
            size_hint_y=None,
            height='60dp',
            background_color=(1, 0.41, 0.71, 1),  # Rosa
            color=(1, 1, 1, 1)  # Blanco
        )
        login_button.bind(on_press=self.login)
        
        # Register button
        register_button = Button(
            text='Crear Cuenta',
            font_size='16sp',
            size_hint_y=None,
            height='50dp',
            background_color=(0.8, 0.5, 0.6, 1),  # Rosa oscuro
            color=(1, 1, 1, 1)  # Blanco
        )
        register_button.bind(on_press=self.go_to_register)
        
        form_layout.add_widget(input_container)
        form_layout.add_widget(login_button)
        form_layout.add_widget(register_button)
        
        # Add all to main layout
        main_layout.add_widget(header_layout)
        main_layout.add_widget(form_layout)
        
        self.add_widget(main_layout)

    def login(self, instance):
        username = self.username.text if self.username.text else ""
        password = self.password.text if self.password.text else ""
        
        if not username or not password:
            self.show_error("Por favor ingrese usuario y contraseña")
            return
        
        # Validación de usuario usando AuthManager
        if self.auth_manager.login(username, password):
            self.manager.current = 'profile'
        else:
            self.show_error("Usuario o contraseña incorrectos")

    def go_to_register(self, instance):
        self.manager.current = 'register'

    def show_error(self, message):
        print(f"Error: {message}")
