# Base image
FROM python:3.9-slim

# Set environment variables to avoid warnings in Docker builds
ENV DEBIAN_FRONTEND=noninteractive

# Install necessary dependencies for Chrome and ChromeDriver
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    curl \
    gnupg \
    --no-install-recommends

# Install Chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && apt-get install -y google-chrome-stable

# Install ChromeDriver
RUN CHROME_VERSION=$(google-chrome --version | grep -oP '\d{2,3}' | head -1) && \
    wget https://chromedriver.storage.googleapis.com/${CHROME_VERSION}.0.0/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip && \
    mv chromedriver /usr/local/bin/ && \
    chmod +x /usr/local/bin/chromedriver

# Set display port for Chrome
ENV DISPLAY=:99

# Copy the requirements file
COPY requirements.txt /app/requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the application files
COPY . /app

# Set the working directory
WORKDIR /app

# Run the bot
CMD ["python", "bot.py"]
