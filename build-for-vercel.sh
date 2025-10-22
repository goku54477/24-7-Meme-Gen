#!/bin/bash

# Build script for Vercel deployment
# This script exports the frontend and prepares it for Vercel

set -e  # Exit on error

echo "🎨 MEME BLASTER - Vercel Build Script"
echo "======================================"

# Check if reflex is installed
if ! command -v reflex &> /dev/null; then
    echo "❌ Reflex is not installed!"
    echo "   Install it with: pip install -r requirements.txt"
    exit 1
fi

# Clean previous builds
echo "🧹 Cleaning previous builds..."
rm -rf vercel-deploy
rm -f frontend.zip

# Export frontend
echo "📦 Exporting frontend..."
reflex export --frontend-only

# Check if export was successful
if [ ! -f "frontend.zip" ]; then
    echo "❌ Export failed! frontend.zip not found."
    exit 1
fi

# Create deployment directory
echo "📁 Creating deployment directory..."
mkdir -p vercel-deploy
cd vercel-deploy

# Extract frontend
echo "📂 Extracting frontend..."
unzip -q ../frontend.zip

# Copy Vercel configuration
if [ -f "../vercel.json" ]; then
    echo "⚙️  Copying vercel.json..."
    cp ../vercel.json .
else
    echo "⚠️  Warning: vercel.json not found in root directory"
    echo "   Creating a basic vercel.json..."
    cat > vercel.json << 'EOF'
{
  "version": 2,
  "framework": "nextjs",
  "routes": [
    {
      "src": "/api/(.*)",
      "dest": "https://YOUR-BACKEND-URL/api/$1"
    },
    {
      "src": "/(.*)",
      "dest": "/$1"
    }
  ]
}
EOF
    echo "⚠️  Remember to update YOUR-BACKEND-URL in vercel.json!"
fi

cd ..

echo ""
echo "✅ Build complete!"
echo ""
echo "📋 Next steps:"
echo "   1. Deploy your backend to Render, Railway, or Fly.io"
echo "   2. Update vercel-deploy/vercel.json with your backend URL"
echo "   3. cd vercel-deploy"
echo "   4. vercel --prod"
echo ""
echo "📚 For detailed instructions, see VERCEL_QUICK_START.md"
