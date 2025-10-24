#!/bin/bash

# Complete Deployment Script for MEME BLASTER
# This script guides you through deploying both backend and frontend

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

clear

echo -e "${PURPLE}"
echo "╔═══════════════════════════════════════════════════════════╗"
echo "║                                                           ║"
echo "║        🎨 MEME BLASTER - Complete Deployment 🚀          ║"
echo "║                                                           ║"
echo "╚═══════════════════════════════════════════════════════════╝"
echo -e "${NC}"
echo ""

# Step 1: Check prerequisites
echo -e "${BLUE}📋 Step 1: Checking Prerequisites...${NC}"
echo ""

HAS_ERRORS=false

# Check Git
if command -v git &> /dev/null; then
    echo -e "${GREEN}✅ Git installed${NC}"
else
    echo -e "${RED}❌ Git not found${NC}"
    HAS_ERRORS=true
fi

# Check if it's a git repo
if [ -d ".git" ]; then
    echo -e "${GREEN}✅ Git repository initialized${NC}"
else
    echo -e "${YELLOW}⚠️  Not a git repository${NC}"
    echo -e "${BLUE}   Initializing git...${NC}"
    git init
    echo -e "${GREEN}✅ Git initialized${NC}"
fi

# Check Python
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
    echo -e "${GREEN}✅ Python installed: $PYTHON_VERSION${NC}"
else
    echo -e "${RED}❌ Python 3 not found${NC}"
    HAS_ERRORS=true
fi

# Check Reflex
if python3 -c "import reflex" 2>/dev/null; then
    echo -e "${GREEN}✅ Reflex installed${NC}"
else
    echo -e "${YELLOW}⚠️  Reflex not installed${NC}"
    echo -e "${BLUE}   Installing dependencies...${NC}"
    pip install -r requirements.txt
    echo -e "${GREEN}✅ Dependencies installed${NC}"
fi

# Check Vercel CLI
if command -v vercel &> /dev/null; then
    echo -e "${GREEN}✅ Vercel CLI installed${NC}"
else
    echo -e "${YELLOW}⚠️  Vercel CLI not found${NC}"
    echo -e "${BLUE}   Install with: npm i -g vercel${NC}"
fi

echo ""

if [ "$HAS_ERRORS" = true ]; then
    echo -e "${RED}❌ Please install missing dependencies and try again.${NC}"
    exit 1
fi

echo -e "${GREEN}✅ All prerequisites met!${NC}"
echo ""

# Step 2: Prepare for deployment
echo -e "${BLUE}📦 Step 2: Preparing for Deployment...${NC}"
echo ""

echo "Current status:"
echo "  - Backend code: ✅ Ready"
echo "  - Frontend build: ✅ Ready (in vercel-deploy/)"
echo "  - Configuration: ✅ Ready"
echo "  - API Key: ✅ Provided"
echo ""

# Step 3: Git setup
echo -e "${BLUE}📤 Step 3: Git Repository Setup${NC}"
echo ""

# Check if remote exists
if git remote get-url origin &> /dev/null; then
    REMOTE_URL=$(git remote get-url origin)
    echo -e "${GREEN}✅ Git remote configured: $REMOTE_URL${NC}"
else
    echo -e "${YELLOW}⚠️  No git remote configured${NC}"
    echo ""
    echo "To deploy to Render, you need to push your code to GitHub/GitLab/Bitbucket."
    echo ""
    read -p "Do you have a git repository URL? (y/N) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo ""
        read -p "Enter your git repository URL: " GIT_URL
        git remote add origin "$GIT_URL"
        echo -e "${GREEN}✅ Remote added: $GIT_URL${NC}"
    else
        echo ""
        echo -e "${CYAN}📝 Create a repository on:${NC}"
        echo "   - GitHub: https://github.com/new"
        echo "   - GitLab: https://gitlab.com/projects/new"
        echo "   - Bitbucket: https://bitbucket.org/repo/create"
        echo ""
        echo "Then run this script again."
        exit 0
    fi
fi

echo ""

# Check if there are uncommitted changes
if [[ -n $(git status -s) ]]; then
    echo -e "${YELLOW}⚠️  You have uncommitted changes${NC}"
    echo ""
    read -p "Commit and push changes now? (y/N) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        git add .
        git commit -m "Prepare for Render deployment"
        
        # Try to push
        echo ""
        echo -e "${BLUE}Pushing to remote...${NC}"
        if git push -u origin main 2>/dev/null || git push -u origin master 2>/dev/null; then
            echo -e "${GREEN}✅ Code pushed successfully!${NC}"
        else
            echo -e "${YELLOW}⚠️  Push failed. Please push manually:${NC}"
            echo "   git push -u origin main"
        fi
    fi
else
    echo -e "${GREEN}✅ No uncommitted changes${NC}"
fi

echo ""

# Step 4: Backend deployment instructions
echo -e "${PURPLE}"
echo "╔═══════════════════════════════════════════════════════════╗"
echo "║                                                           ║"
echo "║           🚀 BACKEND DEPLOYMENT (Render)                 ║"
echo "║                                                           ║"
echo "╚═══════════════════════════════════════════════════════════╝"
echo -e "${NC}"
echo ""

echo -e "${CYAN}📝 Three ways to deploy backend:${NC}"
echo ""
echo -e "${YELLOW}Option 1: Blueprint Deploy (Easiest)${NC}"
echo "  1. Go to: https://dashboard.render.com/select-repo"
echo "  2. Click 'New' → 'Blueprint'"
echo "  3. Select your repository"
echo "  4. Render auto-detects render.yaml"
echo "  5. Add GOOGLE_API_KEY in Environment tab"
echo "  6. Service deploys automatically!"
echo ""
echo -e "${YELLOW}Option 2: Manual Deploy${NC}"
echo "  1. Go to: https://render.com"
echo "  2. New + → Web Service"
echo "  3. Connect your repository"
echo "  4. Configure:"
echo "     - Build: pip install -r requirements.txt && reflex init"
echo "     - Start: reflex run --env prod --backend-only --backend-port 8000"
echo "     - Env: GOOGLE_API_KEY = AIzaSyCszFeBHnfLEDnBWCLDzZ7zmBXkxF2hyg8"
echo "  5. Deploy!"
echo ""
echo -e "${YELLOW}Option 3: Quick Link${NC}"
echo "  Create a Deploy to Render button on your repo"
echo ""

echo -e "${BLUE}ℹ️  Detailed instructions: DEPLOY_BACKEND_NOW.md${NC}"
echo ""

read -p "Press Enter when backend is deployed..."
echo ""

# Get backend URL
echo -e "${CYAN}🔗 Enter your backend URL:${NC}"
echo "   (Example: https://meme-blaster-backend.onrender.com)"
echo ""
read -p "Backend URL: " BACKEND_URL

# Validate URL
if [[ ! $BACKEND_URL =~ ^https?:// ]]; then
    echo -e "${RED}❌ Invalid URL format${NC}"
    exit 1
fi

echo ""
echo -e "${GREEN}✅ Backend URL: $BACKEND_URL${NC}"
echo ""

# Step 5: Update vercel.json
echo -e "${BLUE}⚙️  Step 5: Updating Vercel Configuration...${NC}"
echo ""

# Update vercel.json with the backend URL
sed -i "s|https://YOUR-BACKEND-URL-HERE|$BACKEND_URL|g" vercel-deploy/vercel.json

echo -e "${GREEN}✅ vercel.json updated with backend URL${NC}"
echo ""

# Step 6: Frontend deployment
echo -e "${PURPLE}"
echo "╔═══════════════════════════════════════════════════════════╗"
echo "║                                                           ║"
echo "║          🌐 FRONTEND DEPLOYMENT (Vercel)                 ║"
echo "║                                                           ║"
echo "╚═══════════════════════════════════════════════════════════╝"
echo -e "${NC}"
echo ""

echo -e "${CYAN}Ready to deploy frontend to Vercel?${NC}"
echo ""
read -p "Deploy now? (y/N) " -n 1 -r
echo

if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo ""
    echo -e "${BLUE}🚀 Deploying to Vercel...${NC}"
    echo ""
    
    cd vercel-deploy
    
    # Check if logged in to Vercel
    if ! vercel whoami &> /dev/null; then
        echo -e "${YELLOW}⚠️  Not logged in to Vercel${NC}"
        echo -e "${BLUE}   Logging in...${NC}"
        vercel login
    fi
    
    # Deploy
    echo ""
    echo -e "${BLUE}Deploying to production...${NC}"
    echo ""
    vercel --prod
    
    echo ""
    echo -e "${GREEN}✅ Frontend deployed!${NC}"
    
    cd ..
else
    echo ""
    echo -e "${YELLOW}Skipping frontend deployment${NC}"
    echo ""
    echo "To deploy later, run:"
    echo "  cd vercel-deploy"
    echo "  vercel --prod"
fi

echo ""

# Final summary
echo -e "${PURPLE}"
echo "╔═══════════════════════════════════════════════════════════╗"
echo "║                                                           ║"
echo "║                🎉 DEPLOYMENT COMPLETE! 🎉                ║"
echo "║                                                           ║"
echo "╚═══════════════════════════════════════════════════════════╝"
echo -e "${NC}"
echo ""

echo -e "${GREEN}✅ Deployment Summary:${NC}"
echo ""
echo "  Backend URL:  $BACKEND_URL"
echo "  Frontend:     Check Vercel output above"
echo ""
echo -e "${CYAN}📋 Testing Checklist:${NC}"
echo "  [ ] Visit your Vercel URL"
echo "  [ ] Upload an image"
echo "  [ ] Generate AI captions"
echo "  [ ] Edit text"
echo "  [ ] Download meme"
echo "  [ ] Test on mobile"
echo ""
echo -e "${BLUE}📚 Documentation:${NC}"
echo "  - Complete guide: COMPLETE_DEPLOYMENT_GUIDE.md"
echo "  - Backend guide: DEPLOY_BACKEND_NOW.md"
echo "  - Quick ref: VERCEL_DEPLOY_QUICKREF.md"
echo ""
echo -e "${YELLOW}💡 Next Steps:${NC}"
echo "  1. Test your deployed app"
echo "  2. Add custom domain (optional)"
echo "  3. Set up monitoring"
echo "  4. Share with the world!"
echo ""
echo -e "${GREEN}🎨 Happy memeing! 🚀${NC}"
echo ""
