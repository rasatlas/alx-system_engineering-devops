# A puppet manifest that kills a process named killmenow.
exec { 'pkill':
  command => '/usr/bin/pkill killmenow'
  
}
