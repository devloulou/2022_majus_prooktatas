# python
# flask

FROM python:3.8-alpine
RUN mkdir /app
COPY app.py /app/
WORKDIR /app

RUN pip install Flask

EXPOSE 8000
CMD ["python", "app.py"]