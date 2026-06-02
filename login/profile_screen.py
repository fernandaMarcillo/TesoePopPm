from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class ProfileScreen(Screen):
    # Colores - Fondo blanco con botones rosados
    BACKGROUND_COLOR = "#FFFFFF"  # Blanco
    CARD_COLOR = "#FFE4E1"  # Rosa muy claro
    PRIMARY_COLOR = "#FF69B4"  # Rosa
    BUTTON_COLOR = "#FF69B4"  # Rosa
    TEXT_PRIMARY = "#333333"  # Gris oscuro
    TEXT_SECONDARY = "#666666"  # Gris medio
    BORDER_COLOR = "#FF69B4"

    def __init__(self, auth_manager=None, **kwargs):
        super(ProfileScreen, self).__init__(**kwargs)
        self.auth_manager = auth_manager
        self.username_label = None
        self.email_label = None
        self.full_name_label = None
        self.build_ui()

    def build_ui(self):
        # Main layout
        main_layout = BoxLayout(orientation='vertical')
        
        # Header section
        header_layout = BoxLayout(orientation='vertical', size_hint_y=0.15, padding='20dp', spacing='10dp')
        
        title_label = Label(
            text='Perfil de Usuario',
            font_size='28sp',
            color=(1, 0.41, 0.71, 1),  # Rosa
            size_hint_y=None,
            height='50dp',
            bold=True
        )
        
        header_layout.add_widget(title_label)
        
        # Content section
        content_layout = BoxLayout(orientation='vertical', size_hint_y=0.7, padding='30dp', spacing='20dp')
        
        # Info card
        info_card = BoxLayout(orientation='vertical', size_hint_y=None, height='250dp', padding='20dp', spacing='15dp')
        
        info_title = Label(
            text='Información Personal',
            font_size='20sp',
            color=(1, 0.41, 0.71, 1),  # Rosa
            size_hint_y=None,
            height='40dp',
            bold=True
        )
        
        # Username section
        username_section = BoxLayout(orientation='vertical', size_hint_y=None, height='80dp', spacing='5dp')
        
        username_label = Label(
            text='Usuario',
            font_size='14sp',
            color=(0.4, 0.4, 0.4, 1),  # Gris oscuro
            size_hint_y=None,
            height='25dp'
        )
        
        self.username_label = Label(
            text='',
            font_size='18sp',
            color=(0.2, 0.2, 0.2, 1),  # Gris oscuro
            size_hint_y=None,
            height='30dp'
        )
        
        username_section.add_widget(username_label)
        username_section.add_widget(self.username_label)
        
        # Email section
        email_section = BoxLayout(orientation='vertical', size_hint_y=None, height='80dp', spacing='5dp')
        
        email_label = Label(
            text='Email',
            font_size='14sp',
            color=(0.4, 0.4, 0.4, 1),  # Gris oscuro
            size_hint_y=None,
            height='25dp'
        )
        
        self.email_label = Label(
            text='',
            font_size='18sp',
            color=(0.2, 0.2, 0.2, 1),  # Gris oscuro
            size_hint_y=None,
            height='30dp'
        )
        
        email_section.add_widget(email_label)
        email_section.add_widget(self.email_label)
        
        # Full name section
        full_name_section = BoxLayout(orientation='vertical', size_hint_y=None, height='80dp', spacing='5dp')
        
        full_name_title = Label(
            text='Nombre Completo',
            font_size='14sp',
            color=(0.4, 0.4, 0.4, 1),  # Gris oscuro
            size_hint_y=None,
            height='25dp'
        )
        
        self.full_name_label = Label(
            text='',
            font_size='18sp',
            color=(0.2, 0.2, 0.2, 1),  # Gris oscuro
            size_hint_y=None,
            height='30dp'
        )
        
        full_name_section.add_widget(full_name_title)
        full_name_section.add_widget(self.full_name_label)
        
        info_card.add_widget(info_title)
        info_card.add_widget(username_section)
        info_card.add_widget(email_section)
        info_card.add_widget(full_name_section)
        
        content_layout.add_widget(info_card)
        
        # Button section
        button_layout = BoxLayout(orientation='vertical', size_hint_y=0.15, padding='30dp', spacing='15dp')
        
        logout_button = Button(
            text='Cerrar Sesión',
            font_size='18sp',
            size_hint_y=None,
            height='50dp',
            background_color=(1, 0.41, 0.71, 1),  # Rosa
            color=(1, 1, 1, 1)  # Blanco
        )
        logout_button.bind(on_press=self.logout)
        
        products_button = Button(
            text='Volver a Productos',
            font_size='16sp',
            size_hint_y=None,
            height='45dp',
            background_color=(0.8, 0.5, 0.6, 1),  # Rosa oscuro
            color=(1, 1, 1, 1)  # Blanco
        )
        products_button.bind(on_press=self.go_to_products)
        
        button_layout.add_widget(logout_button)
        button_layout.add_widget(products_button)
        
        # Add all to main layout
        main_layout.add_widget(header_layout)
        main_layout.add_widget(content_layout)
        main_layout.add_widget(button_layout)
        
        self.add_widget(main_layout)

    def on_enter(self):
        self.update_user_info()

    def update_user_info(self):
        if self.auth_manager and self.auth_manager.get_current_user():
            user = self.auth_manager.get_current_user()
            self.username_label.text = user.username
            self.email_label.text = user.email
            self.full_name_label.text = user.full_name or "No especificado"
        else:
            self.show_error("No hay usuario logueado")

    def logout(self, instance):
        if self.auth_manager:
            self.auth_manager.logout()
            self.manager.current = 'login'

    def go_to_products(self, instance):
        self.manager.current = 'products'

    def show_error(self, message):
        print(f"Error: {message}")
