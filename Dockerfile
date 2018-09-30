FROM tiangolo/uwsgi-nginx-flask:python3.7

COPY uup_flask /app
COPY etc/ssl.conf /etc/nginx/conf.d/

COPY certs /etc/letsencrypt/live/getuupnow.com/

