# Documentation for Django template


## Contents
[Setup](#setup)


## Setup

For local development:
1. create new vhosts config:

Check that paths to django virtualenv are set
```
<VirtualHost *:80>

    	LogLevel info

	Alias /static/ /Users/schien/sites/env/django/elena/static

#    	DocumentRoot "/Users/schien/sites/env/django/elena/"
    ServerName homeit
    ErrorLog "/Users/elena/sites/logs/homeit-error_log"
    CustomLog "/Users/elena/sites/logs/homeit-access_log" common
    <Directory "/Users/elena/sites/env/django/elena/static">
            Order deny,allow
            Allow from all
    </Directory>

# make sure python path contains entry to virutalenv site paackages as well as django project
	WSGIDaemonProcess homeit.server processes=2 threads=15 display-name=%{GROUP} python-path=/Users/elena/sites/env/django/lib/python2.7/site-packages:/Users/schien/sites/env/django/elena
	WSGIProcessGroup homeit.server

	# start script
	WSGIScriptAlias / /Users/elena/sites/env/django/elena/elena/wsgi.py

	<Directory "/Users/elena/sites/env/django/elena/elena/">
        <Files wsgi.py>
            Order allow,deny
            Allow from all
        </Files>
    </Directory>


</VirtualHost>
```

2. Include in `/etc/apache2/extra/httpd-vhosts.conf`
```
include /etc/apache2/extra/vhosts/elena.conf
```

3. Add alias to /etc/hosts
```
127.0.0.1       homeit
fe80::1%lo0     homeit
```


4. edit djagno secret key

5. edit DB params and path to log file in local_settings.py

6. edit gmail account / if needed