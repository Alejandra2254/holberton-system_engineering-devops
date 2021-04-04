# create a manifest that kills a process named killmenow
exec {'pkill': # name of the file
    command => 'pkill killmenow' ,
    path    => '/usr/bin/',
}