# Use official lightweight Python image
FROM python:3.10-slim

# Set working directory to the Django project root
WORKDIR /app/sistema_pedidos

# Install netcat for the entrypoint script
RUN apt-get update && apt-get install -y netcat-openbsd

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the full project directory
COPY . /app/

# Copy the entrypoint script and make it executable
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Expose port 8000
EXPOSE 8000

# Use the entrypoint script as the container's entrypoint
ENTRYPOINT ["/app/entrypoint.sh"]
