# COPWATCH


BACKEND SETUP:

## Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

## Setup Instructions

1. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   ```

2. **Activate the virtual environment:**
   
   On Linux/macOS:
   ```bash
   source venv/bin/activate
   ```
   
   On Windows:
   ```bash
   venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

   Or install packages individually:
   ```bash
   pip install fastapi uvicorn django torch torchvision ultralytics opencv-python ffmpeg-python
   pip install psycopg2-binary  # for PostgreSQL if using
   ```

4. **Verify installation:**
   ```bash
   pip list
   ```

## Deactivating the virtual environment
When you're done working on the project, you can deactivate the virtual environment:
```bash
deactivate
```