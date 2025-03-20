# Use official lightweight Python image
FROM python:3.10-slim

# Set working directory to the Django project root
WORKDIR /app/sistema_pedidos

# Install system dependencies
RUN apt-get update && apt-get install -y netcat-openbsd

# Copy only requirements.txt first to leverage Docker cache
COPY requirements.txt /app/

# Upgrade pip
RUN pip install --upgrade pip

# Install dependencies separately before copying the full project
RUN pip install --no-cache-dir -r /app/requirements.txt

# Now copy the entire application
COPY . /app/

# Copy the entrypoint script and make it executable
RUN chmod +x /app/entrypoint.sh

# Expose port 8000
EXPOSE 8000

# Use the entrypoint script as the container's entrypoint
ENTRYPOINT ["/app/entrypoint.sh"]
