# Install flask from pip3 using Puppet

# Ensure that pip3 is installed
package { 'python3-pip':
  ensure => installed,
}

# Install Flask using pip3
exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask',
  path    => '/usr/bin',
  require => Package['python3-pip'],
}

