import reflex as rx
from app.state import MemeState


def suggestion_chip(text: str) -> rx.Component:
    """A chip for a single meme text suggestion."""
    return rx.el.button(
        text,
        on_click=lambda: MemeState.select_suggestion(text),
        class_name="bg-gray-200 text-gray-800 text-sm font-medium px-4 py-2 rounded-full hover:bg-gray-300 transition-colors shadow-sm",
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
                        "AI is thinking...", class_name="text-gray-500 font-medium"
                    ),
                    class_name="flex flex-col items-center gap-4 p-8",
                ),
            ),
            rx.cond(
                MemeState.is_error,
                rx.el.div(
                    rx.icon("flag_triangle_right", size=48, class_name="text-red-500"),
                    rx.el.p(
                        "Couldn't generate captions.",
                        class_name="text-red-600 font-semibold mt-2",
                    ),
                    rx.el.button(
                        "Try Again",
                        on_click=MemeState.generate_gemini_suggestions,
                        class_name="mt-4 bg-orange-500 text-white px-4 py-2 rounded-full hover:bg-orange-600",
                    ),
                    class_name="flex flex-col items-center gap-2 p-8",
                ),
                rx.el.div(
                    rx.el.h3(
                        "Choose a caption or write your own:",
                        class_name="text-md font-semibold text-gray-700 mb-3 text-center",
                    ),
                    rx.el.div(
                        rx.foreach(MemeState.meme_suggestions, suggestion_chip),
                        class_name="flex flex-wrap justify-center gap-2",
                    ),
                    class_name="w-full p-4",
                ),
            ),
        ),
        rx.el.div(
            rx.el.button(
                rx.icon("pencil", size=20),
                "Edit Text",
                on_click=MemeState.toggle_text_dialog,
                class_name="flex items-center gap-2 bg-gray-700 text-white font-bold py-3 px-6 rounded-full shadow-md hover:bg-gray-800 hover:shadow-lg transition-all duration-300",
            ),
            rx.el.button(
                rx.icon("download", size=20),
                "Download",
                on_click=MemeState.download_meme,
                class_name="flex items-center gap-2 bg-orange-500 text-white font-bold py-3 px-6 rounded-full shadow-md hover:bg-orange-600 hover:shadow-lg transition-all duration-300",
            ),
            class_name="flex justify-center gap-4 mt-6",
        ),
        class_name="w-full",
    )