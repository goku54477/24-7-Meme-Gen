import reflex as rx
from app.state import MemeState


def meme_text_overlay(text: rx.Var[str], position_class: str) -> rx.Component:
    return rx.el.div(
        rx.el.p(
            text,
            class_name="text-white font-extrabold text-3xl uppercase text-center tracking-wide",
            style={
                "WebkitTextStroke": "1.5px black",
                "textShadow": "-2px -2px 0 #000, 2px -2px 0 #000, -2px 2px 0 #000, 2px 2px 0 #000",
            },
        ),
        class_name=f"absolute {position_class} left-4 right-4 p-2",
    )


def image_preview() -> rx.Component:
    """Component to display the uploaded image with meme text overlay."""
    return rx.el.div(
        rx.image(
            src=rx.get_upload_url(MemeState.image_url),
            class_name="rounded-lg object-contain h-full w-full",
        ),
        meme_text_overlay(MemeState.top_text, "top-2"),
        meme_text_overlay(MemeState.bottom_text, "bottom-2"),
        class_name="relative w-full max-w-md aspect-square bg-gray-900 rounded-lg overflow-hidden shadow-lg border border-gray-700 font-['Impact']",
    )