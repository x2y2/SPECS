Name:           nginx
Version:        1.8.1
Release:	1
Summary:        nginx rpm

Group:          Library
License:        GPL
            
Source0:       %{name}-%{version}.tar.gz 


%description


%prep
%setup -q


%build
./configure \
  --prefix=/tools/nginx  \
  --with-pcre=/tmp/pcre-8.37 \
  --with-zlib=/tmp/zlib-1.2.8 \
  --conf-path=/tools/nginx/conf/nginx.conf \
  --pid-path=/tools/nginx/run/run.pid \
  --lock-path=/tools/nginx/run/run.lock \
  --http-client-body-temp-path=/data/dataTemp/client_body_temp \
  --http-proxy-temp-path=/data/dataTemp/proxy_temp \
  --with-openssl=/tmp/openssl-1.0.2d \
  --with-http_stub_status_module \
  --with-http_gzip_static_module

make
%install
make install DESTDIR=$RPM_BUILD_ROOT
%clean
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/tools/nginx/{ssl,sites-enabled}
mkdir -p $RPM_BUILD_ROOT/data/dataTemp/{client_body_temp,proxy_temp}
/bin/cp /tmp/bestpay.key $RPM_BUILD_ROOT/tools/nginx/ssl
/bin/cp /tmp/bestpay.pem $RPM_BUILD_ROOT/tools/nginx/ssl

%files
/tools/nginx/conf/*
/tools/nginx/html/*
/tools/nginx/sbin/*
/tools/nginx/ssl/*

%dir
/tools/nginx/ssl
/tools/nginx/sites-enabled
/tools/nginx/run
/tools/nginx/logs
/data/dataTemp/client_body_temp
/data/dataTemp/proxy_temp
%post 
/bin/chown bestpay.bestpay -R /tools/nginx
/bin/chown bestpay.bestpay -R /data/dataTemp
ln -sf /tools/nginx/sbin/nginx /sbin/nginx
if [ ! -d /etc/nginx ];then
  mkdir /etc/nginx
fi
ln -sf /tools/nginx/conf/nginx.conf /etc/nginx/nginx.conf
%changelog
