import reflex as rx
from app.state import MemeState


def suggestion_chip(text: str) -> rx.Component:
    return rx.el.button(
        text,
        on_click=lambda: MemeState.select_suggestion(text),
        class_name="suggestion-chip",
    )


def action_button(
    icon: str, text: str, on_click: rx.event.EventType, style: str
) -> rx.Component:
    return rx.el.button(
        rx.icon(icon, class_name="size-5"),
        text,
        on_click=on_click,
        class_name=f"flex items-center gap-2 font-bold py-3 px-6 rounded-full shadow-lg transition-all duration-300 transform hover:scale-105 {style}",
    )


def meme_actions() -> rx.Component:
    return rx.el.div(
        rx.match(
            MemeState.is_loading,
            (
                True,
                rx.el.div(
                    rx.spinner(class_name="text-[#ff6b35]", size="3"),
                    rx.el.p(
                        "BLASTING MEMES...",
                        class_name="text-gray-600 font-bold text-lg mt-2 font-['Bangers'] tracking-wider",
                    ),
                    class_name="flex flex-col items-center gap-4 p-8",
                ),
            ),
            rx.cond(
                MemeState.is_error,
                rx.el.div(
                    rx.icon("bomb", size=64, class_name="text-[#ff5252]"),
                    rx.el.p(
                        "MEME-POCALYPSE!",
                        class_name="text-[#ff5252] font-black text-3xl mt-4 font-['Bangers']",
                    ),
                    rx.el.button(
                        "TRY AGAIN!",
                        on_click=MemeState.generate_gemini_suggestions,
                        class_name="mt-6 bg-[#ff6b35] text-white px-6 py-3 rounded-full hover:bg-[#ffc107] font-bold text-lg font-['Bangers'] tracking-widest",
                    ),
                    class_name="flex flex-col items-center gap-2 p-8",
                ),
                rx.el.div(
                    rx.el.h3(
                        "CHOOSE YOUR CAPTION!",
                        class_name="text-2xl font-black text-gray-800 mb-4 text-center tracking-wider font-['Bangers']",
                    ),
                    rx.el.div(
                        rx.foreach(MemeState.meme_suggestions, suggestion_chip),
                        class_name="flex flex-wrap justify-center gap-3 p-2",
                    ),
                    class_name="w-full p-4 bg-gray-900/10 rounded-2xl",
                ),
            ),
        ),
        rx.el.div(
            action_button(
                "pencil",
                "EDIT",
                MemeState.toggle_text_dialog,
                "bg-[#00d4ff] text-black",
            ),
            action_button(
                "download", "SAVE", MemeState.download_meme, "bg-[#ff5252] text-white"
            ),
            class_name="flex justify-center gap-4 mt-6",
        ),
        class_name="w-full max-w-md mt-4",
    )