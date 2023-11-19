Certainly! Here's an explanation of Master-Slave replication, Sentinel for high availability, and Redis Cluster for horizontal scaling, along with code examples for setting up and using these features in Redis.

**Master-Slave Replication:**

Master-Slave replication in Redis involves creating one or more replica (slave) servers that replicate data from a primary (master) server. This setup provides data redundancy and can be used to scale read operations.

1. **Configuration:**

   In the Redis configuration file (usually `redis.conf`), configure the master server as follows:

   ```conf
   # Master configuration
   port 6379
   bind 127.0.0.1
   requirepass your_password  # Optional: set a password for authentication
   ```

   Then, configure the slave server(s) as follows:

   ```conf
   # Slave configuration
   port 6380
   bind 127.0.0.1
   replicaof 127.0.0.1 6379
   masterauth your_password  # Optional: set the master server's password
   ```

2. **Python Code Example:**

   Use the `redis-py` library to connect to the master and slave servers in Python:

   ```python
   import redis

   # Connect to the master server
   master = redis.Redis(host='localhost', port=6379, password='your_password')

   # Connect to the slave server
   slave = redis.Redis(host='localhost', port=6380, password='your_password')
   ```

3. **Testing Replication:**

   You can test replication by writing data to the master and reading it from the slave. Data written to the master should be automatically replicated to the slave:

   ```python
   # Write data to the master
   master.set('key', 'value')

   # Read the data from the slave
   value = slave.get('key')
   print(value.decode('utf-8'))
   ```

**Sentinel for High Availability:**

Redis Sentinel is a monitoring and failover solution that provides high availability for Redis. It monitors Redis servers and promotes a replica to a master in case the master server fails.

1. **Configuration:**

   Create a Sentinel configuration file (e.g., `sentinel.conf`) with the following content:

   ```conf
   # Sentinel configuration
   sentinel monitor mymaster 127.0.0.1 6379 2
   sentinel down-after-milliseconds mymaster 5000
   sentinel failover-timeout mymaster 60000
   sentinel parallel-syncs mymaster 1
   ```

   In this configuration, you specify the master server's IP, port, and the number of replicas. Adjust the values according to your needs.

2. **Starting Sentinel:**

   Start the Sentinel service with the following command:

   ```
   redis-sentinel /path/to/sentinel.conf
   ```

3. **Python Code Example:**

   Connect to Redis using Sentinel for high availability:

   ```python
   import redis
   from redis.sentinel import Sentinel

   # Create a Sentinel instance
   sentinel = Sentinel([('localhost', 26379)], password='your_password')

   # Connect to the master server via Sentinel
   master = sentinel.master_for('mymaster', password='your_password')

   # Connect to the replica server via Sentinel
   replica = sentinel.slave_for('mymaster', password='your_password')
   ```

**Redis Cluster for Horizontal Scaling:**

Redis Cluster is a way to horizontally scale Redis across multiple servers, providing data sharding and high availability.

1. **Cluster Configuration:**

   Set up a Redis Cluster by creating a configuration file with the cluster nodes and configuring each Redis instance for the cluster. You can use the `redis-trib.rb` script to create the cluster. Ensure that each Redis instance has a unique port and cluster configuration.

2. **Python Code Example:**

   Connect to the Redis Cluster using the `redis-py` library:

   ```python
   from rediscluster import RedisCluster

   # List cluster nodes
   startup_nodes = [
       {"host": "127.0.0.1", "port": "7000"},
       {"host": "127.0.0.1", "port": "7001"},
       # Add more nodes as needed
   ]

   # Create a Redis Cluster client
   rc = RedisCluster(startup_nodes=startup_nodes, decode_responses=True)
   ```

3. **Data Sharding:**

   Data in a Redis Cluster is automatically sharded across multiple Redis instances. When connecting to the cluster, you can use the `rc` client instance to interact with the data, and the client will automatically route commands to the appropriate Redis nodes.

   For example:

   ```python
   rc.set('key', 'value')
   value = rc.get('key')
   ```

Redis Cluster provides horizontal scaling and automatic failover, allowing you to distribute data across multiple Redis servers for increased capacity and fault tolerance.
