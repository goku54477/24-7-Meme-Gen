#!/bin/bash

# Vercel Deployment Script for MEME BLASTER
# This script automates the Vercel deployment process

set -e  # Exit on error

echo "🎨 MEME BLASTER - Vercel Deployment"
echo "===================================="
echo ""

# Check if vercel CLI is installed
if ! command -v vercel &> /dev/null; then
    echo "❌ Vercel CLI is not installed!"
    echo "   Install it with: npm i -g vercel"
    echo ""
    echo "   After installing, run this script again."
    exit 1
fi

# Check if vercel.json exists
if [ ! -f "vercel.json" ]; then
    echo "❌ vercel.json not found!"
    echo "   Make sure you're in the vercel-deploy directory."
    exit 1
fi

# Check if backend URL is configured
if grep -q "YOUR-BACKEND-URL-HERE" vercel.json; then
    echo "⚠️  WARNING: Backend URL not configured!"
    echo ""
    echo "   Before deploying, you need to:"
    echo "   1. Deploy your backend to Render (see README.md)"
    echo "   2. Update vercel.json with your backend URL"
    echo ""
    echo "   Current vercel.json contains: YOUR-BACKEND-URL-HERE"
    echo ""
    read -p "   Have you deployed the backend and updated vercel.json? (y/N) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo ""
        echo "   Please complete backend deployment first:"
        echo "   1. Go to https://render.com"
        echo "   2. Create a Web Service from your repository"
        echo "   3. Add GOOGLE_API_KEY environment variable"
        echo "   4. Copy your backend URL"
        echo "   5. Update vercel.json in this directory"
        echo ""
        exit 1
    fi
fi

# Show pre-deployment checklist
echo ""
echo "📋 Pre-Deployment Checklist:"
echo "   ✅ Frontend exported and ready"
echo "   ✅ vercel.json configured"
echo ""
read -p "   Ready to deploy to Vercel? (y/N) " -n 1 -r
echo

if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "   Deployment cancelled."
    exit 0
fi

echo ""
echo "🚀 Deploying to Vercel..."
echo ""

# Deploy to Vercel
vercel --prod

echo ""
echo "✅ Deployment complete!"
echo ""
echo "📋 Next steps:"
echo "   1. Visit your deployment URL (shown above)"
echo "   2. Test image upload"
echo "   3. Test AI meme generation"
echo "   4. Test meme download"
echo ""
echo "💡 Tips:"
echo "   - Add a custom domain in Vercel Dashboard"
echo "   - Monitor usage in Vercel Analytics"
echo "   - Check backend logs in Render Dashboard"
echo ""
echo "🎉 Your meme generator is now live!"
echo ""