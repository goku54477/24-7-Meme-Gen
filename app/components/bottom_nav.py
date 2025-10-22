import reflex as rx
from app.state import MemeState


def nav_button(icon: str, label: str, view: str) -> rx.Component:
    is_active = MemeState.active_view == view
    return rx.el.button(
        rx.icon(icon, class_name="size-7 transition-all duration-300"),
        rx.cond(
            is_active,
            rx.el.span(label, class_name="text-[10px] font-bold"),
            rx.el.span(class_name="text-[10px]"),
        ),
        on_click=lambda: MemeState.set_active_view(view),
        class_name=rx.cond(
            is_active,
            "flex flex-col items-center justify-center gap-1 w-20 h-12 text-white bg-white/20 rounded-full transition-all duration-300 scale-110",
            "flex flex-col items-center justify-center gap-1 w-16 h-16 text-gray-300 transition-all duration-300",
        ),
    )


def bottom_nav() -> rx.Component:
    return rx.el.div(
        nav_button("home", "Home", "home"),
        nav_button("gallery-vertical-end", "Gallery", "gallery"),
        nav_button("settings", "Settings", "settings"),
        class_name="fixed bottom-0 left-0 right-0 h-24 bg-black/30 backdrop-blur-xl border-t border-white/10 flex justify-evenly items-center shadow-[0_-4px_20px_rgba(0,0,0,0.2)]",
    )