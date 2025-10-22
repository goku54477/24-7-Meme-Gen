import reflex as rx


def header() -> rx.Component:
    return rx.el.header(
        rx.el.div(
            rx.image(src="logo.jpg", class_name="size-16 rounded-full object-cover border-2 border-black shadow-lg"),
            rx.el.h1(
                "MEME BLASTER",
                class_name="text-5xl font-black font-['Bangers'] action-lines",
                style={
                    "background": "linear-gradient(90deg, #FFE600 0%, #FF1493 25%, #00FF00 50%, #00D4FF 75%, #FFE600 100%)",
                    "WebkitBackgroundClip": "text",
                    "WebkitTextFillColor": "transparent",
                    "backgroundClip": "text",
                    "textShadow": "4px 4px 0px #000, -2px -2px 0px #000, 2px -2px 0px #000, -2px 2px 0px #000, 2px 2px 0px #000",
                    "WebkitTextStroke": "3px #000",
                    "paintOrder": "stroke fill",
                    "letterSpacing": "0.1em"
                },
            ),
            class_name="flex items-center justify-center gap-3",
        ),
        class_name="fixed top-0 left-0 right-0 z-10 flex items-center justify-center h-24 bg-[#ff6b35]/80 backdrop-blur-sm border-b-4 border-black halftone-bg shadow-lg",
    )