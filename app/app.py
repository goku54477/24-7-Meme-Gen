import reflex as rx
from app.state import MemeState
from app.components.header import header
from app.components.bottom_nav import bottom_nav
from app.components.image_preview import image_preview
from app.components.meme_actions import meme_actions
from app.components.text_edit_dialog import text_edit_dialog


def fab_upload() -> rx.Component:
    return rx.upload.root(
        rx.el.button(
            rx.icon("camera", class_name="size-10 stroke-[3]"),
            rx.el.div(class_name="boom-effect"),
            class_name="fab-button group",
        ),
        id="camera_upload",
        on_drop=MemeState.handle_upload(rx.upload_files(upload_id="camera_upload")),
        accept={"image/*": []},
        class_name="fixed bottom-[100px] right-6 z-20",
    )


def home_view() -> rx.Component:
    return rx.el.div(
        rx.cond(
            MemeState.has_image,
            rx.el.div(
                image_preview(),
                meme_actions(),
                rx.el.button(
                    "NEW MEME!",
                    on_click=MemeState.clear_selection,
                    class_name="mt-8 text-sm font-bold text-gray-500 uppercase tracking-widest hover:text-pink-500 transition-colors duration-300",
                ),
                class_name="flex flex-col items-center gap-2 w-full px-4",
            ),
            rx.el.div(
                rx.el.div(
                    rx.icon("image-plus", class_name="size-12 text-gray-400"),
                    rx.el.h2(
                        "UPLOAD AN IMAGE!",
                        class_name="text-2xl font-black text-gray-700 mt-6 tracking-tighter font-['Bangers']",
                    ),
                    rx.el.p(
                        "Tap the 'BOOM' button to start memeing!",
                        class_name="text-gray-500 mt-1 text-md font-semibold",
                    ),
                    class_name="flex flex-col items-center justify-center text-center p-8 bg-white/50 backdrop-blur-lg border border-white/20 rounded-3xl shadow-lg",
                ),
                class_name="flex flex-col items-center justify-center text-center h-full p-4",
            ),
        ),
        class_name="flex-1 flex items-center justify-center w-full",
    )


def index() -> rx.Component:
    return rx.el.main(
        rx.el.div(
            header(),
            rx.el.div(
                rx.match(
                    MemeState.active_view,
                    ("home", home_view()),
                    (
                        "gallery",
                        rx.el.p(
                            "Gallery Coming Soon...",
                            class_name="text-center text-gray-500 font-bold text-2xl font-['Bangers'] tracking-wider",
                        ),
                    ),
                    (
                        "settings",
                        rx.el.p(
                            "Settings Coming Soon...",
                            class_name="text-center text-gray-500 font-bold text-2xl font-['Bangers'] tracking-wider",
                        ),
                    ),
                    home_view(),
                ),
                class_name="pt-24 pb-28 w-full flex-1 flex flex-col",
            ),
            bottom_nav(),
            fab_upload(),
            text_edit_dialog(),
            class_name="relative flex flex-col min-h-screen w-full items-center bg-gradient-mesh",
        ),
        class_name="font-['Inter'] select-none",
        id="app",
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    stylesheets=["/styles.css"],
    head_components=[
        rx.el.meta(charset="UTF-8"),
        rx.el.meta(
            name="viewport",
            content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no",
        ),
        rx.el.meta(name="theme-color", content="#8B5CF6"),
        rx.el.meta(
            name="description", content="AI-powered meme generator for mobile devices"
        ),
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Bangers&display=swap",
            rel="stylesheet",
        ),
        rx.el.link(rel="manifest", href="/manifest.json"),
        rx.el.meta(name="mobile-web-app-capable", content="yes"),
        rx.el.meta(name="apple-mobile-web-app-capable", content="yes"),
        rx.el.meta(name="apple-mobile-web-app-status-bar-style", content="default"),
        rx.el.script(src="/sw.js"),
    ],
)
app.add_page(index, route="/")