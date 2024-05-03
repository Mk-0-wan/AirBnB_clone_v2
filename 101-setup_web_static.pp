# creating folders to hold my archived static files

package { 'nginx':
	ensure => 'installed',
}

service { 'nginx':
	ensure => 'running',
}


file { ['/data/, /data/web_static/, 
	/data/web_static/releases/, /data/web_static/shared/,
	/data/web_static/releases/test']:

	ensure 	=> 'directory',
	owner 	=> 'ubuntu',
	group	=> 'ubuntu',
	recurse => 'true',
}

file { '/data/web_static/releases/test/index.html':
	ensure 	=> 'file',
	content => 'Alx Software Engineering School',
}

file { '/data/web_static/current':
	ensure	=> 'link',
	target	=> '/data/web_static/releases/test'
}

exec { '/etc/nginx/sites-available/default':
	command	=> 'sudo sed -i "12i location /hbnb_static {\n alias /data/web_static/current; \n}\n" /etc/nginx/sites-available/default',
}
