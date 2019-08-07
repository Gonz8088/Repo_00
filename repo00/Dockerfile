# Use an official runtime as a parent image
FROM # <name of image>

# Set the working directory to /name of working directory
WORKDIR /<name of working directory>

# Copy the current directory contents into the container at /app
COPY . /<name of working directory>

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port ## available to the world outside this container
EXPOSE <##>

# Define environment variable
ENV NAME <name>

# Run app.py when the container launches
CMD ["python", "<name of app>.py"]
