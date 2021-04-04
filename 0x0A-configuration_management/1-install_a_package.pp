# install puppet-lint.
exec {'puppet-lint': # name of the file
    command => 'gem install puppet-lint -v 2.1.1',
    path    => '/usr/bin:/usr/sbin:/bin',
}