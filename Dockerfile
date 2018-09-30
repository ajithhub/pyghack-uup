FROM tiangolo/uwsgi-nginx-flask:python3.7


COPY uup_flask/requirements.txt /app
RUN pip install -r /app/requirements.txt
COPY uup_flask /app
COPY etc/ssl.conf /etc/nginx/conf.d/
RUN python /app/dataloader.py

COPY certs /etc/letsencrypt/live/getuupnow.com/

