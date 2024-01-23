# A script to increase the amount of requests an nginx server can handle
# Increase the ULIMIT of the default nginx file
exec { 'fix_ulimit':
  command => '/usr/bin/sudo /bin/sed -i "s/15/4096/" /etc/default/nginx',
  before  => Exec['restart'],
}

exec { 'restart':
  command => '/usr/bin/sudo /usr/sbin/service nginx restart',
}
