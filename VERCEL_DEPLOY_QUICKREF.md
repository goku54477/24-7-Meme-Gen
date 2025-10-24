# 🚀 Vercel Deployment Quick Reference

## One-Page Deployment Guide

### Prerequisites ✅
```bash
# Install Vercel CLI
npm i -g vercel

# Verify installations
vercel --version
python3 --version
```

### 3-Step Deployment 🎯

#### STEP 1: Deploy Backend (15 min)
```
1. Go to https://render.com
2. New + → Web Service → Connect Git repo
3. Configure:
   Name: meme-blaster-backend
   Build: pip install -r requirements.txt && reflex init
   Start: reflex run --env prod --backend-only --backend-port 8000
   Env: GOOGLE_API_KEY = AIzaSyCszFeBHnfLEDnBWCLDzZ7zmBXkxF2hyg8
4. Deploy → Copy URL
```

#### STEP 2: Update Config (1 min)
```bash
# Edit /app/vercel-deploy/vercel.json
# Replace: YOUR-BACKEND-URL-HERE
# With: https://your-backend.onrender.com
```

#### STEP 3: Deploy Frontend (5 min)
```bash
cd /app/vercel-deploy
vercel login
vercel --prod
```

### Testing Checklist ✅
- [ ] Homepage loads
- [ ] Upload image works
- [ ] AI generates 4 captions
- [ ] Can select/edit captions
- [ ] Download meme works
- [ ] Mobile responsive

### Troubleshooting 🔧

**AI not working?**
→ Check backend URL in vercel.json
→ Verify GOOGLE_API_KEY in Render
→ Check Render logs

**Slow first load?**
→ Free tier cold start (30-60s)
→ Upgrade to $7/month always-on

**CORS errors?**
→ Usually auto-handled by Reflex
→ Check browser console

### Cost 💰
- Vercel: FREE
- Render: FREE (or $7/month always-on)
- Gemini: FREE (15 req/min)

### Commands Cheat Sheet 📝

```bash
# Re-export frontend
cd /app && ./build-for-vercel.sh

# Deploy frontend
cd /app/vercel-deploy && vercel --prod

# Check vercel.json
cat /app/vercel-deploy/vercel.json | grep dest

# Test backend
curl https://your-backend.onrender.com
```

### Documentation 📚
- Complete Guide: `COMPLETE_DEPLOYMENT_GUIDE.md`
- Backend Guide: `RENDER_BACKEND_DEPLOY.md`
- Frontend Guide: `vercel-deploy/README.md`
- Status: `DEPLOYMENT_STATUS.md`

### Support 🆘
- Render Docs: https://render.com/docs
- Vercel Docs: https://vercel.com/docs
- Reflex Docs: https://reflex.dev/docs

---

**Total Time: ~20 minutes**
**Difficulty: Easy**
**Status: Ready to Deploy! 🎉**
