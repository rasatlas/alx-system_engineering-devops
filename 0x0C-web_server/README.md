# 0x0C. Web server
`DevOps` `SysAdmin`

## Learning Objectives 
### General
- What is the main role of a web server
- What is a child process
- Why web servers usually have a parent process and child processes
- What are the main HTTP requests
### DNS
- What DNS stands for
- What is DNS main role
### DNS Record Types
- `A`
- `CNAME`
- `TXT`
- `MX`

## Requirements
### General
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted on `Ubuntu 16.04 LTS`
- All your files should end with a new line
- A `README.md` file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- Your Bash script must pass `Shellcheck` (version `0.3.7`) without any error
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining what is the script doing
- You can’t use `systemctl` for restarting a process

## Tasks

__0. Transfer a file to your server__</br>
Write a Bash script that transfers a file from our client to a server:</br>

Requirements:
- Accepts 4 parameters
    1. The path to the file to be transferred
    2. The IP of the server we want to transfer the file to
    3. The username `scp` connects with
    4. The path to the SSH private key that `scp` uses
- Display `Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY` if less than 3 parameters passed
- `scp` must transfer the file to the user home directory `~/`
- Strict host key checking must be disabled when using `scp`</br>
Example:
```bash
sylvain@ubuntu$ ./0-transfer_file
Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY
sylvain@ubuntu$
sylvain@ubuntu$ ssh ubuntu@8.8.8.8 -i /vagrant/sylvain 'ls ~/'
afile
sylvain@ubuntu$
sylvain@ubuntu$ touch some_page.html
sylvain@ubuntu$ ./0-transfer_file some_page.html 8.8.8.8 sylvain /vagrant/private_key
some_page.html                                     100%   12     0.1KB/s   00:00
sylvain@ubuntu$ ssh ubuntu@8.8.8.8 -i /vagrant/private_key 'ls ~/'
afile
some_page.html
sylvain@ubuntu$
```

In this example, I:</br>

- remotely execute the `ls ~/` command via `ssh` to see what `~/` contains
- create a file named `some_page.html`
- execute my `0-transfer_file` script
- remotely execute the `ls ~/` command via `ssh` to see that the file `some_page.html` has been successfully transferred</br>
That is one way of publishing your website pages to your server.

__1. Install nginx web server__</br>
Web servers are the piece of software generating and serving HTML pages, let’s install one!</br>

Requirements:
- Install `nginx` on your `web-01`
- server
- Nginx should be listening on port 80
- When querying Nginx at its root `/` with a GET request (requesting a page) using `curl`, it must return a page that contains the string `Hello World!`
- As an answer file, write a Bash script that configures a new Ubuntu machine to respect above requirements (this script will be run on the server itself)
- You can’t use `systemctl` for restarting `nginx`</br>

Server terminal:
```bash
root@sy-web-01$ ./1-install_nginx_web_server > /dev/null 2>&1
root@sy-web-01$
root@sy-web-01$ curl localhost
Hello World!
root@sy-web-01$
```
Local terminal:
```bash
sylvain@ubuntu$ curl 34.198.248.145/
Hello World!
sylvain@ubuntu$ curl -sI 34.198.248.145/
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 21 Feb 2017 23:43:22 GMT
Content-Type: text/html
Content-Length: 30
Last-Modified: Tue, 21 Feb 2017 07:21:32 GMT
Connection: keep-alive
ETag: "58abea7c-1e"
Accept-Ranges: bytes

sylvain@ubuntu$
```
In this example `34.198.248.145` is the IP of my `web-01` server. If you want to query the Nginx that is locally installed on your server, you can use `curl 127.0.0.1`.</br>

If things are not going as expected, make sure to check out Nginx logs, they can be found in `/var/log/`.</br>

__Maarten’s PRO-tip:__ When you use `sudo su` on your web-01 you can become root like this to test your file:
```bash
sylvain@ubuntu$ sudo su
root@ubuntu#
```
