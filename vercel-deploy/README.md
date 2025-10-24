# MEME BLASTER - Vercel Deployment

This directory contains the exported frontend ready for Vercel deployment.

## 🚀 Quick Deployment

### Prerequisites
- Vercel CLI: `npm i -g vercel`
- Backend deployed on Render (see Backend Deployment below)
- Google Gemini API Key: `AIzaSyCszFeBHnfLEDnBWCLDzZ7zmBXkxF2hyg8`

### Step 1: Deploy Backend to Render

1. **Create Render Account**: Go to https://render.com

2. **Create New Web Service**:
   - Click "New +" → "Web Service"
   - Choose "Build and deploy from a Git repository"
   - Connect your GitHub account and select your repository

3. **Configure Service**:
   ```
   Name: meme-blaster-backend (or your choice)
   Region: Select closest to your users
   Branch: main (or your deployment branch)
   Root Directory: (leave empty if deploying whole repo)
   Runtime: Python 3
   Build Command: pip install -r requirements.txt && reflex init
   Start Command: reflex run --env prod --backend-only --backend-port 8000
   ```

4. **Add Environment Variables**:
   - Click "Environment" tab
   - Add: `GOOGLE_API_KEY` = `AIzaSyCszFeBHnfLEDnBWCLDzZ7zmBXkxF2hyg8`

5. **Deploy**:
   - Click "Create Web Service"
   - Wait 3-5 minutes for deployment
   - Copy your backend URL (e.g., `https://meme-blaster-backend.onrender.com`)

6. **Test Backend**:
   - Visit your backend URL in browser
   - You should see the Reflex backend running

### Step 2: Update Vercel Configuration

**Edit `vercel.json`** in this directory and replace `YOUR-BACKEND-URL-HERE` with your actual Render URL:

```json
{
  "version": 2,
  "framework": "nextjs",
  "buildCommand": "echo 'Frontend already built via reflex export'",
  "routes": [
    {
      "src": "/api/(.*)",
      "dest": "https://your-backend.onrender.com/api/$1",
      "headers": {
        "Cache-Control": "no-cache"
      }
    },
    {
      "src": "/(.*)",
      "dest": "/$1"
    }
  ]
}
```

### Step 3: Deploy to Vercel

```bash
# Login to Vercel (first time only)
vercel login

# Deploy to production
vercel --prod
```

**Follow the prompts:**
- Set up and deploy? → **Y**
- Which scope? → Choose your account
- Link to existing project? → **N** (unless you have one)
- Project name? → **meme-blaster** (or your choice)
- In which directory is your code? → **./
- Want to override settings? → **N**

### Step 4: Verify Deployment

After deployment:
1. Visit your Vercel URL (shown after deployment)
2. Test image upload
3. Test AI meme generation
4. Test meme download

## 📝 Alternative: Manual Vercel Dashboard Deployment

If you prefer using the Vercel Dashboard:

1. **Prepare Git Repository**:
   ```bash
   git init
   git add .
   git commit -m "Vercel deployment ready"
   git remote add origin <your-github-repo-url>
   git push -u origin main
   ```

2. **Deploy via Dashboard**:
   - Go to https://vercel.com/dashboard
   - Click "Add New" → "Project"
   - Import your Git repository
   - Vercel will auto-detect the configuration
   - Click "Deploy"

## 🔧 Troubleshooting

### Frontend loads but AI doesn't work
- ✅ Check backend is running (visit backend URL)
- ✅ Verify `GOOGLE_API_KEY` is set in Render
- ✅ Check `vercel.json` has correct backend URL
- ✅ Check browser console for errors

### CORS Errors
If you see CORS errors in browser console:

1. Update backend code to allow your Vercel domain:
   - Add CORS middleware in your backend
   - Allow origin: `https://your-app.vercel.app`

2. For Reflex apps, CORS is typically handled automatically

### 404 Errors on API Calls
- Ensure backend URL in `vercel.json` is correct
- Backend must include `/api` in the route path
- Check Render logs for backend errors

### Backend Cold Starts (Render Free Tier)
- Free tier spins down after 15 minutes of inactivity
- First request may take 30-60 seconds to wake up
- Upgrade to paid plan ($7/month) for always-on backend

## 💰 Cost Breakdown

**Vercel:**
- Hobby Plan: **FREE** (perfect for personal projects)
- 100GB bandwidth/month
- Unlimited deployments

**Render (Backend):**
- Free Tier: **FREE** (with cold starts)
- Paid Plan: **$7/month** (always-on, recommended)

**Google Gemini API:**
- Free Tier: 15 requests/minute
- Check usage: https://console.cloud.google.com

**Total: $0-7/month** depending on your backend choice

## 🎨 Custom Domain

To add a custom domain:

1. Go to Vercel Dashboard → Your Project
2. Click "Settings" → "Domains"
3. Add your domain
4. Update DNS records as instructed
5. SSL certificate auto-provisioned

## 📊 Monitoring

**Vercel:**
- Dashboard shows deployments and analytics
- Real-time logs available

**Render:**
- Check logs: Dashboard → Your Service → Logs
- Monitor CPU/Memory usage

**Google Gemini:**
- Monitor API usage: https://console.cloud.google.com
- Set up billing alerts

## 🆘 Need Help?

- Vercel Docs: https://vercel.com/docs
- Render Docs: https://render.com/docs
- Reflex Docs: https://reflex.dev/docs
- Google Gemini: https://ai.google.dev

---

**Made with ❤️ using Reflex + Vercel**