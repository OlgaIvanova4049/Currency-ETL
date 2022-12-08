FROM python:3.9.0

WORKDIR code

RUN apt-get -y update \
    && apt-get -y install git \
    && apt-get clean

RUN python -m pip install -U pip
RUN pip install poetry

COPY poetry.lock pyproject.toml ./
RUN poetry config virtualenvs.create false \
  && poetry install

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
