# Backend Deployment Guide - Render

This guide walks you through deploying the MEME BLASTER backend to Render.

## Prerequisites

- GitHub account (or GitLab/Bitbucket)
- Render account (create free at https://render.com)
- Google Gemini API Key: `AIzaSyCszFeBHnfLEDnBWCLDzZ7zmBXkxF2hyg8`

## Step-by-Step Deployment

### 1. Prepare Your Repository

Ensure your code is pushed to a Git repository:

```bash
# If not already initialized
git init
git add .
git commit -m "Prepare for deployment"
git remote add origin <your-github-repo-url>
git push -u origin main
```

### 2. Create Render Account

1. Go to https://render.com
2. Click "Get Started" or "Sign Up"
3. Sign up with GitHub (recommended) or email

### 3. Create New Web Service

1. **Dashboard**: Click "New +" button in the top right
2. **Select**: Choose "Web Service"
3. **Connect Repository**:
   - If first time: Click "Connect GitHub" and authorize Render
   - Select your repository from the list
   - Or use "Public Git Repository" if repo is public

### 4. Configure Web Service

Fill in the following settings:

**Basic Settings:**
```
Name: meme-blaster-backend
  (or any name you prefer - will be part of your URL)

Region: Oregon (US West)
  (choose closest to your target users)

Branch: main
  (or your default branch)

Root Directory: 
  (leave blank if deploying from repository root)

Runtime: Python 3
```

**Build & Deploy Settings:**
```
Build Command:
pip install -r requirements.txt && reflex init

Start Command:
reflex run --env prod --backend-only --backend-port 8000
```

**Instance Type:**
```
Free
  (or upgrade to Starter $7/month for always-on)
```

### 5. Add Environment Variables

Scroll down to "Environment Variables" section:

**Click "Add Environment Variable":**
```
Key: GOOGLE_API_KEY
Value: AIzaSyCszFeBHnfLEDnBWCLDzZ7zmBXkxF2hyg8
```

**Optional - Add more if needed:**
```
Key: PYTHON_VERSION
Value: 3.11

Key: PORT
Value: 8000
```

### 6. Advanced Settings (Optional)

Expand "Advanced" section if needed:

**Auto-Deploy:**
- ✅ Yes (recommended - auto-deploys on git push)

**Docker:**
- Leave unchecked (not needed for Python apps)

**Health Check Path:**
```
/
  (Render will ping this to check if backend is alive)
```

### 7. Create Web Service

1. Click "Create Web Service" button at the bottom
2. Render will start building your application
3. Wait 3-5 minutes for initial deployment

### 8. Monitor Deployment

You'll see:
- **Build Logs**: Shows `pip install` and build process
- **Deploy Logs**: Shows application starting
- **Status**: Will change from "Building" → "Deploying" → "Live"

**Watch for these logs:**
```
==> Building...
==> pip install -r requirements.txt
==> reflex init
==> Starting server...
==> Your service is live 🎉
```

### 9. Get Your Backend URL

Once deployed, you'll see:
```
https://meme-blaster-backend.onrender.com
```

**Copy this URL** - you'll need it for Vercel configuration!

### 10. Test Backend

**Visit your backend URL:**
- Open in browser: `https://your-backend-url.onrender.com`
- You should see the Reflex backend response
- No errors should appear

**Check logs:**
- Go to "Logs" tab in Render Dashboard
- Look for any errors or warnings
- Backend should show "Running on 0.0.0.0:8000"

## Configuration Files Reference

### requirements.txt (should exist in your repo)
```
reflex==0.8.15a1
openai
google-genai
pillow
PyGithub
gunicorn
```

### render.yaml (optional - for infrastructure as code)

You can create this file for easier redeployment:

```yaml
services:
  - type: web
    name: meme-blaster-backend
    runtime: python
    buildCommand: pip install -r requirements.txt && reflex init
    startCommand: reflex run --env prod --backend-only --backend-port 8000
    envVars:
      - key: GOOGLE_API_KEY
        value: AIzaSyCszFeBHnfLEDnBWCLDzZ7zmBXkxF2hyg8
      - key: PYTHON_VERSION
        value: '3.11'
      - key: PORT
        value: '8000'
```

## Troubleshooting

### Build Fails

**Error: "Could not find requirements.txt"**
- Solution: Ensure `requirements.txt` is in repository root
- Or set "Root Directory" if in subfolder

**Error: "Module not found"**
- Solution: Add missing package to `requirements.txt`

**Error: "reflex: command not found"**
- Solution: Check build command includes `pip install -r requirements.txt`

### Deploy Succeeds But App Doesn't Start

**Check Logs for:**
- Port binding issues
- Missing environment variables
- Python version mismatch

**Common fixes:**
```bash
# Ensure start command uses correct port
reflex run --env prod --backend-only --backend-port $PORT

# Or explicitly use 8000
reflex run --env prod --backend-only --backend-port 8000
```

### App Works But AI Generation Fails

**Check:**
- ✅ `GOOGLE_API_KEY` is set correctly
- ✅ API key has no extra spaces
- ✅ API key is valid (test at https://aistudio.google.com)

**Check Google Cloud Console:**
- Enable Gemini API if not enabled
- Check quota limits
- Verify billing is set up (if using paid tier)

### Free Tier Limitations

**Cold Starts:**
- Free tier spins down after 15 minutes of inactivity
- First request after idle takes 30-60 seconds
- Solution: Upgrade to Starter ($7/month) for always-on

**Usage Limits:**
- Free tier: 750 hours/month
- Usually enough for hobby projects
- Monitor usage in Dashboard

## Updating Your Backend

When you make code changes:

1. **Push to Git:**
   ```bash
   git add .
   git commit -m "Update backend"
   git push
   ```

2. **Auto-Deploy:**
   - Render automatically detects the push
   - Rebuilds and redeploys
   - Takes 3-5 minutes

3. **Manual Deploy:**
   - Go to Dashboard → Your Service
   - Click "Manual Deploy" → "Deploy latest commit"

## Environment Variables Management

**To Update:**
1. Go to Dashboard → Your Service
2. Click "Environment" in left sidebar
3. Edit or add variables
4. Click "Save Changes"
5. Render will automatically redeploy

## Monitoring & Logs

**View Logs:**
- Dashboard → Your Service → Logs
- Shows real-time output
- Search and filter available

**Metrics:**
- Dashboard → Your Service → Metrics
- CPU usage
- Memory usage
- Request count

**Alerts (Paid Plans):**
- Set up email alerts for errors
- Monitor uptime

## Scaling

**Free Tier:**
- Single instance
- Shared CPU
- 512 MB RAM

**Starter ($7/month):**
- Always-on (no cold starts)
- 0.5 CPU
- 512 MB RAM

**Standard ($25/month+):**
- Dedicated CPU
- More RAM
- Multiple instances
- Auto-scaling

## Alternative Backend Hosts

If Render doesn't work for you:

### Railway (https://railway.app)
- Similar to Render
- $5/month with credits
- Auto-detects Python

### Fly.io (https://fly.io)
- More complex setup
- Free tier with credit card
- Global edge deployment

### Heroku (https://heroku.com)
- No free tier anymore
- Starts at $5/month
- Well-documented

## Next Steps

After backend is deployed:

1. ✅ Copy your backend URL
2. ✅ Update `/app/vercel-deploy/vercel.json` with the URL
3. ✅ Deploy frontend to Vercel
4. ✅ Test the complete application

See `VERCEL_QUICK_START.md` for frontend deployment.

---

**Backend deployed? Let's deploy the frontend! →** Go back to `/app/vercel-deploy/` and follow the README.