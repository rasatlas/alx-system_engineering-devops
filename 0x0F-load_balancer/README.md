# 0x0F. Load balancer
`DevOps` `SysAdmin`

## Resources
Read or watch:
- [Introduction to load-balancing and HAproxy](https://www.digitalocean.com/community/tutorials/an-introduction-to-haproxy-and-load-balancing-concepts)
- [HTTP header](https://www.techopedia.com/definition/27178/http-header)
- [Debian/Ubuntu HAProxy packages](https://haproxy.debian.net/)

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

## Tasks

__0. Double the number of webservers__ </br>

In this first task you need to configure `web-02` to be identical to `web-01`. Fortunately, you built a Bash script during your [web server project](https://intranet.alxswe.com/projects/266), and they’ll now come in handy to easily configure `web-02`. Remember, always try to automate your work!</br>

Since we’re placing our web servers behind a load balancer for this project, we want to add a custom Nginx response header. The goal here is to be able to track which web server is answering our HTTP requests, to understand and track the way a load balancer works. More in the coming tasks.</br>

Requirements:

- Configure Nginx so that its HTTP response contains a custom header (on `web-01` and `web-02`)
	- The name of the custom HTTP header must be `X-Served-By`
	- The value of the custom HTTP header must be the hostname of the server Nginx is running on
- Write `0-custom_http_response_header` so that it configures a brand new Ubuntu machine to the requirements asked in this task
	- [Ignore](https://github.com/koalaman/shellcheck/wiki/Ignore) [SC2154](https://github.com/koalaman/shellcheck/wiki/SC2154) for `shellcheck`</br>

Example:

```python
sylvain@ubuntu$ curl -sI 34.198.248.145 | grep X-Served-By
X-Served-By: 03-web-01
sylvain@ubuntu$ curl -sI 54.89.38.100 | grep X-Served-By
X-Served-By: 03-web-02
sylvain@ubuntu$
```

__1. Install your load balancer__ </br>

Install and configure HAproxy on your `lb-01` server.</br>

Requirements: </br>
- Configure HAproxy so that it send traffic to `web-01` and `web-02`
- Distribute requests using a roundrobin algorithm
- Make sure that HAproxy can be managed via an init script
- Make sure that your servers are configured with the right hostnames: `[STUDENT_ID]-web-01` and `[STUDENT_ID]-web-02`. If not, follow this [tutorial](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/set-hostname.html).
- For your answer file, write a Bash script that configures a new Ubuntu machine to respect above requirements</br>

Example:

```python
sylvain@ubuntu$ curl -Is 54.210.47.110
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Mon, 27 Feb 2017 06:12:17 GMT
Content-Type: text/html
Content-Length: 30
Last-Modified: Tue, 21 Feb 2017 07:21:32 GMT
Connection: keep-alive
ETag: "58abea7c-1e"
X-Served-By: 03-web-01
Accept-Ranges: bytes

sylvain@ubuntu$ curl -Is 54.210.47.110
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Mon, 27 Feb 2017 06:12:19 GMT
Content-Type: text/html
Content-Length: 612
Last-Modified: Tue, 04 Mar 2014 11:46:45 GMT
Connection: keep-alive
ETag: "5315bd25-264"
X-Served-By: 03-web-02
Accept-Ranges: bytes

sylvain@ubuntu$
```

__2. Add a custom HTTP header with Puppet__ </br>

Just as in task #0, we’d like you to automate the task of creating a custom HTTP header response, but with Puppet.
- The name of the custom HTTP header must be `X-Served-By`
- The value of the custom HTTP header must be the hostname of the server Nginx is running on
- Write `2-puppet_custom_http_response_header.pp` so that it configures a brand new Ubuntu machine to the requirements asked in this task
