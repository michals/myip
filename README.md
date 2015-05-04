# myip
Simple script to store current ip of other machined

## Install myip service on your server with public ip.

    $ git clone https://github.com/michals/myip.git
    $ sudo make install
  
## Start service

    $ sudo myip start

## install on hosts

On machine with dyamic ip (to be tracked), add cronjob to request.
For example:

    # cat > /etc/cron.hourly/myip <<EOF
    wget -q -O /var/tmp/myip.txt -t1 http://myserver:8081/ip?host=hostid
    EOF
    # chmod 755 /etc/cron.hourly/myip

## find out IPs on server

Then you will have on server sqlite db with all hostid mapped to its recent ip:

    # sqlite3 /var/tmp/ip.db 'SELECT ip FROM hosts WHERE host="hostid"'
