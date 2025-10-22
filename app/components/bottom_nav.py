import reflex as rx
from app.state import MemeState


def nav_button(
    icon: str, label: str, is_active: bool, on_click: rx.event.EventType
) -> rx.Component:
    """A single navigation button for the bottom bar."""
    return rx.el.button(
        rx.el.div(
            rx.icon(
                icon,
                size=24,
                class_name=rx.cond(is_active, "text-orange-900", "text-gray-600"),
            ),
            class_name=rx.cond(
                is_active,
                "bg-orange-200 rounded-full p-3 transition-all duration-300",
                "p-3",
            ),
        ),
        rx.el.span(
            label,
            class_name=rx.cond(
                is_active,
                "text-orange-900 font-semibold text-xs",
                "text-gray-700 text-xs",
            ),
        ),
        on_click=on_click,
        class_name="flex flex-col items-center justify-center gap-1 w-full h-full transition-colors duration-300",
    )


def bottom_nav() -> rx.Component:
    """The bottom navigation bar for the app."""
    return rx.el.div(
        nav_button(
            "home",
            "Home",
            MemeState.active_view == "home",
            lambda: MemeState.set_active_view("home"),
        ),
        nav_button(
            "gallery-vertical-end",
            "Gallery",
            MemeState.active_view == "gallery",
            lambda: MemeState.set_active_view("gallery"),
        ),
        nav_button(
            "settings",
            "Settings",
            MemeState.active_view == "settings",
            lambda: MemeState.set_active_view("settings"),
        ),
        class_name="fixed bottom-0 left-0 right-0 h-20 bg-gray-50 flex justify-around items-center border-t border-gray-200 shadow-[0_-1px_3px_rgba(0,0,0,0.05)]",
    )