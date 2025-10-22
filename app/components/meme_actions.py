import reflex as rx
from app.state import MemeState


def suggestion_chip(text: str) -> rx.Component:
    """A chip for a single meme text suggestion."""
    return rx.el.button(
        text,
        on_click=lambda: MemeState.select_suggestion(text),
        class_name="bg-gradient-to-r from-cyan-400 to-blue-500 text-white text-md font-bold px-5 py-2.5 rounded-full hover:from-cyan-500 hover:to-blue-600 transition-all shadow-md transform hover:scale-110",
    )


def meme_actions() -> rx.Component:
    """Actions available after an image is uploaded."""
    return rx.el.div(
        rx.match(
            MemeState.is_loading,
            (
                True,
                rx.el.div(
                    rx.spinner(class_name="text-orange-500", size="3"),
                    rx.el.p(
                        "COOKING UP THE MEMES... 👨\u200d🍳🔥",
                        class_name="text-gray-600 font-bold text-lg mt-2",
                    ),
                    class_name="flex flex-col items-center gap-4 p-8",
                ),
            ),
            rx.cond(
                MemeState.is_error,
                rx.el.div(
                    rx.icon("octagon_x", size=64, class_name="text-red-500"),
                    rx.el.p(
                        "MEME MACHINE BROKE 😭",
                        class_name="text-red-600 font-extrabold text-2xl mt-4",
                    ),
                    rx.el.button(
                        "TRY AGAIN? 🙏",
                        on_click=MemeState.generate_gemini_suggestions,
                        class_name="mt-6 bg-orange-500 text-white px-6 py-3 rounded-full hover:bg-orange-600 font-bold text-lg",
                    ),
                    class_name="flex flex-col items-center gap-2 p-8",
                ),
                rx.el.div(
                    rx.el.h3(
                        "PICK YOUR WEAPON 🎯",
                        class_name="text-2xl font-extrabold text-gray-800 mb-4 text-center tracking-tight",
                    ),
                    rx.el.div(
                        rx.foreach(MemeState.meme_suggestions, suggestion_chip),
                        class_name="flex flex-wrap justify-center gap-3",
                    ),
                    class_name="w-full p-4",
                ),
            ),
        ),
        rx.el.div(
            rx.el.button(
                rx.icon("pencil", size=24),
                "EDIT TEXT ✏️",
                on_click=MemeState.toggle_text_dialog,
                class_name="flex items-center gap-3 bg-gray-800 text-white font-bold py-4 px-8 rounded-full shadow-lg hover:bg-gray-900 hover:shadow-xl transition-all duration-300 transform hover:scale-105",
            ),
            rx.el.button(
                rx.icon("download", size=24),
                "DOWNLOAD 🔥",
                on_click=MemeState.download_meme,
                class_name="flex items-center gap-3 bg-gradient-to-r from-orange-500 to-pink-600 text-white font-bold py-4 px-8 rounded-full shadow-lg hover:from-orange-600 hover:to-pink-700 hover:shadow-xl transition-all duration-300 transform hover:scale-105",
            ),
            class_name="flex justify-center gap-4 mt-8",
        ),
        class_name="w-full",
    )