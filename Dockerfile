# Use a lightweight Python 3.8 image
FROM python:3.8-slim



# Set working directory
WORKDIR /app




# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project files
COPY . .

# Run migrations & start server
CMD bash -c "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"

