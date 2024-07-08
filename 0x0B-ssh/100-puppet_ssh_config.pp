# create a manifest that make changes to a configuration file

exec { 'modify_ssh_config':
  command     => "/bin/sed -i \
                    -e 's/^\\s*#*\\s*PasswordAuthentication\\s*no/PasswordAuthentication yes/g' \
                    -e '/^\\s*IdentityFile\\s*~\\/\\.ssh\\/school/d; /Host\\s*/a IdentityFile ~/.ssh/school' \
                    /etc/ssh/ssh_config",
  path        => '/bin:/usr/bin',
  onlyif      => "/bin/grep -q '^\\s*#*\\s*PasswordAuthentication\\s*no' /etc/ssh/ssh_config || /bin/grep -qv '^\\s*IdentityFile\\s*~/.ssh/school' /etc/ssh/ssh_config",
}

