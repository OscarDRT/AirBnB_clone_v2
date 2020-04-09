#!/bin/bash
#hola
sudo apt-get -y update
sudo apt-get -y 
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
echo "I am here!!!" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -Rh ubuntu:ubuntu /data/
sed -i "45i location /hbnb_static{\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default
service nginx restart
