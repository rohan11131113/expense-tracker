FROM python:3.12

# Create app directory
WORKDIR /app

# Copy all files to container
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Run database initialization script
RUN python init_db.py

# Run the main app
CMD ["python", "app/app.py"]
