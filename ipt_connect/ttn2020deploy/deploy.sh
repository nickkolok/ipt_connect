#!/bin/bash

DATE=`date +%Y-%m-%d---%H-%M-%S`

scp voronezh.iptnet.info:/root/html/ipt/ipt_connect/ipt_connect/db.sqlite3 ./db-$DATE.sqlite3

INSTANCES="YUG SKFO INT EAST URAL NW CFO POV"

for instance in $INSTANCES ; do
	echo $instance
	scp -pr ../IPTdev/* voronezh.iptnet.info:/root/html/ipt/ipt_connect/ipt_connect/TTH2020$instance/
	scp -pr ../IPTdev/templates/IPTdev/* voronezh.iptnet.info:/root/html/ipt/ipt_connect/ipt_connect/TTH2020$instance/templates/TTH2020$instance/
	scp -pr ../IPTdev/static/IPTdev/* voronezh.iptnet.info:/html/ipt/ipt_connect/ipt_connect/static/TTH2020$instance/
done;

ssh voronezh.iptnet.info 'cd /root/html/ipt/ipt_connect/ipt_connect; python manage.py makemigrations; python manage.py migrate; reboot'
