# Fibonacci Docker on Python

This repository contains a Python script that generates the Fibonacci series and runs it within a Docker container.

### Prerequisites

- [Python3](https://www.python.org/)
- [Docker](https://docs.docker.com/engine/install/)

## Installing

1. Clone the repository:

```
git clone git@github.com:Fuan200/fibonacci_docker_python.git
```

2. Run the script:

```
python fibo_docker.py
```

3. Enter the value to `input_user`.

Note: The value `input_user` only can be a integer.

## Getting Started (Docker)

1. Build the image to the proyect:

```
docker build -t <name_of_image> .
```

If you receive an error similar to the following when starting the last command:

```permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock:```

Run the following command first:

```
sudo docker build -t <name_of_image> .
```

2. Run the container:

```
docker run -it --name <container_name> fibo_docker
```

3. Write a number (this only will works one time)

4. Start the container:

```
docker start <container_name>
```

5. Exec the container:

```
docker exec -it <container_name> /bin/bash
```

You will be on the terminal container.

6. Run the script:

```
python fibo_dock.py
```

7. To exit to terminal container:

```
exit
```
<!-- ### Sample Test -->
## Author

- **Fuan200** - [Fuan200](https://github.com/Fuan200)

