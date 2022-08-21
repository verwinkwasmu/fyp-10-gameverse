# fyp-10-gameverse

### Usage - Backend

As a first step, install the requirements:

```
pip install -r requirements.txt
```

This is how you run the code locally (without Docker):

```
uvicorn main:app --host 127.0.0.1 --port 8080 --reload
```

Build and run the Docker image locally, as follows:

```
docker build -t <name> .
docker run -d -p 8080:80 <name>
*(fyi -d is detached mode)*
```

In order to run the server with docker compose, use this:

```
docker-compose up --build
```

To run tests
```
python3 -m pytest -v tests/
```

### Usage - Frontend
As a first step, install the node modules (make sure you have node installed into your system):
```
npm install
```
This is how you run the code locally:
```
npm run dev
```

### Misc

- Volumes are implemented to enable auto-reload of images when developing in docker
