# Create the file school in /tmp
file {'school':
  path    => '/tmp/school',
  ensure  => 'file',
  content => 'I love Puppet',
  group   => 'www-data',
  mode    => '0744',
  owner   => 'www-data',
}
