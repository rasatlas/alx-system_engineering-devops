# 0x08. Networking basics #1

## Resources
### Read or watch:
	- [What is localhost](https://en.wikipedia.org/wiki/Localhost)
	- [What is 0.0.0.0](https://en.wikipedia.org/wiki/0.0.0.0)
	- [What is the hosts file](https://www.makeuseof.com/tag/modify-manage-hosts-file-linux/)
	- [Netcat examples](https://www.thegeekstuff.com/2012/04/nc-command-examples/)
### man or help:
	- `ifconfig`
	- `telnet`
	- `nc`
	- `cut`

## Objectives
- At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
	- What is localhost/127.0.0.1
	- What is 0.0.0.0
	- What is `/etc/hosts`
	- How to display your machine’s active network interfaces

## Requirements
### General
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted on Ubuntu 20.04 LTS
- All your files should end with a new line
- A `README.md` file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- Your Bash script must pass `Shellcheck` (version `0.7.0` via `apt-get`) without any errors
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining what is the script doing

## Tasks
0. Write a Bash script that configures an Ubuntu server with the below requirements.
	- Requirements:
		- localhost resolves to 127.0.0.2
		- facebook.com resolves to 8.8.8.8.
		- The checker is running on Docker
1. Write a Bash script that displays all active IPv4 IPs on the machine it’s executed on.
Example:

```
sylvain@ubuntu$ ./1-show_attached_IPs | cat -e
10.0.2.15$
127.0.0.1$
sylvain@ubuntu$
```

2. Write a Bash script that listens on port 98 on localhost.
**Terminal 0**
Starting my script.

```
sylvain@ubuntu$ sudo ./100-port_listening_on_localhost
```

**Terminal 1**
Connecting to localhost on port 98 using telnet and typing some text.

```
sylvain@ubuntu$ telnet localhost 98
Trying 127.0.0.2...
Connected to localhost.
Escape character is '^]'.
Hello world
test
```

**Terminal 0**
Receiving the text on the other side.

```
sylvain@ubuntu$ sudo ./100-port_listening_on_localhost
Hello world
test
```

