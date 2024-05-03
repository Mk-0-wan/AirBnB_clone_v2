#!/usr/bin/evn bash
# bash scrip that helps one setup a simple testing webpage
# global var
nginx_conf="/etc/nginx/sites-available/default"
config_line="\\\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}"

# setting up the folders for handling fake html file
# ensure that the nginx is installed
sudo apt-get -y install nginx

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# making the fake html content
echo "ALX, still don't now what the X stands for" | sudo tee /data/web_static/releases/test/index.html

# symbolic link between the ../test/ with the ../current
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# ubuntu user should own this directory. R is for recursive
sudo chown -R ubuntu:ubuntu /data

# add the following lines of text to the config file
sudo sed -i "16i $config_line" $nginx_conf

# restart the whole nginx service to allow the new intstructions
sudo systemctl restart nginx
