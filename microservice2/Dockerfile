FROM python:3.9-slim

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

COPY ./app /code/app

# COPY ./alembic /app/alembic
# COPY ./alembic.ini /app/alembic.ini

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7999"]