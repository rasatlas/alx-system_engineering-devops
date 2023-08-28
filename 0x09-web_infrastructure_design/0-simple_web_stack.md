- Link to [`0. Simple web stack Design`](https://github.com/rasatlas/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/0%20-%20Simple%20Web%20Stack.png)

- __What is a server__
    - Servers are located in datacenters which are buildings that host hundreds, or even thousands of computers (servers). You can think of a server as a computer without a keyboard, mouse, or screen, that is accessible only by a network. A server can be physical or virtual. A server runs an OS (operating system).

- __What is the role of the domain name__
    - Domain names provide an easy way to recognize and memorize the names using the numerically addressed Internet resources.
    - It is used to address the Internet resources placed on internet or it provides and abstraction that allows the resources to be moved from one place to another in hierarchy.
    - It provides a way to move the resources in a topological form and provide the translation to be done using the IP addresses and domain names.
    - Domain names provide a way to the registrants to refer to the domain owners for their registration of the domain and have the ownership of it.

- __What type of DNS record www is in `www.foobar.com`__
    - It is a CNAME DNS record. It's a subdomain which points to the SLD (Second Level Domain) foobar.com in the CNAME DNS record.
    - This subdomain contains a website's homepage and its most important pages. The www subdomain is so widely used that most domain registrars include it with domain name purchases.

- __What is the role of the web server__
    - The primary role of a web server is to store, process, and deliver requested information or webpages to end users.

- __What is the role of the application server__
    - The function of the application server is to act as host (or container) for the user's business logic while facilitating access to and performance of the business application.

- __What is the role of the database__
    - The role of the DB is efficient data management which involves CRUD operations.

- __What is the server using to communicate with the computer of the user requesting the website__
    - The server uses HTTP request to communicate with clients. If security and encryption is needed it uses HTTPS.

- The above implementation of simple web stack has a single point of failure (SPOF) since it doesn't implement any form of redundancy.

- When maintenance is needed the downtime of the system is equal to the amount of time it takes to maintain and re-run the server.
