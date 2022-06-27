# subbly-server

AWS E2(ubuntu), Nginx + Uwsgi를 이용하여 배포

# Uwsgi
#### path : etc/uwsgi/sites/subbly-server.ini
#### cmd : uwsgi --http :8000 --module subbly-server.wsgi

        [uwsgi]
        base = /home/ubuntu/subbly-server

        home = %(base)/venv
        chdir = %(base)
        module = config.wsgi:application

        socket = /tmp/django.sock
        chmod-socket = 666

        master = true
        enable-threads = true
        pidfile = /tmp/django.pid

        vacuum = true
        logger = file:/tmp/uwsgi.log


# Nginx
#### path : etc/nginx/nginx.conf
#### cmd : systemctl start nginx

        user www-data;
        worker_processes auto;
        pid /run/nginx.pid;
        include /etc/nginx/modules-enabled/*.conf;

        events {
                worker_connections 768;
                # multi_accept on;
        }

        http {

        ##
        # Basic Settings
        ##

        sendfile on;
        tcp_nopush on;
        types_hash_max_size 2048;
        # server_tokens off;

        # server_names_hash_bucket_size 64;
        # server_name_in_redirect off;

        include /etc/nginx/mime.types;
        default_type application/octet-stream;

        ##
        # SSL Settings
        ##

        ssl_protocols TLSv1 TLSv1.1 TLSv1.2 TLSv1.3; # Dropping SSLv3, ref: POODLE
        ssl_prefer_server_ciphers on;

        ##
        # Logging Settings
        ##

        access_log /var/log/nginx/access.log;
        error_log /var/log/nginx/error.log;

        ##
        # Gzip Settings
        ##

        gzip on;

        # gzip_vary on;
        # gzip_proxied any;
        # gzip_comp_level 6;
        # gzip_buffers 16 8k;
        # gzip_http_version 1.1;
        # gzip_types text/plain text/css application/json application/javascript text/xml application/xml application/xml+rss text/javascript;

        ##
        # Virtual Host Configs
        ##

        include /etc/nginx/conf.d/*.conf;
        include /etc/nginx/sites-enabled/*;
        }

        #mail {
        #       # See sample authentication script at:
        #       # http://wiki.nginx.org/ImapAuthenticateWithApachePhpScript
        #
        #       # auth_http localhost/auth.php;
        #       # pop3_capabilities "TOP" "USER";
        #       # imap_capabilities "IMAP4rev1" "UIDPLUS";
        #
        #       server {
        #               listen     localhost:110;
        #               protocol   pop3;
        #               proxy      on;
        #       }
        #
        #       server {
        #               listen     localhost:143;
        #               protocol   imap;
        #               proxy      on;
        #       }
        #}
#### path : etc/nginx/site-enabled/subbly-server
        upstream django {
                server unix:///tmp/django.sock;
        }

        server {
                listen      80;
                server_name localhost;
                charset     utf-8;

                client_max_body_size 75M;   # adjust to taste

                location / {
                        uwsgi_pass django;
                        include   /etc/nginx/uwsgi_params;
                }
        }
#### path : etc/nginx/site-enabled/default
        server {
        listen 8080 default_server;     #8000에서 8080으로 수정
        listen [::]:8080 default_server;           #8000에서 8080으로 
        
