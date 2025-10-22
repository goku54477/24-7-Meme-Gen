# ⚡ Quick Commands Reference

Essential commands for MEME BLASTER development and deployment.

## Local Development

### Start the App
```bash
cd /app
./start.sh
# Or manually:
reflex run
```

### Start in Production Mode
```bash
reflex run --env prod
```

### View Logs
```bash
# If running in background
tail -f /tmp/reflex.log
```

## Building for Deployment

### Export Frontend for Vercel
```bash
cd /app
./build-for-vercel.sh
```

Or manually:
```bash
reflex export --frontend-only
mkdir vercel-deploy
cd vercel-deploy
unzip ../frontend.zip
```

## Deployment Commands

### Reflex Cloud (Easiest)
```bash
cd /app
reflex deploy
```

### Vercel Deployment
```bash
# After running build-for-vercel.sh
cd vercel-deploy
vercel login  # First time only
vercel --prod
```

### Backend Deployment (Render Example)
```bash
# Via Git
git push render main

# Or use Render dashboard
# Build: pip install -r requirements.txt
# Start: reflex run --env prod --backend-only
```

## Verification

### Check App Status
```bash
# Local
curl http://localhost:3000

# Backend API health
curl http://localhost:8000/ping
```

### View Dependencies
```bash
# Python
pip list | grep reflex

# Check version
reflex --version
```

## Environment Variables

### Set Locally (Linux/Mac)
```bash
export GOOGLE_API_KEY="your-key-here"
```

### Set Locally (Windows PowerShell)
```powershell
$env:GOOGLE_API_KEY="your-key-here"
```

### Verify Environment Variable
```bash
echo $GOOGLE_API_KEY
```

## Troubleshooting

### Clean Rebuild
```bash
cd /app
rm -rf .web
reflex init
reflex run
```

### Clear Cache
```bash
rm -rf __pycache__
rm -rf .web/
```

### Check Logs
```bash
# Backend logs (if using supervisor)
tail -f /var/log/supervisor/backend.err.log

# Reflex logs
tail -f /tmp/reflex.log
```

### Port Already in Use
```bash
# Kill Reflex processes
pkill -f reflex

# Or find and kill specific port
lsof -ti:3000 | xargs kill -9
lsof -ti:8000 | xargs kill -9
```

## File Management

### View Project Structure
```bash
cd /app
tree -L 2  # If tree is installed
# Or
find . -maxdepth 2 -type f
```

### Check File Sizes
```bash
ls -lh assets/
du -sh .web/
```

## Git Commands (If Using Version Control)

### Initial Setup
```bash
git init
git add .
git commit -m "Initial commit with logo and Vercel config"
```

### Push to Remote
```bash
git remote add origin <your-repo-url>
git push -u origin main
```

## Package Management

### Update Dependencies
```bash
pip install --upgrade reflex
```

### Install Specific Package
```bash
pip install package-name
pip freeze > requirements.txt  # Update requirements
```

## Testing

### Test Image Upload
```bash
curl -X POST http://localhost:3000/upload \
  -F "file=@test-image.jpg"
```

### Test Backend API
```bash
# Health check
curl http://localhost:8000/

# API endpoint
curl http://localhost:8000/api/health
```

## Maintenance

### Check Disk Space
```bash
df -h
```

### Clean Up Uploads
```bash
# Be careful with this command!
rm -rf /app/uploaded_files/*
```

### Backup
```bash
# Backup entire project
tar -czf meme-blaster-backup.tar.gz /app/

# Backup assets only
tar -czf assets-backup.tar.gz /app/assets/
```

## Performance

### Check Memory Usage
```bash
free -h
```

### Check Process Status
```bash
ps aux | grep reflex
```

### Monitor Resources
```bash
htop  # If installed
# Or
top
```

## Vercel-Specific

### List Deployments
```bash
vercel ls
```

### View Deployment Details
```bash
vercel inspect <deployment-url>
```

### Remove Deployment
```bash
vercel rm <deployment-name>
```

### Set Environment Variables
```bash
vercel env add GOOGLE_API_KEY production
```

### Pull Environment Variables
```bash
vercel env pull
```

## Quick Links

- **Reflex Docs**: https://reflex.dev/docs
- **Vercel Docs**: https://vercel.com/docs
- **Get Gemini API Key**: https://aistudio.google.com/apikey
- **Render**: https://render.com
- **Railway**: https://railway.app

## Emergency Commands

### Stop Everything
```bash
pkill -f reflex
pkill -f python
```

### Reset to Clean State
```bash
cd /app
rm -rf .web vercel-deploy frontend.zip
reflex init
```

### Check What's Running
```bash
netstat -tuln | grep LISTEN
# Or
ss -tuln | grep LISTEN
```

---

**💡 Tip**: Bookmark this file for quick reference during development!
