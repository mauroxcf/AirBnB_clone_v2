#!/usr/bin/env bash
#sets up your web servers for the deployment of web_static
sudo apt -y update
sudo apt install -y nginx
mkdir -p data/web_static/releases
mkdir -p data/web_static/shared
mkdir -p data/web_static/releases/test
touch data/web_static/releases/test/index.html
sudo echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data
sed -i '/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/;}' /etc/nginx/sites-available/default
service nginx restart
