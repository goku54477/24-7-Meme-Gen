import reflex as rx
from app.state import MemeState


def text_input_field(
    label: str, value: rx.Var[str], on_change: rx.event.EventHandler
) -> rx.Component:
    """A styled text input field for the dialog."""
    return rx.el.div(
        rx.el.label(label, class_name="text-sm font-medium text-gray-700 mb-1"),
        rx.el.input(
            default_value=value,
            on_change=on_change,
            placeholder=f"Enter {label.lower()}...",
            class_name="w-full p-2 border border-gray-300 rounded-md shadow-sm focus:ring-orange-500 focus:border-orange-500",
        ),
        class_name="w-full",
    )


def text_edit_dialog() -> rx.Component:
    """Dialog for editing meme top and bottom text."""
    return rx.radix.primitives.dialog.root(
        rx.radix.primitives.dialog.trigger(rx.el.div()),
        rx.radix.primitives.dialog.overlay(
            class_name="fixed inset-0 bg-black/50 data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 z-50"
        ),
        rx.radix.primitives.dialog.content(
            rx.radix.primitives.dialog.title(
                "Edit Meme Text", class_name="text-lg font-semibold text-gray-900"
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
                        class_name="px-4 py-2 bg-gray-200 text-gray-800 rounded-md hover:bg-gray-300",
                    )
                ),
                rx.radix.primitives.dialog.close(
                    rx.el.button(
                        "Save",
                        class_name="px-4 py-2 bg-orange-500 text-white rounded-md hover:bg-orange-600",
                    )
                ),
                class_name="flex justify-end gap-3 mt-6",
            ),
            class_name="fixed left-1/2 top-1/2 z-50 w-full max-w-md -translate-x-1/2 -translate-y-1/2 rounded-xl border bg-background p-6 shadow-lg duration-200 data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[state=closed]:slide-out-to-left-1/2 data-[state=closed]:slide-out-to-top-[48%] data-[state=open]:slide-in-from-left-1/2 data-[state=open]:slide-in-from-top-[48%]",
        ),
        open=MemeState.show_text_dialog,
        on_open_change=MemeState.set_show_text_dialog,
    )