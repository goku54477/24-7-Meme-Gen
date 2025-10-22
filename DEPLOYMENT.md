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

### Option 2: Split Deployment (Vercel + Backend Host)

If you want to deploy the frontend to Vercel and backend separately:

#### Step 1: Export Frontend
```bash
# Export only the frontend as static files
reflex export --frontend-only
```

This creates a `frontend.zip` file containing the static Next.js build.

#### Step 2: Prepare for Vercel
```bash
# Extract the frontend files
unzip frontend.zip -d vercel-frontend
cd vercel-frontend
```

#### Step 3: Deploy to Vercel

**Using Vercel CLI:**
```bash
# Install Vercel CLI if not already installed
npm i -g vercel

# Deploy
vercel
```

**Using Git Integration:**
1. Push the extracted frontend files to a Git repository
2. Connect the repository in the Vercel dashboard
3. Vercel will auto-detect and deploy

#### Step 4: Deploy Backend Separately
The backend requires:
- Python 3.10+
- Google API key for Gemini AI
- Environment variable: `GOOGLE_API_KEY`

Recommended backend hosting platforms:
- Render
- Railway
- Fly.io
- Any Python-compatible cloud provider

#### Step 5: Connect Frontend to Backend
After deploying backend, update the frontend's API URL configuration to point to your backend URL.

## Environment Variables Required

### Backend
- `GOOGLE_API_KEY`: Your Google Gemini API key

### Frontend (if split deployment)
- `NEXT_PUBLIC_API_URL`: Backend API URL (if deploying separately)

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
