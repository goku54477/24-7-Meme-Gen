import reflex as rx
from app.state import MemeState


def text_input_field(
    label: str, value: rx.Var[str], on_change: rx.event.EventHandler
) -> rx.Component:
    return rx.el.div(
        rx.el.label(
            label,
            class_name="text-sm font-bold text-gray-400 mb-1 uppercase tracking-wider",
        ),
        rx.el.input(
            default_value=value,
            on_change=on_change,
            placeholder=f"Enter {label.lower()}...",
            class_name="w-full p-3 bg-gray-800 border-2 border-gray-700 rounded-lg text-white placeholder-gray-500 focus:ring-cyan-400 focus:border-cyan-400 focus:ring-2 transition-all",
        ),
        class_name="w-full",
    )


def text_edit_dialog() -> rx.Component:
    return rx.radix.primitives.dialog.root(
        rx.radix.primitives.dialog.trigger(rx.el.div()),
        rx.radix.primitives.dialog.overlay(
            class_name="fixed inset-0 bg-black/60 backdrop-blur-sm data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 z-50"
        ),
        rx.radix.primitives.dialog.content(
            rx.radix.primitives.dialog.title(
                "EDIT TEXT",
                class_name="text-2xl font-black text-white font-['Bangers'] tracking-wider",
            ),
            rx.el.div(
                text_input_field(
                    "Top Text", MemeState.top_text, MemeState.set_top_text
                ),
                text_input_field(
                    "Bottom Text", MemeState.bottom_text, MemeState.set_bottom_text
                ),
                class_name="flex flex-col gap-4 mt-4",
            ),
            rx.el.div(
                rx.radix.primitives.dialog.close(
                    rx.el.button(
                        "Cancel",
                        class_name="px-5 py-2 bg-gray-700 text-white font-bold rounded-lg hover:bg-gray-600 transition-colors",
                    )
                ),
                rx.radix.primitives.dialog.close(
                    rx.el.button(
                        "SAVE!",
                        class_name="px-5 py-2 bg-pink-500 text-white font-bold rounded-lg hover:bg-pink-600 transition-colors font-['Bangers'] tracking-wider text-lg",
                    )
                ),
                class_name="flex justify-end gap-3 mt-6",
            ),
            class_name="fixed left-1/2 top-1/2 z-50 w-[90%] max-w-md -translate-x-1/2 -translate-y-1/2 rounded-2xl border-4 border-black bg-gray-900 p-6 shadow-lg duration-200 data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[state=closed]:slide-out-to-left-1/2 data-[state=closed]:slide-out-to-top-[48%] data-[state=open]:slide-in-from-left-1/2 data-[state=open]:slide-in-from-top-[48%]",
        ),
        open=MemeState.show_text_dialog,
        on_open_change=MemeState.set_show_text_dialog,
    )