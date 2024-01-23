# Increase hard file limit to enable holberton user to open
# a file without any error message.

exec {'fix_soft_file_limit':
  command => 'sed -i "/^holberton soft/s/4/40000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

exec {'fix_hard_file_limit':
  command => 'sed -i "/^holberton hard/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin:/bin'
}
