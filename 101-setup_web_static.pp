#!/usr/bin/env bash
# Puppet manifest to set up web servers for web_static deployment

# Install Nginx if not already installed
package { 'nginx':
  ensure => 'installed',
}

# Create necessary directories
file { ['/data', '/data/web_static', '/data/web_static/releases', '/data/web_static/shared']:
  ensure  => 'directory',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0755',
  recurse => true,
}

file { '/data/web_static/releases/test':
  ensure  => 'directory',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0755',
}

# Create a fake HTML file
file { '/data/web_static/releases/test/index.html':
  ensure  => 'file',
  content => '<html>\n<head>\n</head>\n<body>\n  Holberton School\n</body>\n</html>\n',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0644',
}

# Create a symbolic link
file { '/data/web_static/current':
  ensure  => 'link',
  target  => '/data/web_static/releases/test',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0755',
}

# Update Nginx configuration
file { '/etc/nginx/sites-available/default':
  content => template('nginx-default.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Nginx configuration template
file { '/etc/nginx/sites-available/default':
  ensure  => 'file',
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
}

service { 'nginx':
  ensure     => 'running',
  enable     => true,
  subscribe  => File['/etc/nginx/sites-available/default'],
}
