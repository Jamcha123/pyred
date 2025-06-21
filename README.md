# pyred
pyred is a python redis cli tool 
pyred allows you to add redis data to any redis server using python

installation: 

    1. pip install argparse --break-system-packages

    2. pip install redis --break-system-packages

    3. sudo apt-get install redis

init: 

    1. run a redis-server in another terminal or use redis in the cloud e.g redis.io //use redis-server

    2. python3 index.py --help // to get the help menu

    3. python3 index.py -t 127.0.0.1 -p 6379 -u default -c default -n key -d hello-world

you of course need to run a redis server using ```redis-server```