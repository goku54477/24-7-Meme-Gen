# Deployment Guide for MEME BLASTER

This guide covers deploying the MEME BLASTER application to Vercel.

## Important Notes

MEME BLASTER is built with Reflex, a Python full-stack framework. The application has two components:
- **Frontend**: Next.js-based static site
- **Backend**: Python/FastAPI backend with AI meme generation (Google Gemini)

## Deployment Options

### Option 1: Reflex Cloud (Recommended - Full Stack)
The easiest way to deploy the complete application is using Reflex's built-in hosting:

```bash
reflex deploy
```

This handles both frontend and backend deployment automatically with:
- Automatic SSL certificates
- Global CDN
- Serverless backend
- One-click deployment

**Pros:**
- Simplest deployment method
- Handles both frontend and backend
- No separate configuration needed
- Built-in scaling and monitoring

**Cons:**
- Less control over infrastructure
- May have usage limits on free tier

### Option 2: Vercel Frontend + Separate Backend (Advanced)

If you want to deploy the frontend to Vercel and backend separately, follow these steps:

#### Step 1: Export Frontend
```bash
# Export only the frontend as static files
reflex export --frontend-only
```

This creates a `frontend.zip` file containing the static Next.js build.

#### Step 2: Prepare Vercel Deployment

**Extract and organize files:**
```bash
# Create a deployment directory
mkdir vercel-deploy
cd vercel-deploy

# Extract frontend
unzip ../frontend.zip

# The structure should now have:
# - .next/ (Next.js build)
# - public/ (static assets)
# - package.json
# - Other Next.js files
```

**Create or update `package.json`:**
If not present, create a minimal `package.json`:
```json
{
  "name": "meme-blaster-frontend",
  "version": "1.0.0",
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start"
  },
  "dependencies": {
    "next": "^14.0.0",
    "react": "^18.2.0",
    "react-dom": "^18.2.0"
  }
}
```

#### Step 3: Configure Vercel

**Create `vercel.json` in your deployment directory:**
```json
{
  "version": 2,
  "buildCommand": "echo 'Build already complete'",
  "framework": "nextjs",
  "routes": [
    {
      "src": "/api/(.*)",
      "dest": "https://your-backend-url.com/api/$1"
    },
    {
      "src": "/(.*)",
      "dest": "/$1"
    }
  ]
}
```

**Important:** Replace `https://your-backend-url.com` with your actual backend URL.

#### Step 4: Deploy to Vercel

**Method A: Using Vercel CLI (Recommended)**
```bash
# Install Vercel CLI if not already installed
npm i -g vercel

# Login to Vercel
vercel login

# Deploy (from the vercel-deploy directory)
vercel --prod
```

**Method B: Git Integration**
1. Initialize git in the `vercel-deploy` directory:
   ```bash
   git init
   git add .
   git commit -m "Initial Vercel deployment"
   ```
2. Push to GitHub/GitLab/Bitbucket:
   ```bash
   git remote add origin <your-repo-url>
   git push -u origin main
   ```
3. Go to [Vercel Dashboard](https://vercel.com/dashboard)
4. Click "Import Project"
5. Select your repository
6. Vercel will auto-detect Next.js and configure the build

**Configure Environment Variables in Vercel:**
1. Go to Project Settings > Environment Variables
2. Add `NEXT_PUBLIC_API_URL` with your backend URL
3. Redeploy if necessary

#### Step 5: Deploy Backend Separately

The backend requires a Python-compatible hosting platform. Here are the recommended options:

**Option A: Render**
1. Create a new Web Service on [Render](https://render.com)
2. Connect your Git repository
3. Set build command: `pip install -r requirements.txt`
4. Set start command: `reflex run --env prod` or `gunicorn`
5. Add environment variable: `GOOGLE_API_KEY`

**Option B: Railway**
1. Create a new project on [Railway](https://railway.app)
2. Connect your Git repository
3. Railway will auto-detect Python
4. Add environment variable: `GOOGLE_API_KEY`
5. Deploy

**Option C: Fly.io**
Create a `fly.toml`:
```toml
app = "meme-blaster-backend"

[build]
  [build.env]
    PYTHON_VERSION = "3.11"

[env]
  PORT = "8000"

[[services]]
  http_checks = []
  internal_port = 8000
  processes = ["app"]
  protocol = "tcp"
  
  [[services.ports]]
    port = 80
    handlers = ["http"]
  
  [[services.ports]]
    port = 443
    handlers = ["tls", "http"]
```

Deploy with:
```bash
fly launch
fly secrets set GOOGLE_API_KEY=your-key-here
fly deploy
```

#### Step 6: Update Frontend Configuration

After deploying the backend, update your Vercel project:

1. In Vercel Dashboard, go to your project
2. Settings > Environment Variables
3. Update or add: `NEXT_PUBLIC_API_URL=https://your-backend-url.com`
4. Redeploy your frontend

**Update `vercel.json` routes:**
```json
{
  "routes": [
    {
      "src": "/api/(.*)",
      "dest": "https://your-actual-backend-url.com/api/$1"
    }
  ]
}
```

Commit and push to trigger redeployment.

#### Step 7: Configure CORS on Backend

Ensure your backend accepts requests from your Vercel domain. In your backend code, configure CORS:

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://your-vercel-domain.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## Quick Vercel Deployment Checklist

For the simplest Vercel deployment:

1. ✅ Export frontend: `reflex export --frontend-only`
2. ✅ Extract files: `unzip frontend.zip -d vercel-deploy`
3. ✅ Deploy backend to Render/Railway/Fly.io
4. ✅ Get backend URL (e.g., `https://meme-blaster.onrender.com`)
5. ✅ Update `vercel.json` with backend URL
6. ✅ Deploy to Vercel: `vercel --prod`
7. ✅ Add environment variable `GOOGLE_API_KEY` to backend
8. ✅ Test the application

## Environment Variables Required

### Backend
- `GOOGLE_API_KEY`: Your Google Gemini API key ([Get one here](https://aistudio.google.com/apikey))

### Frontend (if split deployment)
- `NEXT_PUBLIC_API_URL`: Backend API URL (if deploying separately)
  - Example: `https://meme-blaster-backend.onrender.com`

## Features

- AI-powered meme caption generation using Google Gemini
- Image upload and processing
- Custom text overlay with Impact font styling
- Mobile-optimized UI with comic book aesthetics
- Download generated memes

## Tech Stack

- **Framework**: Reflex (Python full-stack)
- **Frontend**: Next.js, React, Tailwind CSS
- **Backend**: FastAPI, Python
- **AI**: Google Gemini 1.5 Flash
- **Image Processing**: Pillow (PIL)

## Important Considerations

1. **Static vs Dynamic**: The frontend can be deployed as static files, but dynamic features (AI meme generation) require a backend server.

2. **CORS Configuration**: If deploying frontend and backend separately, ensure CORS is properly configured on the backend to accept requests from your Vercel domain.

3. **API Costs**: Google Gemini API usage may incur costs depending on your usage volume.

4. **File Storage**: Uploaded images are temporarily stored on the backend server. Consider using cloud storage (S3, etc.) for production.

## Troubleshooting

### Frontend Shows But Features Don't Work
- Ensure backend is deployed and running
- Check that frontend's API URL points to the correct backend
- Verify CORS settings

### AI Generation Fails
- Confirm `GOOGLE_API_KEY` is set in backend environment
- Check Google Cloud API quota and billing
- Review backend logs for errors

### Upload Issues
- Ensure backend has write permissions for file uploads
- Check file size limits on your hosting platform

## Support

For Reflex-specific deployment questions, visit:
- [Reflex Documentation](https://reflex.dev/docs/)
- [Reflex Discord](https://discord.gg/reflex-dev)
