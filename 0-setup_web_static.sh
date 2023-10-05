#!/usr/bin/env bash
# Script sets up web servers for deployment of web_static.

# Install Nginx if not installed
if ! dpkg -l | grep -q nginx; then
    sudo apt-get update
    sudo apt-get -y install nginx
fi

# Create required directories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/current/

# Create fake HTML file
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html >/dev/null

# Create or recreate symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership to ubuntu user and group recursively
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
config_file="/etc/nginx/sites-available/default"
config_content="location /hbnb_static/ {
    alias /data/web_static/current/;
    index index.html;
}"

# Add or update configuration
if grep -q "location /hbnb_static/" "$config_file"; then
    sudo sed -i "/location \/hbnb_static\//c\\$config_content" "$config_file"
else
    echo "$config_content" | sudo tee -a "$config_file" >/dev/null
fi

# Restart Nginx
sudo service nginx restart

exit 0
