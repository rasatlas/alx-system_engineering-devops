# A Puppet manifest that creates a file in /tmp.
file{ '/tmp/school':
  ensure  => 'present',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'Ilove Puppet'
}
