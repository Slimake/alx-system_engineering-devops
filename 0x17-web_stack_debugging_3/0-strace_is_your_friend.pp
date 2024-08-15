# Using strace, find out why Apache is returning a 500 error.
# Once you find the issue, fix it and then automate it using Puppet
exec { 'fix-wordpress':
  command => "sed -i 's/class-wp-locale.phpp/class-wp-locale.php/g' wp-settings.php",
  cwd     => '/var/www/html',
  path    => ['/bin', '/usr/bin',]
}
