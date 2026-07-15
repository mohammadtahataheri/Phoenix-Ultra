import customtkinter as ctk

THEMES = {
    "آبی نیمه شب": {
        "mode": "Dark",
        "color": {
            "main": "#1E1E1E",
            "button": "#3B02F6",
            "text": "#FFFFFF",
            "base": "#2B2525"
        },
        "font": {
            "family": "Vazirmatn",
            "size": 16
        }
    },

    "زمردی": {
        "mode": "Light",
        "color": {
            "main": "#FFFFFF",
            "button": "#22C55E",
            "text": "#000000",
            "base": "#6e6e6e"
        },
        "font": {
            "family": "Vazirmatn",
            "size": 18
        }
    },
    "سرخ تیره": {
        "mode": "Dark",
        "color": {
            "main": "#121212",
            "button": "#EF4444",
            "text": "#FFFFFF",
            "base": "#2D2D2D"
        },
        "font": {
            "family": "Vazirmatn",
            "size": 18
        }
    },

    "بنفش اطلسی": {
        "mode": "Dark",
        "color": {
            "main": "#1A1A2E",
            "button": "#8B5CF6",
            "text": "#FFFFFF",
            "base": "#2C2C54"
        },
        "font": {
            "family": "Vazirmatn",
            "size": 18
        }
    },

    "غروب نارنجی": {
        "mode": "Light",
        "color": {
            "main": "#FFF7ED",
            "button": "#F97316",
            "text": "#000000",
            "base": "#D6D3D1"
        },
        "font": {
            "family": "Vazirmatn",
            "size": 18
        }
    },

    "اقیانوسی": {
        "mode": "Dark",
        "color": {
            "main": "#0F172A",
            "button": "#06B6D4",
            "text": "#FFFFFF",
            "base": "#1E293B"
        },
        "font": {
            "family": "Vazirmatn",
            "size": 18
        }
    },

    "طلایی": {
        "mode": "Light",
        "color": {
            "main": "#F5F5F5",
            "button": "#EAB308",
            "text": "#000000",
            "base": "#BDBDBD"
        },
        "font": {
            "family": "Vazirmatn",
            "size": 18
        }
    },

    "کهکشان صورتی": {
        "mode": "Dark",
        "color": {
            "main": "#111827",
            "button": "#EC4899",
            "text": "#FFFFFF",
            "base": "#374151"
        },
        "font": {
            "family": "Vazirmatn",
            "size": 18
        }
    },

    "نسیم نعنایی": {
        "mode": "Light",
        "color": {
            "main": "#ECFEFF",
            "button": "#14B8A6",
            "text": "#000000",
            "base": "#94A3B8"
        },
        "font": {
            "family": "Vazirmatn",
            "size": 18
        }
    }
}

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("900x600")

        self.current_theme = "آبی نیمه شب"
        self.widgets = []
        self.configure(
            fg_color=THEMES[self.current_theme]["color"]["base"]
        )
        # صفحه اصلی
        self.sidebar = ctk.CTkFrame(
            self,
            width=70,
            corner_radius=15,
            fg_color=THEMES[self.current_theme]["color"]["main"]
        )
        self.sidebar.pack(
            side="left",
            fill="y",
            padx=20,
            pady=20
        )
        self.sidebar.pack_propagate(False)

        self.content = ctk.CTkFrame(
            self,
            corner_radius=15,
            fg_color = THEMES[self.current_theme]["color"]["main"]
        )
        self.content.pack(
            side="right",
            fill="both",
            expand=True,
            padx=(0, 20),
            pady=20
        )

        # دکمه‌ها
        self.home_btn = ctk.CTkButton(
            self.sidebar,
            text="🏠",
            width=40,
            fg_color=THEMES[self.current_theme]["color"]["button"],
            text_color=THEMES[self.current_theme]["color"]["text"],
            command=self.show_home
        )

        self.home_btn.pack(
            anchor="n",
            pady=(10, 5)
        )

        self.widgets.append(self.home_btn)
        self.setting_btn = ctk.CTkButton(
            self.sidebar,
            text="⚙️",
            width=40,
            fg_color=THEMES[self.current_theme]["color"]["button"],
            text_color=THEMES[self.current_theme]["color"]["text"],
            command=self.show_settings
        )

        self.setting_btn.pack(
            anchor="n",
            pady=(5, 10)
        )

        self.widgets.append(self.setting_btn)
        self.show_home()

    def clear_content(self):
        for widget in self.content.winfo_children():
            widget.destroy()

    def show_home(self):
        self.clear_content()

        theme = THEMES[self.current_theme]

        title = ctk.CTkLabel(
            self.content,
            text="welcome to home screen",
            font=(
                theme["font"]["family"],
                theme["font"]["size"]
            ),
            text_color=theme["color"]["text"]
        )
        title.pack(pady=30)

        text = ctk.CTkLabel(
            self.content,
            text="به صفحه اصلی خوش آمدید.",
            text_color=theme["color"]["text"],
            font=(
                theme["font"]["family"],
                theme["font"]["size"]
            )
        )
        text.pack()
    def show_settings(self):
        self.clear_content()

        theme = THEMES[self.current_theme]

        theme = THEMES[self.current_theme]

        title = ctk.CTkLabel(
            self.content,
            text="⚙️ تنظیمات",
            font=(theme["font"]["family"], theme["font"]["size"]),
            text_color=THEMES[self.current_theme]["color"]["text"]

        )
        title.pack(pady=30)

        self.theme_menu = ctk.CTkOptionMenu(
            self.content,
            values=list(THEMES.keys()),
            command=self.change_theme,
            font=(theme["font"]["family"], theme["font"]["size"]),
            fg_color=THEMES[self.current_theme]["color"]["button"],
            text_color=THEMES[self.current_theme]["color"]["text"],
        )
        self.theme_menu.pack(pady=10)

        self.theme_menu.set(self.current_theme)

    def change_theme(self, name):
        self.current_theme = name

        theme = THEMES[name]

        ctk.set_appearance_mode(theme["mode"])

        self.apply_theme()
    def apply_theme(self):
        theme = THEMES[self.current_theme]

        self.configure(
            fg_color=theme["color"]["base"]
        )

        self.sidebar.configure(
            fg_color=theme["color"]["main"]
        )

        self.content.configure(
            fg_color=theme["color"]["main"]
        )

        for widget in self.widgets:
            widget.configure(
                fg_color=theme["color"]["button"],
                text_color=theme["color"]["text"]
            )
app = App()
app.mainloop()