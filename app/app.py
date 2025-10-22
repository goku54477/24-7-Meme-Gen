import reflex as rx
from app.state import MemeState
from app.components.header import header
from app.components.bottom_nav import bottom_nav
from app.components.image_preview import image_preview
from app.components.meme_actions import meme_actions
from app.components.text_edit_dialog import text_edit_dialog


def fab_upload() -> rx.Component:
    """Floating Action Button for uploading an image."""
    return rx.upload.root(
        rx.el.button(
            rx.icon("camera", size=32),
            class_name="w-20 h-20 bg-gradient-to-br from-orange-400 to-pink-500 text-white rounded-full flex items-center justify-center shadow-2xl hover:from-orange-500 hover:to-pink-600 focus:outline-none focus:ring-4 focus:ring-orange-300 transition-all duration-300 transform hover:scale-110 active:scale-95 animate-pulse",
        ),
        id="camera_upload",
        on_drop=MemeState.handle_upload(rx.upload_files(upload_id="camera_upload")),
        accept={"image/*": []},
        class_name="fixed bottom-24 right-4 z-20",
    )


def home_view() -> rx.Component:
    """The main view of the application where users create memes."""
    return rx.el.div(
        rx.cond(
            MemeState.has_image,
            rx.el.div(
                image_preview(),
                meme_actions(),
                rx.el.button(
                    "CREATE NEW MEME 🚀",
                    on_click=MemeState.clear_selection,
                    class_name="mt-6 text-orange-500 font-bold hover:underline text-lg transition-transform hover:scale-105",
                ),
                class_name="flex flex-col items-center gap-6 w-full px-4",
            ),
            rx.el.div(
                rx.icon("image-plus", size=80, class_name="text-gray-400"),
                rx.el.h2(
                    "WHERE'S THE MEME? 👀",
                    class_name="text-4xl font-extrabold text-gray-800 mt-6 tracking-tighter",
                ),
                rx.el.p(
                    "Tap that orange button and let's get memeing! 🚀",
                    class_name="text-gray-500 mt-2 text-lg font-medium",
                ),
                class_name="flex flex-col items-center justify-center text-center h-full p-4",
            ),
        ),
        class_name="flex-1 flex items-center justify-center w-full",
    )


def index() -> rx.Component:
    """The main page of the meme generator app."""
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
                            "Gallery Coming Soon... 갤러리 ✨",
                            class_name="text-center text-gray-500 font-bold text-2xl",
                        ),
                    ),
                    (
                        "settings",
                        rx.el.p(
                            "Settings Coming Soon... 설정 ⚙️",
                            class_name="text-center text-gray-500 font-bold text-2xl",
                        ),
                    ),
                    home_view(),
                ),
                class_name="pt-20 pb-20 w-full flex-1 flex flex-col",
            ),
            bottom_nav(),
            fab_upload(),
            text_edit_dialog(),
            class_name="relative flex flex-col min-h-screen w-full bg-gray-50 items-center",
        ),
        class_name="font-['Inter']",
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(index, route="/")