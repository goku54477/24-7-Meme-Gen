import reflex as rx


def header() -> rx.Component:
    """The main header for the app."""
    return rx.el.header(
        rx.el.div(
            rx.icon("bot-message-square", class_name="text-orange-500", size=32),
            rx.el.h1(
                "AI Meme Gen",
                class_name="text-2xl font-bold text-gray-800 tracking-tighter",
            ),
            class_name="flex items-center gap-3",
        ),
        class_name="fixed top-0 left-0 right-0 z-10 flex items-center justify-between px-4 h-16 bg-white/80 backdrop-blur-md border-b border-gray-200 shadow-sm",
    )