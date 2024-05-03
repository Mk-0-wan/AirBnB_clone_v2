#!/usr/bin/env bash
# Set env variables to use development environemnt

echo "setting Database setup to Development Environment..."
echo -ne "[      ]:\r"
sleep 1
export HBNB_ENV="dev"
echo -ne "[#     ]: ENV set to $HBNB_ENV\t\t\r"
sleep 1
export HBNB_MYSQL_USER="hbnb_dev"
echo -ne "[##    ]: USER set to $HBNB_MYSQL_USER\t\t\r"
sleep 1
export HBNB_MYSQL_PWD="hbnb_dev_pwd"
echo -ne "[###   ]: PWD set to $HBNB_MYSQL_PWD\t\t\r"
sleep 1
export HBNB_MYSQL_HOST="localhost"
echo -ne "[####  ]: HOST set to $HBNB_MYSQL_HOST               \t\t\r"
sleep 1
export HBNB_MYSQL_DB="hbnb_dev_db"
echo -ne "[##### ]: DB set to $HBNB_MYSQL_DB             \r"
sleep 1
export HBNB_TYPE_STORAGE="db"
echo -ne "[######]: STORAGE TYPE set to $HBNB_TYPE_STORAGE\t\t\r"
sleep 1
echo -ne "\ndone\n"
