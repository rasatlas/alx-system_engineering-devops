- Link to [`1. Distributed web infrastructure Design`](https://github.com/rasatlas/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/1%20-%20Distributed%20Web%20Infrastructure.png)

- This implementation adds `load-balancer` and replication of a server.

- The load-balancer uses `Round-Robin Load Balancing` and an `active-active` configuration instead of active-passive configuration. In an active-passive configuration, the server load balancer recognizes a failed node and redirects traffic to the next available node. In an active-active configuration, the load balancer spreads out the workload's traffic among multiple nodes.

- The system doesn't implement `security certificate` for secure communication. So it uses the insecure `HTTP` for data transfers between client and servers.

- The system doesn't also implement any `monitoring mechanism` which makes it difficult to measure the different performance metrices of the system, which might help in decision making and problem solving.
