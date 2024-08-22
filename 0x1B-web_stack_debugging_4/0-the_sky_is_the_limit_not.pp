# Fix Nginx "accept4() failed (24: Too many open files)" message when simulting user requests

exec {'modify ULIMIT setting':
  command => 'sed -i "s/15/10000/" /etc/default/nginx && sudo service nginx restart',
  path    => ['/usr/bin', '/usr/sbin']
}
