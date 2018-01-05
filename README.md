# redmine_open_issue_by_slack
Allows you to open an issue in redmine by slack API.


## Install

### Apache Python Module Setting
* The setup process is described for the debian distribution.
1. install apache2, libapache2-mod-python.
    * apt-get install apache2 libapache2-mod-python
2. Modify Apache configuration to use mod_python.
    * Set the path in "Directory" to match your web server environment.

#### Original    
```
<Directory /var/www/>
	Options Indexes FollowSymLinks
	AllowOverride None
	Require all granted
</Directory>
```

#### Change    
```
<Directory /var/www/>
	Options Indexes FollowSymLinks
	AllowOverride None
	Require all granted
	AddHandler mod_python .py
	PythonHandler mod_python.publisher | .py
</Directory>
```

3. Restarting Apache
    * systemctl restart apache2
4. Move the "api.py" file in the server folder to the "Directory" location set above.
