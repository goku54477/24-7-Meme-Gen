import reflex as rx


def header() -> rx.Component:
    """The main header for the app."""
    return rx.el.header(
        rx.el.div(
            rx.image(src="/favicon.ico", class_name="w-12 h-12"),
            rx.el.h1(
                "MEME GENERATOR \ud83d\udd25",
                class_name="text-3xl font-extrabold text-white tracking-tighter",
                style={"textShadow": "2px 2px 4px rgba(0,0,0,0.3)"},
            ),
            class_name="flex items-center gap-4",
        ),
        class_name="fixed top-0 left-0 right-0 z-10 flex items-center justify-center px-4 h-20 bg-gradient-to-r from-purple-500 via-pink-500 to-orange-500 shadow-lg",
    )