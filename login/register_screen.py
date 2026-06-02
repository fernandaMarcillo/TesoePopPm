from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from auth.auth_manager import AuthManager


class RegisterScreen(Screen):
    # Colores - Fondo blanco con botones rosados
    BACKGROUND_COLOR = "#FFFFFF"  # Blanco
    CARD_COLOR = "#FFE4E1"  # Rosa muy claro
    PRIMARY_COLOR = "#FF69B4"  # Rosa
    BUTTON_COLOR = "#FF69B4"  # Rosa
    TEXT_PRIMARY = "#333333"  # Gris oscuro
    TEXT_SECONDARY = "#666666"  # Gris medio
    BORDER_COLOR = "#FF69B4"

    def __init__(self, auth_manager=None, **kwargs):
        super(RegisterScreen, self).__init__(**kwargs)
        self.auth_manager = auth_manager or AuthManager()
        self.username = None
        self.email = None
        self.password = None
        self.confirm_password = None
        self.full_name = None
        self.build_ui()

    def build_ui(self):
        # Main layout
        main_layout = BoxLayout(orientation='vertical', padding='30dp', spacing='15dp')
        
        # Title
        title_label = Label(
            text='Crear Cuenta',
            font_size='32sp',
            color=(1, 0.41, 0.71, 1),  # Rosa
            size_hint_y=None,
            height='50dp',
            bold=True
        )
        
        subtitle_label = Label(
            text='Regístrate para comenzar',
            font_size='16sp',
            color=(0.4, 0.4, 0.4, 1),  # Gris oscuro
            size_hint_y=None,
            height='30dp'
        )
        
        # Full name field (optional)
        full_name_label = Label(
            text='Nombre Completo (Opcional)',
            font_size='14sp',
            color=(1, 0.41, 0.71, 1),  # Rosa
            size_hint_y=None,
            height='25dp'
        )
        
        self.full_name = TextInput(
            size_hint_y=None,
            height='45dp',
            multiline=False,
            hint_text='Ingrese su nombre completo',
            background_color=(1, 0.89, 0.88, 1),  # Rosa muy claro
            foreground_color=(0.2, 0.2, 0.2, 1),  # Gris oscuro
            cursor_color=(1, 0.41, 0.71, 1)  # Rosa
        )
        
        # Username field (required)
        username_label = Label(
            text='Usuario *',
            font_size='14sp',
            color=(1, 0.41, 0.71, 1),  # Rosa
            size_hint_y=None,
            height='25dp'
        )
        
        self.username = TextInput(
            size_hint_y=None,
            height='45dp',
            multiline=False,
            hint_text='Ingrese su usuario',
            background_color=(1, 0.89, 0.88, 1),  # Rosa muy claro
            foreground_color=(0.2, 0.2, 0.2, 1),  # Gris oscuro
            cursor_color=(1, 0.41, 0.71, 1)  # Rosa
        )
        
        # Email field (required)
        email_label = Label(
            text='Email *',
            font_size='14sp',
            color=(1, 0.41, 0.71, 1),  # Rosa
            size_hint_y=None,
            height='25dp'
        )
        
        self.email = TextInput(
            size_hint_y=None,
            height='45dp',
            multiline=False,
            hint_text='Ingrese su email',
            background_color=(1, 0.89, 0.88, 1),  # Rosa muy claro
            foreground_color=(0.2, 0.2, 0.2, 1),  # Gris oscuro
            cursor_color=(1, 0.41, 0.71, 1)  # Rosa
        )
        
        # Password field (required)
        password_label = Label(
            text='Contraseña *',
            font_size='14sp',
            color=(1, 0.41, 0.71, 1),  # Rosa
            size_hint_y=None,
            height='25dp'
        )
        
        self.password = TextInput(
            size_hint_y=None,
            height='45dp',
            multiline=False,
            password=True,
            hint_text='Mínimo 6 caracteres',
            background_color=(1, 0.89, 0.88, 1),  # Rosa muy claro
            foreground_color=(0.2, 0.2, 0.2, 1),  # Gris oscuro
            cursor_color=(1, 0.41, 0.71, 1)  # Rosa
        )
        
        # Confirm password field (required)
        confirm_password_label = Label(
            text='Confirmar Contraseña *',
            font_size='14sp',
            color=(1, 0.41, 0.71, 1),  # Rosa
            size_hint_y=None,
            height='25dp'
        )
        
        self.confirm_password = TextInput(
            size_hint_y=None,
            height='45dp',
            multiline=False,
            password=True,
            hint_text='Confirme su contraseña',
            background_color=(1, 0.89, 0.88, 1),  # Rosa muy claro
            foreground_color=(0.2, 0.2, 0.2, 1),  # Gris oscuro
            cursor_color=(1, 0.41, 0.71, 1)  # Rosa
        )
        
        # Register button
        register_button = Button(
            text='Registrarse',
            font_size='18sp',
            size_hint_y=None,
            height='50dp',
            background_color=(1, 0.41, 0.71, 1),  # Rosa
            color=(1, 1, 1, 1)  # Blanco
        )
        register_button.bind(on_press=self.register)
        
        # Back to login button
        back_button = Button(
            text='Volver al Login',
            font_size='16sp',
            size_hint_y=None,
            height='45dp',
            background_color=(0.8, 0.5, 0.6, 1),  # Rosa oscuro
            color=(1, 1, 1, 1)  # Blanco
        )
        back_button.bind(on_press=self.go_to_login)
        
        # Add all widgets to main layout
        main_layout.add_widget(title_label)
        main_layout.add_widget(subtitle_label)
        main_layout.add_widget(full_name_label)
        main_layout.add_widget(self.full_name)
        main_layout.add_widget(username_label)
        main_layout.add_widget(self.username)
        main_layout.add_widget(email_label)
        main_layout.add_widget(self.email)
        main_layout.add_widget(password_label)
        main_layout.add_widget(self.password)
        main_layout.add_widget(confirm_password_label)
        main_layout.add_widget(self.confirm_password)
        main_layout.add_widget(register_button)
        main_layout.add_widget(back_button)
        
        self.add_widget(main_layout)

    def register(self, instance):
        username = self.username.text if self.username else ""
        email = self.email.text if self.email else ""
        password = self.password.text if self.password else ""
        confirm_password = self.confirm_password.text if self.confirm_password else ""
        full_name = self.full_name.text if self.full_name else ""
        
        print(f"Debug - username: '{username}', email: '{email}', password: '{password}'")
        
        # Validaciones
        if not username or not email or not password:
            self.show_error("Por favor complete todos los campos obligatorios")
            return
        
        if password != confirm_password:
            self.show_error("Las contraseñas no coinciden")
            return
        
        if len(password) < 6:
            self.show_error("La contraseña debe tener al menos 6 caracteres")
            return
        
        # Registrar usuario usando AuthManager
        success, message = self.auth_manager.register(username, email, password, full_name)
        if success:
            self.show_success(message)
            self.manager.current = 'login'
        else:
            self.show_error(message)

    def go_to_login(self, instance):
        self.manager.current = 'login'

    def show_error(self, message):
        print(f"Error: {message}")

    def show_success(self, message):
        print(f"Éxito: {message}")
