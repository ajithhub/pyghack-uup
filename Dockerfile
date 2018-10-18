FROM tiangolo/uwsgi-nginx-flask:python3.7


COPY uup_flask/requirements.txt /app
RUN pip install -r /app/requirements.txt
COPY uup_flask /app
COPY etc/ssl.conf /etc/nginx/conf.d/
RUN python /app/dataloader.py

COPY certs /etc/letsencrypt/live/getuupnow.com/
RUN cd /etc/letsencrypt/live/getuupnow.com/ && openssl rsa -in privkey.pem.encrypted -out privkey.pem -passin pass:"up up up and away"

