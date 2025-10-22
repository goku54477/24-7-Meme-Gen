import reflex as rx


def header() -> rx.Component:
    return rx.el.header(
        rx.el.div(
            rx.image(src="logo.jpg", class_name="size-16 rounded-full object-cover border-2 border-black shadow-lg"),
            rx.el.div(
                rx.el.span(
                    "MEME",
                    style={
                        "color": "#FFE600",
                        "WebkitTextStroke": "3px #000",
                        "textShadow": "5px 5px 0px #000"
                    }
                ),
                rx.el.span(
                    " ",
                ),
                rx.el.span(
                    "BLASTER",
                    style={
                        "color": "#00FF00",
                        "WebkitTextStroke": "3px #000",
                        "textShadow": "5px 5px 0px #000"
                    }
                ),
                class_name="text-5xl font-black font-['Bangers'] tracking-wider",
                style={
                    "letterSpacing": "0.15em"
                }
            ),
            class_name="flex items-center justify-center gap-3",
        ),
        class_name="fixed top-0 left-0 right-0 z-10 flex items-center justify-center h-24 bg-[#ff6b35]/80 backdrop-blur-sm border-b-4 border-black halftone-bg shadow-lg",
    )