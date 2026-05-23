# Blog with Flask

This is a learning project for Flask + Docker. It demonstrates how to containerize a Flask application using Docker.

## Project Description

`This is for learning Flask + Dockerfile`.

## Prerequisites

Make sure you have the following installed on your machine:

- [Docker](https://www.docker.com/products/docker-desktop) (or Docker Engine on Linux)
- [Docker Compose](https://docs.docker.com/compose/install/) (optional, but recommended)

## Building the Docker Image

To build the Docker image from the Dockerfile, run the following command in the project root directory:

```bash
docker build -t blog-with-flask .
```

This command will:
- Read the `Dockerfile` in the current directory
- Build an image with the tag name `blog-with-flask`
- Install all necessary dependencies as defined in the Dockerfile

## Running the Container

Once the image is built successfully, you can run the container using:

```bash
docker run -p 5000:5000 blog-with-flask
```

This command will:
- Create and start a new container from the `blog-with-flask` image
- Map port 5000 on your host machine to port 5000 in the container
- Allow you to access the Flask application at `http://localhost:5000`

### Running the Container in Detached Mode

If you want to run the container in the background:

```bash
docker run -d -p 5000:5000 --name blog-container blog-with-flask
```

This will:
- Run the container in detached mode (in the background)
- Name the container `blog-container` for easy reference
- Display the container ID

### Stopping the Container

To stop a running container:

```bash
docker stop blog-container
```

Or if you're running it in the foreground, press `Ctrl+C`.

### Removing the Container

To remove a stopped container:

```bash
docker rm blog-container
```

## Viewing Container Logs

To view the logs from your running container:

```bash
docker logs blog-container
```

For live logs, use:

```bash
docker logs -f blog-container
```

## Quick Start (Build and Run)

Here's a quick start guide to build and run everything in sequence:

```bash
# 1. Build the Docker image
docker build -t blog-with-flask .

# 2. Run the container
docker run -d -p 5000:5000 --name blog-container blog-with-flask

# 3. Access the application
# Open your browser and go to: http://localhost:5000

# 4. View logs
docker logs -f blog-container

# 5. Stop the container when done
docker stop blog-container
```

## Useful Docker Commands

| Command | Description |
|---------|-------------|
| `docker images` | List all available images |
| `docker ps` | List running containers |
| `docker ps -a` | List all containers (including stopped ones) |
| `docker rmi blog-with-flask` | Remove the image |
| `docker exec -it blog-container bash` | Access container shell |
| `docker inspect blog-container` | View detailed container information |

## Technologies Used

- **Flask**: Python web framework
- **Docker**: Containerization platform
- **Python**: Backend programming language
- **HTML**: Frontend markup

## Learning Resources

- [Flask Official Documentation](https://flask.palletsprojects.com/)
- [Docker Official Documentation](https://docs.docker.com/)
- [Docker Best Practices](https://docs.docker.com/develop/dev-best-practices/)

## Notes

- Make sure port 5000 is available on your host machine, or modify the port mapping in the `docker run` command
- The Dockerfile should define the base image, dependencies, and how to run the Flask application
- For production deployments, consider using Docker Compose or Kubernetes

## License

This is a learning project.
