# 🚀 Quick Vercel Deployment Guide

This guide will help you deploy MEME BLASTER to Vercel in just a few steps.

## Prerequisites

- [Vercel CLI](https://vercel.com/download) installed: `npm i -g vercel`
- A backend hosting account (Render, Railway, or Fly.io)
- Google Gemini API key

## Step-by-Step Deployment

### 1. Export the Frontend

```bash
cd /app
reflex export --frontend-only
```

This creates `frontend.zip` with your static Next.js build.

### 2. Prepare Deployment Directory

```bash
# Create a clean directory for deployment
mkdir vercel-deploy
cd vercel-deploy

# Extract the frontend
unzip ../frontend.zip

# You should now see files like:
# .next/, public/, package.json, etc.
```

### 3. Deploy Backend First

Choose one of these platforms:

**Option A: Render (Recommended)**
1. Go to https://render.com and create account
2. Click "New +" → "Web Service"
3. Connect your Git repository
4. Configure:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `reflex run --env prod --backend-only`
   - **Environment**: Add `GOOGLE_API_KEY=your-key-here`
5. Click "Create Web Service"
6. Wait for deployment and copy your URL (e.g., `https://meme-blaster.onrender.com`)

**Option B: Railway**
1. Go to https://railway.app
2. Click "New Project" → "Deploy from GitHub"
3. Railway auto-detects Python
4. Add environment variable: `GOOGLE_API_KEY`
5. Deploy and get your URL

### 4. Configure Vercel Settings

Update `vercel.json` in your `vercel-deploy` directory:

```json
{
  "version": 2,
  "framework": "nextjs",
  "routes": [
    {
      "src": "/api/(.*)",
      "dest": "https://YOUR-BACKEND-URL.onrender.com/api/$1"
    },
    {
      "src": "/(.*)",
      "dest": "/$1"
    }
  ]
}
```

**Replace** `YOUR-BACKEND-URL.onrender.com` with your actual backend URL.

### 5. Deploy to Vercel

```bash
# Login to Vercel (first time only)
vercel login

# Deploy to production
vercel --prod
```

Follow the prompts:
- Set up and deploy? **Y**
- Which scope? Choose your account
- Link to existing project? **N**
- What's your project's name? **meme-blaster** (or your choice)
- In which directory is your code located? **./** (current directory)
- Want to override settings? **N**

### 6. Verify Deployment

After deployment completes, Vercel will show you your URL:
```
✅ Production: https://meme-blaster-xyz.vercel.app
```

Visit the URL and test:
1. Upload an image
2. Wait for AI suggestions
3. Download a meme

## Troubleshooting

### Frontend loads but AI doesn't work
- ✅ Check backend is running (visit backend URL directly)
- ✅ Verify `GOOGLE_API_KEY` is set on backend
- ✅ Check `vercel.json` has correct backend URL
- ✅ Check browser console for CORS errors

### CORS Errors
Add to your backend code:
```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://your-vercel-url.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### 404 Errors on API Calls
- Ensure `vercel.json` routes are correct
- Backend must be accessible at the URL specified
- Check backend logs for errors

### Static Build Issues
If Vercel can't build:
```bash
# Ensure you're using the exported build
ls -la .next/
# Should show: server/, static/, etc.
```

## Alternative: Reflex Cloud (Easier!)

If Vercel deployment is complex, consider using Reflex Cloud:

```bash
cd /app
reflex deploy
```

This deploys both frontend and backend automatically with zero configuration.

## Cost Considerations

**Vercel:**
- Free tier: 100GB bandwidth, unlimited personal projects
- Hobby: Free for personal use
- Pro: $20/month for commercial use

**Backend (Render Free Tier):**
- Free tier available
- Spins down after inactivity (may have cold starts)
- Upgrade to paid for always-on ($7/month)

**Google Gemini API:**
- Free tier: 15 requests per minute
- See [pricing](https://ai.google.dev/pricing) for details

## Next Steps

After successful deployment:
1. 🎨 Customize your domain in Vercel settings
2. 📊 Set up analytics
3. 🔒 Add SSL (automatic with Vercel)
4. 📈 Monitor usage and performance
5. 🚀 Share your meme generator with the world!

---

Need help? Check out:
- [Vercel Documentation](https://vercel.com/docs)
- [Reflex Documentation](https://reflex.dev/docs/)
- [Render Documentation](https://render.com/docs)
