FROM python:3.8.2

WORKDIR /var/building_access/
COPY requirements.txt ./
RUN pip install -r requirements.txt && pip install channels==2.4.0
COPY . /var/building_access

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]