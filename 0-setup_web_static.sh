#!/usr/bin/env bash
#Script that sets up your web servers for the deployment of web_static
sudo apt-get update
sudo apt-get -y install nginx
mkdir /data/ 
mkdir /data/web_static/
mkdir /data/web_static/releases/
mkdir /data/web_static/shared/
mkdir /data/web_static/releases/test/
echo -e "<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i '42i location /hbnb_static {\nalias /data/web_static/current/;\n}\n' /etc/nginx/sites-available/default
service nginx restart
