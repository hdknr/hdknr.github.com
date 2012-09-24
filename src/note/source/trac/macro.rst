::

    # Virtual Host 
    <Macro VHost $host $base $port>
        <VirtualHost *:$port>
        #Basic
                ServerAdmin admin@$host
                ServerName  $host
                DocumentRoot /home/emdocs/$host/www/
        
        # BasicAuth
           <Location "/" >
                Include $base/$host/conf/httpd.conf.d/auth_pwd_file.def
                </Location>
        
                Include $base/$host/conf/httpd.conf.d/wsgi.def
                Include $base/$host/conf/httpd.conf.d/trac.def
        #Log
                ErrorLog $base/$host/logs/error.log
                LogLevel warn
                CustomLog $base/$host/logs/access.log combined
        
        # SSL
                Include $base/$host/conf/ssl.def
        </VirtualHost>
    </Macro>
    
    #Virtual Directory
    <Macro Trac $host $base $prefix  $prj>

        <Location /prj/$prj > 
          AuthName "Secret Zone"
          AuthUserFile $base/$host/conf/.htpasswd.$prj
          Require valid-user
        </Location>
        
        <Location /prj/$prj/svn >
          DAV svn
          SVNPath $base/$host/prj/$prj/svn
          SVNAutoversioning On
        </Location>
        
        WSGIScriptAlias /prj/$prj/trac $base/$host/prj/wsgi.py
        
        <Location /prj/$prj/trac >
           WSGIProcessGroup ve_$prefix_trac_$prj
           WSGIApplicationGroup %{SERVER}
           Options All
        </Location>
    </Macro>

    #WSGI
    <Macro WSGI $ve $prefix $prj >
        WSGIDaemonProcess ve_$prefix_trac_$prj user=www-data group=www-data threads=25 python-path=$ve/lib/python2.7/site-packages:$ve/bin
    </Macro>

    #SSL
    <Macro SSL $host $base >
        SSLEngine on
        SSLCertificateFile $base/$host/cert/cert.pem
        SSLCertificateKeyFile $base/$host/cert/privatekey.pem
    </Macro>
