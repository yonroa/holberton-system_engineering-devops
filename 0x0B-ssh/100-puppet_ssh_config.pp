# set up your client SSH configuration
include stdlib

file_line { 'Declare identity file':
  ensure  => 'present',
  path    => '/etc/shh/ssh_config',
  line    => '    IdentityFile ~/.ssh/holberton',
  replace => true,
}

file_line { 'Turn off passwd auth':
  ensure  => 'present',
  path    => '/etc/shh/ssh_config',
  line    => '    PasswordAuthentication no',
  replace => true,
}
