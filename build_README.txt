cd /work/pyghack-uup
git pull
docker build -t uup_app .
docker run -p80:80 -p443:443 uup_app
