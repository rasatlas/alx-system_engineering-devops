# Puppet manifest that installs flask from pip3. Version must be 2.1.0
package{'flask 2.1.0':
  ensure   => installed,
  provider => 'pip3'
}
