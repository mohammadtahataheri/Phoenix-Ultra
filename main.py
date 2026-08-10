import customtkinter as ctk

# رفع غلط‌های املایی در نام تم‌ها
THEMES = {
    "night blue": {
        "mode": "Dark",
        "color": {"main": "#1E1E1E", "button": "#3B02F6", "text": "#FFFFFF", "base": "#2B2525"},
        "font": {"family": "Vazirmatn", "size": 16}
    },
    "emerald": {
        "mode": "Light",
        "color": {"main": "#FFFFFF", "button": "#22C55E", "text": "#000000", "base": "#6e6e6e"},
        "font": {"family": "Vazirmatn", "size": 18}
    },
    "dark red": {
        "mode": "Dark",
        "color": {"main": "#121212", "button": "#EF4444", "text": "#FFFFFF", "base": "#2D2D2D"},
        "font": {"family": "Vazirmatn", "size": 18}
    },
    "purple": {
        "mode": "Dark",
        "color": {"main": "#1A1A2E", "button": "#8B5CF6", "text": "#FFFFFF", "base": "#2C2C54"},
        "font": {"family": "Vazirmatn", "size": 18}
    },
    "orange": {
        "mode": "Light",
        "color": {"main": "#FFF7ED", "button": "#F97316", "text": "#000000", "base": "#D6D3D1"},
        "font": {"family": "Vazirmatn", "size": 18}
    },
    "ocean": {
        "mode": "Dark",
        "color": {"main": "#0F172A", "button": "#06B6D4", "text": "#FFFFFF", "base": "#1E293B"},
        "font": {"family": "Vazirmatn", "size": 18}
    },
    "gold": {
        "mode": "Light",
        "color": {"main": "#F5F5F5", "button": "#EAB308", "text": "#000000", "base": "#BDBDBD"},
        "font": {"family": "Vazirmatn", "size": 18}
    },
    "Pink Galaxy": {
        "mode": "Dark",
        "color": {"main": "#111827", "button": "#EC4899", "text": "#FFFFFF", "base": "#374151"},
        "font": {"family": "Vazirmatn", "size": 18}
    },
    "surprise": {
        "mode": "Light",
        "color": {"main": "#ECFEFF", "button": "#14B8A6", "text": "#000000", "base": "#94A3B8"},
        "font": {"family": "Vazirmatn", "size": 18}
    }
}

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("900x600")
        
        # تنظیم تم اولیه
        self.current_theme = "night blue"
        
        # لیست‌های جداگانه برای منوی کناری و محتوا جهت جلوگیری از به‌روزرسانی ویجت‌های تخریب شده
        self.sidebar_widgets = []
        self.content_widgets = []
        self.theme_menu = None 

        # پیکربندی پنجره اصلی
        self.configure(fg_color=THEMES[self.current_theme]["color"]["base"])
        ctk.set_appearance_mode(THEMES[self.current_theme]["mode"])

        # --- منوی کناری ---
        self.sidebar = ctk.CTkFrame(
            self, width=70, corner_radius=15,
            fg_color=THEMES[self.current_theme]["color"]["main"]
        )
        self.sidebar.pack(side="left", fill="y", padx=20, pady=20)
        self.sidebar.pack_propagate(False)

        # --- محوطه محتوای اصلی ---
        self.content = ctk.CTkFrame(
            self, corner_radius=15,
            fg_color=THEMES[self.current_theme]["color"]["main"]
        )
        self.content.pack(side="right", fill="both", expand=True, padx=(0, 20), pady=20)

        # دکمه‌های منوی کناری
        self.create_sidebar_button("🏠", self.show_home)
        self.create_sidebar_button("⚙️", self.show_settings)
        self.create_sidebar_button("📱", self.show_apps)

        self.show_home()

    def create_sidebar_button(self, text, command):
        btn = ctk.CTkButton(
            self.sidebar, text=text, width=40,
            fg_color=THEMES[self.current_theme]["color"]["button"],
            text_color=THEMES[self.current_theme]["color"]["text"],
            command=command
        )
        btn.pack(anchor="n", pady=5)
        self.sidebar_widgets.append(btn)

    def clear_content(self):
        """فریم محتوا را پاک کرده و لیست ویجت‌های محتوا را بازنشانی می‌کند"""
        for widget in self.content.winfo_children():
            widget.destroy()
        self.content_widgets.clear()
        self.theme_menu = None

    def show_home(self):
        self.clear_content()
        theme = THEMES[self.current_theme]

        title = ctk.CTkLabel(
            self.content, text="welcome to home screen",
            font=(theme["font"]["family"], theme["font"]["size"]),
            text_color=theme["color"]["text"]
        )
        title.pack(pady=30)
        self.content_widgets.append(title)

        text = ctk.CTkLabel(
            self.content, text="به صفحه اصلی خوش آمدید.",
            text_color=theme["color"]["text"],
            font=(theme["font"]["family"], theme["font"]["size"])
        )
        text.pack()
        self.content_widgets.append(text)

    def show_settings(self):
        self.clear_content()
        theme = THEMES[self.current_theme]

        title = ctk.CTkLabel(
            self.content, text="⚙️ تنظیمات",
            font=(theme["font"]["family"], theme["font"]["size"]),
            text_color=theme["color"]["text"]
        )
        title.pack(pady=30)
        self.content_widgets.append(title)

        # منوی کشویی تم (به طور خاص برای به‌روزرسانی رنگ‌ها ردیابی می‌شود)
        self.theme_menu = ctk.CTkOptionMenu(
            self.content, values=list(THEMES.keys()),
            command=self.change_theme,
            font=(theme["font"]["family"], theme["font"]["size"]),
            fg_color=theme["color"]["button"],
            button_color=theme["color"]["button"],
            button_hover_color=theme["color"]["button"],
            text_color=theme["color"]["text"],
            dropdown_fg_color=theme["color"]["main"],
            dropdown_hover_color=theme["color"]["button"],
            dropdown_text_color=theme["color"]["text"]
        )
        self.theme_menu.pack(pady=10)
        self.theme_menu.set(self.current_theme)

    def show_apps(self):
        self.clear_content()
        theme = THEMES[self.current_theme]

        title = ctk.CTkLabel(
            self.content, text="📱 برنامک ها",
            font=(theme["font"]["family"], theme["font"]["size"]),
            text_color=theme["color"]["text"]
        )
        title.pack(pady=30)
        self.content_widgets.append(title)

        # دکمه‌ای برای هدایت واقعی به صفحه برنامه اضافه شد
        open_btn = ctk.CTkButton(
            self.content, text="باز کردن برنامه", width=120,
            fg_color=theme["color"]["button"],
            text_color=theme["color"]["text"],
            font=(theme["font"]["family"], theme["font"]["size"]),
            command=self.app
        )
        open_btn.pack(pady=10)
        self.content_widgets.append(open_btn)

    def app(self):
        self.clear_content()
        theme = THEMES[self.current_theme]

        title = ctk.CTkLabel(
            self.content, text="برنامک",
            font=(theme["font"]["family"], theme["font"]["size"]),
            text_color=theme["color"]["text"]
        )
        title.pack(pady=30)
        self.content_widgets.append(title)

        # مکان‌نمایی برای منطق اصلی برنامه شما
        calc = ctk.CTkButton(
            self.content, text="ماشین حساب", width=120,
            fg_color=theme["color"]["button"],
            text_color=theme["color"]["text"],
            font=(theme["font"]["family"], theme["font"]["size"]),
            command=lambda: print("منطق ماشین حساب اینجا قرار می‌گیرد!")
        )
        calc.pack(pady=10)
        self.content_widgets.append(calc)

    def change_theme(self, name):
        self.current_theme = name
        theme = THEMES[name]
        ctk.set_appearance_mode(theme["mode"])
        self.apply_theme()

    def apply_theme(self):
        """رنگ‌های برنامه اصلی، منوی کناری و تمام ویجت‌های فعال را به‌روزرسانی می‌کند"""
        theme = THEMES[self.current_theme]

        # به‌روزرسانی پس‌زمینه‌ها
        self.configure(fg_color=theme["color"]["base"])
        self.sidebar.configure(fg_color=theme["color"]["main"])
        self.content.configure(fg_color=theme["color"]["main"])

        # به‌روزرسانی ایمن ویجت‌های منوی کناری و محتوا
        for widget in self.sidebar_widgets + self.content_widgets:
            if widget.winfo_exists():
                widget.configure(
                    fg_color=theme["color"]["button"],
                    text_color=theme["color"]["text"]
                )

        # به‌روزرسانی آنی رنگ‌های منوی کشویی
        if self.theme_menu and self.theme_menu.winfo_exists():
            self.theme_menu.configure(
                fg_color=theme["color"]["button"],
                button_color=theme["color"]["button"],
                button_hover_color=theme["color"]["button"],
                text_color=theme["color"]["text"],
                dropdown_fg_color=theme["color"]["main"],
                dropdown_hover_color=theme["color"]["button"],
                dropdown_text_color=theme["color"]["text"]
            )

if __name__ == "__main__":
    app = App()
    app.mainloop()
