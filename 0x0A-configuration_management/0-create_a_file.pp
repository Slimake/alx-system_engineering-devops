# Create a file in /tmp

file {'/tmp/school':
    content  => 'I love Puppet',
    mode  => '0744',
    path  => '/tmp/school',
    owner => 'www-data',
    group => 'www-data'
}
