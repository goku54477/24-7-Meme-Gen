import reflex as rx
from app.state import MemeState


def nav_button(
    icon: str, label: str, emoji: str, is_active: bool, on_click: rx.event.EventType
) -> rx.Component:
    """A single navigation button for the bottom bar."""
    return rx.el.button(
        rx.el.div(
            rx.icon(
                icon,
                size=28,
                class_name=rx.cond(is_active, "text-orange-900", "text-gray-600"),
            ),
            class_name=rx.cond(
                is_active,
                "bg-orange-300 rounded-full p-3 transition-all duration-300 transform scale-110",
                "p-3",
            ),
        ),
        rx.el.span(
            f"{label} {emoji}",
            class_name=rx.cond(
                is_active,
                "text-orange-900 font-bold text-sm",
                "text-gray-700 text-sm font-medium",
            ),
        ),
        on_click=on_click,
        class_name="flex flex-col items-center justify-center gap-1 w-full h-full transition-all duration-300 focus:outline-none",
    )


def bottom_nav() -> rx.Component:
    """The bottom navigation bar for the app."""
    return rx.el.div(
        nav_button(
            "home",
            "Home",
            "🏠",
            MemeState.active_view == "home",
            lambda: MemeState.set_active_view("home"),
        ),
        nav_button(
            "gallery-vertical-end",
            "Gallery",
            "✨",
            MemeState.active_view == "gallery",
            lambda: MemeState.set_active_view("gallery"),
        ),
        nav_button(
            "settings",
            "Settings",
            "⚙️",
            MemeState.active_view == "settings",
            lambda: MemeState.set_active_view("settings"),
        ),
        class_name="fixed bottom-0 left-0 right-0 h-24 bg-gray-100 flex justify-around items-center border-t-2 border-gray-200 shadow-[0_-2px_10px_rgba(0,0,0,0.08)]",
    )