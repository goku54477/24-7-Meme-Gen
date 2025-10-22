import reflex as rx
import asyncio
import os
from typing import Optional
import google.genai as genai
from google.genai import types
import json
import logging
from PIL import Image, ImageDraw, ImageFont
import textwrap
import time


class MemeState(rx.State):
    """Manages the state for the meme generator app."""

    image_url: str | None = None
    is_loading: bool = False
    active_view: str = "home"
    meme_suggestions: list[str] = []
    selected_meme_text: str = ""
    top_text: str = ""
    bottom_text: str = ""
    show_text_dialog: bool = False
    is_error: bool = False

    @rx.event
    async def handle_upload(self, files: list[rx.UploadFile]):
        """Handle image upload, show loader, and trigger meme generation."""
        if not files:
            return
        self.is_loading = True
        self.is_error = False
        self.meme_suggestions = []
        yield
        file = files[0]
        upload_data = await file.read()
        outfile = rx.get_upload_dir() / file.filename
        with outfile.open("wb") as f:
            f.write(upload_data)
        self.image_url = file.filename
        self.is_loading = False
        yield
        yield MemeState.generate_gemini_suggestions

    @rx.event(background=True)
    async def generate_gemini_suggestions(self):
        """Generate meme suggestions using the Gemini API."""
        async with self:
            if not self.image_url:
                self.is_error = True
                return
            self.is_loading = True
            self.is_error = False
            self.meme_suggestions = []
        yield
        try:
            api_key = os.getenv("GOOGLE_API_KEY")
            if not api_key:
                logging.error("GOOGLE_API_KEY is not set.")
                raise ValueError("GOOGLE_API_KEY is not set.")
            genai.configure(api_key=api_key)
            client = genai.GenerativeModel(model_name="gemini-1.5-flash")
            image_path = rx.get_upload_dir() / self.image_url
            with image_path.open("rb") as f:
                image_bytes = f.read()
            image_part = types.Part.from_data(data=image_bytes, mime_type="image/jpeg")
            prompt = "You are a meme caption generator. Analyze this image and suggest 4 funny, short meme captions. Each caption must have a TOP and an optional BOTTOM text, separated by a pipe character '|'. Example: 'TOP TEXT | BOTTOM TEXT' or just 'TOP TEXT'. Keep captions concise (under 10 words per line). Return a JSON array of 4 strings with no other text or markdown."
            contents = [image_part, prompt]
            response = await client.generate_content_async(contents)
            response_text = response.text.strip()
            if response_text.startswith("""on
"""):
                response_text = response_text[8:]
            elif response_text.startswith("on"):
                response_text = response_text[7:]
            elif response_text.startswith("""
"""):
                response_text = response_text[4:]
            elif response_text.startswith(""):
                response_text = response_text[3:]
            if response_text.endswith("""
"""):
                response_text = response_text[:-4]
            elif response_text.endswith(""):
                response_text = response_text[:-3]
            response_text = response_text.strip()
            suggestions = json.loads(response_text)
            async with self:
                self.meme_suggestions = suggestions
                self.is_loading = False
        except Exception as e:
            logging.exception(f"Error generating Gemini suggestions: {e}")
            async with self:
                self.is_loading = False
                self.is_error = True
            yield rx.toast(
                "Failed to generate AI suggestions. Please try again.", duration=5000
            )

    @rx.var
    def has_image(self) -> bool:
        """Check if an image has been uploaded."""
        return self.image_url is not None

    @rx.event
    def set_active_view(self, view: str):
        """Set the active view for the bottom navigation."""
        self.active_view = view

    @rx.event
    def select_suggestion(self, text: str):
        """Select a meme text suggestion and apply it."""
        parts = text.split("|")
        self.selected_meme_text = text
        self.top_text = parts[0].strip()
        self.bottom_text = parts[1].strip() if len(parts) > 1 else ""

    @rx.event
    def toggle_text_dialog(self):
        """Toggle the visibility of the meme text input dialog."""
        self.show_text_dialog = not self.show_text_dialog

    @rx.event
    def set_top_text(self, text: str):
        self.top_text = text

    @rx.event
    def set_bottom_text(self, text: str):
        self.bottom_text = text

    @rx.event
    def clear_selection(self):
        """Clear the selected image and suggestions."""
        self.image_url = None
        self.meme_suggestions = []
        self.top_text = ""
        self.bottom_text = ""
        self.is_error = False

    def _draw_text_with_stroke(
        self, draw, text, position, font, text_color="white", stroke_color="black"
    ):
        x, y = position
        stroke_width = 3
        draw.text(
            (x - stroke_width, y - stroke_width),
            text,
            font=font,
            fill=stroke_color,
            align="center",
        )
        draw.text(
            (x + stroke_width, y - stroke_width),
            text,
            font=font,
            fill=stroke_color,
            align="center",
        )
        draw.text(
            (x + stroke_width, y + stroke_width),
            text,
            font=font,
            fill=stroke_color,
            align="center",
        )
        draw.text(
            (x - stroke_width, y + stroke_width),
            text,
            font=font,
            fill=stroke_color,
            align="center",
        )
        draw.text((x, y), text, font=font, fill=text_color, align="center")

    @rx.event(background=True)
    async def download_meme(self):
        """Compose the meme image with text and provide it for download."""
        async with self:
            if not self.image_url:
                yield rx.toast("No image to download.", duration=3000)
                return
            self.is_loading = True
        yield
        try:
            image_path = rx.get_upload_dir() / self.image_url
            with Image.open(image_path).convert("RGBA") as base_image:
                txt_layer = Image.new("RGBA", base_image.size, (255, 255, 255, 0))
                draw = ImageDraw.Draw(txt_layer)
                try:
                    font_path = "assets/Bangers-Regular.ttf"
                    if not os.path.exists(font_path):
                        font_path = "arial.ttf"
                    font_size = int(base_image.width / 9)
                    font = ImageFont.truetype(font_path, font_size)
                except IOError as e:
                    logging.exception(f"Error loading font: {e}")
                    font = ImageFont.load_default()
                top_text = self.top_text.upper()
                bottom_text = self.bottom_text.upper()
                avg_char_width = (
                    sum(
                        (font.getbbox(char)[2] for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
                    )
                    / 26
                )
                max_chars = int(base_image.width * 0.9 / avg_char_width)
                wrapped_top = textwrap.fill(
                    top_text, width=max_chars if max_chars > 0 else 1
                )
                wrapped_bottom = textwrap.fill(
                    bottom_text, width=max_chars if max_chars > 0 else 1
                )
                top_text_bbox = draw.multiline_textbbox(
                    (0, 0), wrapped_top, font=font, align="center"
                )
                top_text_width = top_text_bbox[2] - top_text_bbox[0]
                x_top = (base_image.width - top_text_width) / 2
                y_top = base_image.height * 0.05
                self._draw_text_with_stroke(draw, wrapped_top, (x_top, y_top), font)
                bottom_text_bbox = draw.multiline_textbbox(
                    (0, 0), wrapped_bottom, font=font, align="center"
                )
                bottom_text_width = bottom_text_bbox[2] - bottom_text_bbox[0]
                bottom_text_height = bottom_text_bbox[3] - bottom_text_bbox[1]
                x_bottom = (base_image.width - bottom_text_width) / 2
                y_bottom = (
                    base_image.height - bottom_text_height - base_image.height * 0.05
                )
                self._draw_text_with_stroke(
                    draw, wrapped_bottom, (x_bottom, y_bottom), font
                )
                out_image = Image.alpha_composite(base_image, txt_layer)
                out_image = out_image.convert("RGB")
                timestamp = int(time.time())
                final_filename = f"meme_{timestamp}.jpg"
                out_path = rx.get_upload_dir() / final_filename
                out_image.save(out_path, "JPEG")
            async with self:
                self.is_loading = False
            yield rx.download(url=f"/_upload/{final_filename}", filename=final_filename)
            yield rx.toast("Meme ready for download!", duration=3000)
        except Exception as e:
            logging.exception(f"Error creating meme: {e}")
            async with self:
                self.is_loading = False
            yield rx.toast("Failed to create meme.", duration=5000)