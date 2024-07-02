# Install and configure an Nginx server using Puppet. 
# Also perform a 301 redirect when querying /redirect_me.

$add301_redirect = '\\\n\tlocation /redirect_me {\n\t\t return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;\n\t}'
$add404_notfound = '\\\n\terror_page 404 /custom_404.html;\n\tlocation = /custom_404.html {\n\t\tinternal;\n\t}'

package { 'install_and_configure_nginx':
    ensure => 'installed',
    name   => 'nginx',
}

file { '/var/www/html/index.nginx-debian.html':
    ensure  => file,
    content => 'Hello World!',
}

file { '/var/www/html/custom_404.html':
    ensure  => file,
    content => 'Ceci n\'est pas une page',
}

exec { 'add_301_redirect':
    command => "sed -i '53i ${add301_redirect}' /etc/nginx/sites-available/default",
    path    => '/usr/bin:/usr/sbin:/bin',
}

exec { 'add_404_notfound':
    command => "sed -i '57i ${add404_notfound}' /etc/nginx/sites-available/default",
    path    => '/usr/bin:/usr/sbin:/bin',
}

exec { 'check_and_reload_nginx':
    command => 'nginx -t && service nginx reload',
    path    => '/usr/bin:/usr/sbin:/bin',
}
