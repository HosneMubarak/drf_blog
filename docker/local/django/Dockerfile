# Define a build-time argument for the Python version and use a specific base image.
# ARG allows you to parameterize the Dockerfile.
ARG PYTHON_VERSION=3.11.2-bullseye
FROM python:${PYTHON_VERSION} as python

# This creates the first stage named 'python' with the specified Python version.

# Create a new build stage named 'python-build-stage'.
FROM python as python-build-stage

# This creates a new build stage that extends the 'python' stage created earlier.

# Define a build-time argument for the build environment (default is 'local').
# This argument can be set during the build process.
ARG BUILD_ENVIRONMENT=local

# Update the package list and install build essentials and PostgreSQL development libraries.
RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential \
    libpq-dev

# This stage updates the package list, installs build tools, and PostgreSQL development libraries.

# Copy the requirements file to the build stage.
COPY ./requirements .

# This copies the requirements file (used to install Python dependencies) from the host to the build stage.

# Create Python wheels (binary packages) for the dependencies.
RUN pip wheel --wheel-dir /usr/src/app/wheels -r ${BUILD_ENVIRONMENT}.txt

# This command uses 'pip' to create binary wheels for Python dependencies mentioned in the requirements file.

# Create a new build stage named 'python-run-stage'.
FROM python as python-run-stage

# This creates another build stage, which is separate from the 'python-build-stage'.

# Define a build-time argument for the build environment (default is 'local').
ARG BUILD_ENVIRONMENT=local

# Define environment variables to configure Python behavior.
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the BUILD_ENV environment variable to the provided build environment.
ENV BUILD_ENV=${BUILD_ENVIRONMENT}

# These commands set various environment variables used to configure Python and the application.

# Set the working directory inside the container to '/app'.
ARG APP_HOME=/app
WORKDIR ${APP_HOME}

# This sets the working directory inside the container to '/app'.

# Update the package list and install required dependencies.
RUN apt-get update && apt-get install --no-install-recommends -y \
    libpq-dev \
    gettext

# This stage updates the package list, installs more dependencies needed by the application, and later cleans up.

# Clean up unnecessary packages to reduce image size.
RUN apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

# This removes unnecessary packages to reduce the final image size.

# Copy Python wheel files from the 'python-build-stage' to '/wheels' in the current stage.
COPY --from=python-build-stage /usr/src/app/wheels /wheels/

# This copies the Python wheels created in the 'python-build-stage' to the '/wheels' directory.

# Install the dependencies from the wheels, and then remove the wheels to save space.
RUN pip install --no-cache-dir --no-index --find-links=/wheels/ /wheels/* \
    && rm -rf /wheels/

# This command installs Python dependencies from the wheels and then removes the wheels to save space.

# Copy the entrypoint and start scripts to the container, make them executable.
COPY ./docker/local/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

# This copies entrypoint and start scripts from the host to the container, making them executable.

COPY ./docker/local/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

COPY ./docker/local/django/celery/worker/start /start-celeryworker
RUN sed -i 's/\r$//g' /start-celeryworker
RUN chmod +x /start-celeryworker

COPY ./docker/local/django/celery/flower/start /start-flower
RUN sed -i 's/\r$//g' /start-flower
RUN chmod +x /start-flower

# Copy the application code to the working directory '/app'.
COPY . ${APP_HOME}

# This copies the application code from the host to the container's working directory.

# Define the entry point for the container when it starts.
ENTRYPOINT ["/entrypoint"]

# This specifies the entry point for the container, which is the 'entrypoint' script.
