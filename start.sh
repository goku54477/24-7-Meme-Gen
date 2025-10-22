#!/bin/bash

# MEME BLASTER Startup Script

echo "🎨 Starting MEME BLASTER..."

# Check if GOOGLE_API_KEY is set
if [ -z "$GOOGLE_API_KEY" ]; then
    echo "⚠️  Warning: GOOGLE_API_KEY environment variable is not set!"
    echo "   AI meme generation will not work without it."
    echo "   Set it with: export GOOGLE_API_KEY='your-key-here'"
fi

# Check if reflex is installed
if ! command -v reflex &> /dev/null; then
    echo "Installing dependencies..."
    pip install -r requirements.txt
fi

# Initialize reflex if .web directory doesn't exist
if [ ! -d ".web" ]; then
    echo "Initializing Reflex..."
    reflex init
fi

# Start the app
echo "🚀 Launching app..."
reflex run --env prod
