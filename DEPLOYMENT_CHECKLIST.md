# 📋 Deployment Checklist

Use this checklist to ensure a smooth deployment of MEME BLASTER.

## Pre-Deployment

### Required Items
- [ ] Google Gemini API key obtained from https://aistudio.google.com/apikey
- [ ] Vercel account created at https://vercel.com
- [ ] Backend hosting account (Render/Railway/Fly.io)
- [ ] Vercel CLI installed: `npm i -g vercel`

### Code Preparation
- [x] Logo added to `/app/assets/logo.jpg`
- [x] Logo integrated into header component
- [ ] Tested app locally with `reflex run`
- [ ] Verified AI meme generation works with your API key
- [ ] Committed all changes to git (if using git deployment)

## Deployment Steps

### Option 1: Reflex Cloud (Simplest)
- [ ] Run `reflex deploy` from `/app` directory
- [ ] Set `GOOGLE_API_KEY` environment variable during deployment
- [ ] Wait for deployment to complete
- [ ] Test the deployed URL
- [ ] Verify all features work (upload, AI generation, download)

### Option 2: Vercel + Separate Backend

#### Backend Deployment
- [ ] Choose backend platform (Render/Railway/Fly.io)
- [ ] Create new project/service
- [ ] Configure build command: `pip install -r requirements.txt`
- [ ] Configure start command: `reflex run --env prod --backend-only`
- [ ] Set environment variable: `GOOGLE_API_KEY`
- [ ] Deploy and wait for completion
- [ ] Copy backend URL (e.g., `https://meme-blaster.onrender.com`)
- [ ] Test backend is accessible (visit URL in browser)

#### Frontend Deployment
- [ ] Run export script: `./build-for-vercel.sh`
- [ ] Navigate to `vercel-deploy` directory
- [ ] Update `vercel.json` with actual backend URL
- [ ] Run `vercel login` (first time only)
- [ ] Run `vercel --prod`
- [ ] Copy Vercel deployment URL
- [ ] Wait for deployment to complete

#### Post-Deployment Configuration
- [ ] Update backend CORS to allow Vercel domain
- [ ] Test frontend at Vercel URL
- [ ] Upload test image
- [ ] Verify AI generation works
- [ ] Verify download works
- [ ] Test on mobile device
- [ ] Check browser console for errors

## Verification Tests

### Functionality Tests
- [ ] Homepage loads correctly
- [ ] Logo displays in header
- [ ] Upload button (BOOM) is visible and works
- [ ] Image uploads successfully
- [ ] AI suggestions appear (4 captions)
- [ ] Selecting suggestion applies text
- [ ] Manual text edit works
- [ ] Download button works
- [ ] Downloaded meme has correct text overlay
- [ ] "NEW MEME" button clears and resets

### Performance Tests
- [ ] Page loads in under 3 seconds
- [ ] AI generation completes within 5 seconds
- [ ] No console errors
- [ ] Images load properly
- [ ] Smooth navigation

### Mobile Tests
- [ ] Responsive layout on mobile
- [ ] Touch interactions work
- [ ] Upload from camera works (if on device)
- [ ] Buttons are easily tappable
- [ ] Text is readable
- [ ] Download works on mobile

## Post-Deployment

### DNS & Domain (Optional)
- [ ] Add custom domain in Vercel settings
- [ ] Update DNS records
- [ ] Verify SSL certificate is active
- [ ] Test custom domain

### Monitoring
- [ ] Set up Vercel analytics (optional)
- [ ] Monitor backend logs
- [ ] Check API usage in Google Cloud Console
- [ ] Set up alerts for errors (optional)

### Documentation
- [ ] Update README with deployed URL
- [ ] Document any custom configuration
- [ ] Share deployment URL with stakeholders

## Troubleshooting

If deployment fails, check:

### Frontend Issues
- [ ] Check Vercel build logs
- [ ] Verify Next.js version compatibility
- [ ] Ensure all static assets are present
- [ ] Check browser console for errors

### Backend Issues
- [ ] Check backend logs
- [ ] Verify `GOOGLE_API_KEY` is set
- [ ] Test backend URL directly
- [ ] Check Python dependencies are installed

### Integration Issues
- [ ] Verify backend URL in `vercel.json` is correct
- [ ] Check CORS configuration
- [ ] Test API endpoints with curl/Postman
- [ ] Verify network tab in browser dev tools

## Rollback Plan

If deployment fails or has critical issues:

### Vercel
- [ ] Go to Vercel dashboard
- [ ] Select your project
- [ ] Go to Deployments
- [ ] Find previous working deployment
- [ ] Click "..." menu → "Promote to Production"

### Backend
- [ ] Use platform's rollback feature
- [ ] Or redeploy previous version from git

## Success Criteria

Deployment is successful when:
- ✅ Application loads without errors
- ✅ Logo displays correctly in header
- ✅ Users can upload images
- ✅ AI generates meme suggestions
- ✅ Users can customize and download memes
- ✅ Application works on desktop and mobile
- ✅ No console errors or warnings
- ✅ Response times are acceptable

## Notes

### API Costs
- Google Gemini: Free tier = 15 requests/minute
- Monitor usage at https://console.cloud.google.com

### Scaling Considerations
- Vercel: Free tier handles decent traffic
- Backend: Free tier has limitations (cold starts)
- Consider paid tiers for production traffic

### Security
- [ ] Environment variables are set securely
- [ ] No API keys in frontend code
- [ ] CORS is properly configured
- [ ] HTTPS is enabled (automatic with Vercel)

---

**Date Deployed**: ______________
**Deployed By**: ______________
**Frontend URL**: ______________
**Backend URL**: ______________
