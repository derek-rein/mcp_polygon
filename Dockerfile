FROM python:3.13-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    curl \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Install PDM for dependency management
RUN curl -sSL https://pdm-project.org/install-pdm.py | python3 - && \
    ln -s /root/.local/bin/pdm /usr/local/bin/pdm

# Copy all files needed for the build (including README.md)
COPY . .

# Install dependencies
RUN pdm install

# Make entrypoint executable
RUN chmod +x entrypoint.py

# Set environment variables
ENV PYTHONPATH=/app/src:$PYTHONPATH
ENV PYTHONUNBUFFERED=1

# Expose port (Railway will automatically assign a port)
EXPOSE 8000

# Use pdm to run the application
ENTRYPOINT ["uv", "run", "./entrypoint.py"]
