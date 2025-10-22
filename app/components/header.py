import reflex as rx


def header() -> rx.Component:
    return rx.el.header(
        rx.el.div(
            rx.image(src="logo.jpg", class_name="size-16 rounded-full object-cover border-2 border-black shadow-lg"),
            rx.el.h1(
                "MEME BLASTER",
                class_name="text-4xl font-black text-white tracking-tighter font-['Bangers'] action-lines",
                style={
                    "textShadow": "3px 3px 0px #000, -1px -1px 0px #000, 1px -1px 0px #000, -1px 1px 0px #000, 1px 1px 0px #000"
                },
            ),
            class_name="flex items-center justify-center gap-3",
        ),
        class_name="fixed top-0 left-0 right-0 z-10 flex items-center justify-center h-24 bg-[#ff6b35]/80 backdrop-blur-sm border-b-4 border-black halftone-bg shadow-lg",
    )