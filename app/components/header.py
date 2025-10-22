import reflex as rx


def header() -> rx.Component:
    return rx.el.header(
        rx.el.div(
            rx.image(src="logo.jpg", class_name="size-16 rounded-full object-cover border-2 border-black shadow-lg"),
            rx.el.h1(
                "MEME BLASTER",
                class_name="text-5xl font-black tracking-tight font-['Bangers'] action-lines",
                style={
                    "color": "#FFE600",
                    "textShadow": "4px 4px 0px #000, -2px -2px 0px #000, 2px -2px 0px #000, -2px 2px 0px #000, 2px 2px 0px #000, 6px 6px 0px rgba(0,0,0,0.3)",
                    "WebkitTextStroke": "2px #000",
                    "paintOrder": "stroke fill"
                },
            ),
            class_name="flex items-center justify-center gap-3",
        ),
        class_name="fixed top-0 left-0 right-0 z-10 flex items-center justify-center h-24 bg-[#ff6b35]/80 backdrop-blur-sm border-b-4 border-black halftone-bg shadow-lg",
    )