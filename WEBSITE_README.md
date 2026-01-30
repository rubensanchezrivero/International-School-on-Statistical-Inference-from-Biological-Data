# ICTP School Website

This project includes two web applications for the International School on Statistical Inference from Biological Data:

1. **Streamlit App** (ictpweb/) - Original Python-based application
2. **Astro Website** (website/) - Modern React/Astro landing page with shadcn/ui

## Deployment

Both applications run simultaneously via Docker Compose:

### Ports
- **Astro Website**: http://your-server-ip:3000
- **Streamlit App**: http://your-server-ip:8502

### Deploy to VPS

```bash
# Pull latest changes
git pull

# Build and start both services
docker-compose up -d --build

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

### Individual Service Management

```bash
# Restart only the Astro website
docker-compose restart ictp-school-website

# Restart only the Streamlit app
docker-compose restart ictp-school-streamlit

# View specific service logs
docker-compose logs -f ictp-school-website
```

## Local Development

### Astro Website

```bash
cd website
npm install
npm run dev
```

Runs on http://localhost:3000

### Streamlit App

```bash
cd ictpweb
pip install -r requirements.txt
streamlit run app.py
```

Runs on http://localhost:8501

## Technology Stack

### Astro Website
- **Framework**: Astro 4 with React
- **Styling**: TailwindCSS
- **UI Components**: shadcn/ui (Radix UI primitives)
- **Icons**: Lucide React
- **Deployment**: Docker with Node.js

### Streamlit App
- **Framework**: Streamlit
- **Data**: YAML files
- **Styling**: Custom CSS
- **Deployment**: Docker with Python

## Features

### Astro Website
- Modern, professional scientific conference design
- Fully responsive layout
- Interactive components (Accordion for lectures, Tabs for schedule)
- Clean, no-gradient design following best practices
- Fast page loads with Astro's optimization
- All content and images from original Streamlit app

### Content Sections
- Hero with event details
- Description and directors
- Lectures (interactive accordion)
- Program schedule (tabbed interface)
- Logistics information
- Contact details

## Architecture

Both services run in isolated Docker containers on the same network (`ictp-network`) for potential inter-service communication if needed in the future.

Health checks ensure services are running properly:
- Astro: HTTP check on port 3000
- Streamlit: Custom health endpoint on port 8501
