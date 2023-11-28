# Client configuration file using puppet

file {'/home/vagrant/alx/alx-system_engineering-devops/0x0B-ssh/school':
    ensure  => file,
    content => "Host 34.202.164.88 
        IdentityFile ~/.ssh/school
        PasswordAuthentication no",
}
