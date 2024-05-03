#!/usr/bin/env bash
# Set env variables to use test environemnt

echo "setting Database setup to Test Environment..."
echo -ne "[      ]:\r"
sleep 1
export HBNB_ENV="test"
echo -ne "[#     ]: ENV set to $HBNB_ENV\t\t\r"
sleep 1
export HBNB_MYSQL_USER="hbnb_test"
echo -ne "[##    ]: USER set to $HBNB_MYSQL_USER\t\t\r"
sleep 1
export HBNB_MYSQL_PWD="hbnb_test_pwd"
echo -ne "[###   ]: PWD set to $HBNB_MYSQL_PWD\t\t\r"
sleep 1
export HBNB_MYSQL_HOST="localhost"
echo -ne "[####  ]: HOST set to $HBNB_MYSQL_HOST               \t\t\r"
sleep 1
export HBNB_MYSQL_DB="hbnb_test_db"
echo -ne "[##### ]: DB set to $HBNB_MYSQL_DB             \r"
sleep 1
export HBNB_TYPE_STORAGE="db"
echo -ne "[######]: STORAGE TYPE set to $HBNB_TYPE_STORAGE\t\t\r"
sleep 1
echo -ne "\ndone\n"
