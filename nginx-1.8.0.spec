Name:           nginx
Version:        1.8.0
Release:        1
Summary:        nginx rpm

Group:          Library
License:        GPL
            
Source0:       %{name}-%{version}.tar.gz 


%description


%prep
%setup -q


%build
./configure --prefix=/tools/nginx  --with-pcre=/tmp/pcre-8.37 --with-zlib=/tmp/zlib-1.2.8 --conf-path=/tools/nginx/conf/nginx.conf --pid-path=/tools/nginx/run/run.pid --lock-path=/tools/nginx/run/run.lock --http-client-body-temp-path=/data/dataTemp/client_body_temp --http-proxy-temp-path=/data/dataTemp/proxy_temp --with-http_gzip_static_module --with-openssl=/tmp/openssl-1.0.2d

make
%install
make install
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/tools/nginx/{ssl,sites-enabled}
mkdir -p $RPM_BUILD_ROOT/data/dataTemp/{client_body_temp,proxy_temp}
/bin/cp /tools/nginx/ssl/bestpay.key $RPM_BUILD_ROOT/tools/nginx/ssl
/bin/cp /tools/nginx/ssl/bestpay.pem $RPM_BUILD_ROOT/tools/nginx/ssl

%files
/tools/nginx/conf/fastcgi.conf
/tools/nginx/conf/fastcgi.conf.default
/tools/nginx/conf/fastcgi_params
/tools/nginx/conf/fastcgi_params.default
/tools/nginx/conf/koi-utf
/tools/nginx/conf/koi-win
/tools/nginx/conf/mime.types
/tools/nginx/conf/mime.types.default
/tools/nginx/conf/nginx.conf
/tools/nginx/conf/nginx.conf.default
/tools/nginx/conf/scgi_params
/tools/nginx/conf/scgi_params.default
/tools/nginx/conf/uwsgi_params
/tools/nginx/conf/uwsgi_params.default
/tools/nginx/conf/win-utf
/tools/nginx/html/50x.html
/tools/nginx/html/index.html
/tools/nginx/sbin/nginx
/tools/nginx/ssl/bestpay.key
/tools/nginx/ssl/bestpay.pem

%dir
/tools/nginx/ssl
/tools/nginx/sites-enabled
/data/dataTemp/client_body_temp
/data/dataTemp/proxy_temp
%post 
/bin/chown bestpay.bestpay -R /tools/nginx
/bin/chown bestpay.bestpay -R /data/dataTemp
%changelog
