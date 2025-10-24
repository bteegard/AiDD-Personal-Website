# Docker Deployment Guide for Bryant Teegardin's Personal Website

This guide will help you containerize and deploy your Flask personal website using Docker.

## Prerequisites

- Docker Desktop installed and running on your Windows machine
- Basic familiarity with command line/PowerShell

## Quick Start

### Option 1: Using Docker Compose (Recommended)

1. **Open PowerShell in your project directory**
   ```powershell
   cd "C:\Users\cteeg\Downloads\AiDD Assignment 7"
   ```

2. **Build and run the application**
   ```powershell
   docker-compose up --build
   ```

3. **Access your website**
   - Open your browser and go to: `http://localhost:8000`
   - Your website will be running in a Docker container!

4. **Stop the application**
   ```powershell
   docker-compose down
   ```

### Option 2: Using Docker Commands Directly

1. **Build the Docker image**
   ```powershell
   docker build -t bryant-website .
   ```

2. **Run the container**
   ```powershell
   docker run -d -p 8000:8000 --name bryant-website-container bryant-website
   ```

3. **Access your website**
   - Open your browser and go to: `http://localhost:8000`

4. **Stop and remove the container**
   ```powershell
   docker stop bryant-website-container
   docker rm bryant-website-container
   ```

## What's Included

### Docker Files Created:
- **`Dockerfile`**: Defines how to build your Flask application container
- **`.dockerignore`**: Excludes unnecessary files from the Docker build
- **`docker-compose.yml`**: Orchestrates the application with easy commands
- **`init-db.sh`**: Database initialization script

### Key Features:
- ✅ **Python 3.11** base image for optimal performance
- ✅ **SQLite database** with automatic initialization
- ✅ **Security**: Non-root user for running the application
- ✅ **Health checks**: Monitors application status
- ✅ **Data persistence**: Database survives container restarts
- ✅ **Production ready**: Optimized for deployment

## Development vs Production

### Development Mode
```powershell
# Run with live reloading (if you modify files)
docker-compose up --build
```

### Production Mode
```powershell
# Run with Nginx reverse proxy
docker-compose --profile production up -d
```

## Database Management

The SQLite database (`projects.db`) is automatically created and initialized when the container starts. Your existing database will be preserved in the `./data` directory.

### View Database Contents
```powershell
# Access the running container
docker exec -it bryant-website-container bash

# Inside the container, view database
sqlite3 projects.db
.tables
SELECT * FROM projects;
.quit
```

## Troubleshooting

### Common Issues:

1. **Port already in use**
   ```powershell
   # Check what's using port 8000
   netstat -ano | findstr :8000
   
   # Use a different port in docker-compose.yml
   ports:
     - "8001:8000"  # Change 8000 to 8001
   ```

2. **Permission issues**
   ```powershell
   # Make sure Docker Desktop is running
   # Restart Docker Desktop if needed
   ```

3. **Build failures**
   ```powershell
   # Clean build (removes cache)
   docker-compose build --no-cache
   ```

### View Logs
```powershell
# View application logs
docker-compose logs -f web

# View logs for specific service
docker logs bryant-website-container
```

## Advanced Configuration

### Environment Variables
You can customize the application by setting environment variables in `docker-compose.yml`:

```yaml
environment:
  - FLASK_ENV=development  # Change to development for debug mode
  - FLASK_APP=app.py
  - SECRET_KEY=your-secret-key-here
```

### Volume Mounts
- **Database**: `./data:/app/data` - Persists your SQLite database
- **Static files**: `./static:/app/static` - Live reloading of CSS/images

### Resource Limits
Add resource limits to `docker-compose.yml`:
```yaml
services:
  web:
    # ... other config
    deploy:
      resources:
        limits:
          memory: 512M
        reservations:
          memory: 256M
```

## Deployment to Cloud Platforms

### Docker Hub
1. **Tag your image**
   ```powershell
   docker tag bryant-website yourusername/bryant-website:latest
   ```

2. **Push to Docker Hub**
   ```powershell
   docker push yourusername/bryant-website:latest
   ```

### AWS/Azure/GCP
- Use the `docker-compose.yml` file with cloud container services
- Consider using managed databases instead of SQLite for production
- Add environment variables for cloud-specific configurations

## Security Considerations

- ✅ Application runs as non-root user
- ✅ Minimal base image (Python slim)
- ✅ No unnecessary packages installed
- ✅ Health checks implemented
- ⚠️ **For production**: Consider using environment variables for secrets
- ⚠️ **For production**: Use HTTPS with proper SSL certificates

## Performance Tips

1. **Use multi-stage builds** for smaller images (already implemented)
2. **Enable Docker BuildKit** for faster builds:
   ```powershell
   $env:DOCKER_BUILDKIT=1
   docker-compose up --build
   ```

3. **Use .dockerignore** to exclude unnecessary files (already configured)

## Next Steps

1. **Test the deployment** - Make sure everything works as expected
2. **Customize the configuration** - Adjust ports, environment variables as needed
3. **Set up CI/CD** - Automate building and deployment
4. **Monitor the application** - Add logging and monitoring tools
5. **Scale if needed** - Use Docker Swarm or Kubernetes for multiple instances

---

**Your website is now fully containerized and ready for deployment! 🚀**

For questions or issues, check the Docker logs or refer to the troubleshooting section above.
