import reflex as rx
from app.state import MemeState


def meme_text_overlay(text: rx.Var[str], position_class: str) -> rx.Component:
    return rx.el.div(
        rx.el.p(
            text,
            class_name="text-white font-black text-4xl uppercase text-center tracking-wide leading-tight",
            style={
                "textShadow": "3px 3px 0 #000, -1px -1px 0 #000, 1px -1px 0 #000, -1px 1px 0 #000, 1px 1px 0 #000"
            },
        ),
        class_name=f"absolute {position_class} left-2 right-2 p-2",
    )


def image_preview() -> rx.Component:
    return rx.el.div(
        rx.image(
            src=rx.get_upload_url(MemeState.image_url),
            class_name="object-cover h-full w-full",
        ),
        meme_text_overlay(MemeState.top_text, "top-0"),
        meme_text_overlay(MemeState.bottom_text, "bottom-0"),
        class_name="relative w-full max-w-md aspect-square bg-gray-900 overflow-hidden font-['Bangers'] comic-panel hover:shadow-[0_0_20px_#00d4ff]",
    )