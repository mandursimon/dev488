FROM python:3.8.2

# Copy only requirements, so cache relies only on them.
COPY requirements.txt /app/
RUN cd /app && pip install -r requirements.txt

# Set workdir
WORKDIR /app

# Copy app
COPY . /app/

EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000