# fyp-10-gameverse

## Usage - Backend

As a first step, install the requirements:
```
pip install -r requirements.txt
```
This is how you run the code locally (without Docker):
```
uvicorn main:app --host 0.0.0.0 --port 80 --reload
```
Build and run the Docker image locally, as follows:
```
docker build -t <name> .
docker run -d -p 8080:80 <name>
```
In order to run the server with docker compose, use this:
```
docker-compose up --build
```
To run tests
```
python3 -m pytest -v tests/
```

## Usage - Frontend
#### Created with Vite + Vue 3 with libraries (vue-router, vue query, tailwind css, flowbite, axios)
As a first step, install the node modules (make sure you have node installed into your system):
```
npm install
```
This is how you run the code locally:
```
npm run dev
```
To build:
```
npm run build
```
## Misc

- Volumes are implemented to enable auto-reload of images when developing in docker

Make sure to run prettier formatter to ensure consistency
```
npm run format
```
