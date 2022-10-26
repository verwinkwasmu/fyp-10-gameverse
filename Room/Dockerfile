FROM python:latest

# set the working directory
WORKDIR /code

# install dependencies
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# copy the scripts to the folder
COPY . /code/

# start the server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "83"]