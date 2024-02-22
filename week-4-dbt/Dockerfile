# Use the official Python image from Docker Hub
FROM python:3.9

# Install dbt
RUN pip install dbt-postgres

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy the entire content of the local directory into the container
COPY . .

# Set the entrypoint command to run dbt
CMD ["dbt", "run"]
