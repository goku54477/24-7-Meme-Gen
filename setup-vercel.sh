#!/bin/bash

# One-Click Vercel Deployment Setup
# This script prepares everything needed for Vercel deployment

set -e

echo ""
echo "██████╗ ██╗  ██╗███████╗██████╗ ████████╗██╗"
echo "██╔══██╗╚██╗██╔╝██╔════╝██╔══██╗╚══██╔══╝██║"
echo "██████╔╝ ╚████╔╝ █████╗  ██████╔╝   ██║   ██║"
echo "██╔═══╝   ╚███╔╝  ██╔══╝  ██╔═══╝    ██║   ╚═╝"
echo "██║        ╚██╔╝   ███████╗██║        ██║   ██╗"
echo "╚═╝         ╚═╝    ╚══════╝╚═╝        ╚═╝   ╚═╝"
echo ""
echo "🎨 MEME BLASTER - Complete Vercel Setup"
echo "========================================"
echo ""

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Check prerequisites
echo -e "${BLUE}🔍 Checking prerequisites...${NC}"
echo ""

HAS_ERRORS=false

# Check Python
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
    echo -e "${GREEN}✅ Python installed: $PYTHON_VERSION${NC}"
else
    echo -e "${RED}❌ Python 3 not found${NC}"
    HAS_ERRORS=true
fi

# Check pip
if command -v pip &> /dev/null || command -v pip3 &> /dev/null; then
    echo -e "${GREEN}✅ pip installed${NC}"
else
    echo -e "${RED}❌ pip not found${NC}"
    HAS_ERRORS=true
fi

# Check if dependencies are installed
if python3 -c "import reflex" 2>/dev/null; then
    REFLEX_VERSION=$(python3 -c "import reflex; print(reflex.__version__)")
    echo -e "${GREEN}✅ Reflex installed: $REFLEX_VERSION${NC}"
else
    echo -e "${YELLOW}⚠️  Reflex not installed (will install)${NC}"
fi

# Check Node/npm for Vercel CLI
if command -v npm &> /dev/null; then
    NPM_VERSION=$(npm --version)
    echo -e "${GREEN}✅ npm installed: $NPM_VERSION${NC}"
else
    echo -e "${YELLOW}⚠️  npm not found (needed for Vercel CLI)${NC}"
fi

# Check Vercel CLI
if command -v vercel &> /dev/null; then
    VERCEL_VERSION=$(vercel --version)
    echo -e "${GREEN}✅ Vercel CLI installed: $VERCEL_VERSION${NC}"
else
    echo -e "${YELLOW}⚠️  Vercel CLI not installed${NC}"
    if command -v npm &> /dev/null; then
        echo -e "${BLUE}   Install with: npm i -g vercel${NC}"
    fi
fi

# Check unzip
if command -v unzip &> /dev/null; then
    echo -e "${GREEN}✅ unzip installed${NC}"
else
    echo -e "${RED}❌ unzip not found (required for Reflex)${NC}"
    HAS_ERRORS=true
fi

echo ""

if [ "$HAS_ERRORS" = true ]; then
    echo -e "${RED}❌ Critical dependencies missing!${NC}"
    echo "Please install missing dependencies and try again."
    exit 1
fi

echo -e "${GREEN}✅ All critical dependencies found!${NC}"
echo ""

# Ask to proceed
read -p "Continue with setup? (y/N) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Setup cancelled."
    exit 0
fi

echo ""
echo -e "${BLUE}📦 Step 1: Installing Python dependencies...${NC}"
echo ""
pip install -r requirements.txt || pip3 install -r requirements.txt

echo ""
echo -e "${BLUE}⚙️  Step 2: Initializing Reflex...${NC}"
echo ""
reflex init

echo ""
echo -e "${BLUE}📬 Step 3: Exporting frontend for Vercel...${NC}"
echo ""
./build-for-vercel.sh

echo ""
echo -e "${GREEN}✅ Setup complete!${NC}"
echo ""
echo "========================================"
echo -e "${BLUE}📝 NEXT STEPS:${NC}"
echo "========================================"
echo ""
echo "1️⃣  Deploy Backend to Render:"
echo "   - Go to https://render.com"
echo "   - Create Web Service from your Git repo"
echo "   - Set GOOGLE_API_KEY environment variable"
echo "   - Copy your backend URL"
echo ""
echo "2️⃣  Update Vercel Configuration:"
echo "   - Edit: vercel-deploy/vercel.json"
echo "   - Replace YOUR-BACKEND-URL-HERE with Render URL"
echo ""
echo "3️⃣  Deploy Frontend to Vercel:"
echo "   - cd vercel-deploy"
echo "   - vercel --prod"
echo ""
echo "========================================"
echo -e "${BLUE}📚 Documentation:${NC}"
echo "========================================"
echo ""
echo "Complete Guide: ./COMPLETE_DEPLOYMENT_GUIDE.md"
echo "Backend Guide:  ./RENDER_BACKEND_DEPLOY.md"
echo "Frontend Guide: ./vercel-deploy/README.md"
echo ""
echo -e "${GREEN}🎉 Ready for deployment!${NC}"
echo ""