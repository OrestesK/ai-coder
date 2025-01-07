# Use an official Python runtime as the base image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy only the requirements file to leverage Docker's caching for dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install Prisma separately
# RUN pip install prisma

# Copy the Prisma schema and related files separately
# COPY prisma ./prisma

# Generate the Prisma client
# RUN prisma generate --schema=prisma/schema.prisma

# Copy the rest of the application code
COPY . .

# Expose the port FastAPI will run on
EXPOSE 8000

# Command to run FastAPI
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
