import json

questions = []

def add_q(id, category, question, options, explanation, hint):
    questions.append({
        "id": id,
        "category": category,
        "question": question,
        "options": [{"text": o[0], "correct": o[1]} for o in options],
        "explanation": explanation,
        "hint": hint
    })

# ============================================================
# Domain 1: Design Resilient Architectures (30 questions)
# ============================================================
add_q(1, "Design Resilient Architectures",
     "A company needs to deploy a web application with automatic scaling and high availability across multiple Availability Zones. Which combination of AWS services should they use?",
     [("EC2 in a single AZ with Auto Scaling", False),
      ("EC2 across multiple AZs with Auto Scaling and an Application Load Balancer", True),
      ("EC2 in a single AZ with a Classic Load Balancer", False),
      ("Lambda with no load balancer", False)],
     "Deploying EC2 instances across multiple AZs with Auto Scaling and an ALB provides both high availability and fault tolerance. Multi-AZ ensures the application survives an AZ failure.",
     "Think about high availability: you need multiple AZs, a load balancer, and auto scaling.")

add_q(2, "Design Resilient Architectures",
     "A company wants to implement a disaster recovery strategy with an RPO of 1 hour and RTO of 4 hours. Which DR strategy is MOST cost-effective while meeting these requirements?",
     [("Backup and Restore", False),
      ("Pilot Light", True),
      ("Warm Standby", False),
      ("Multi-Site Active-Active", False)],
     "Pilot Light maintains a minimal version of your environment in the DR region, keeping critical databases and core infrastructure running. It provides a good balance between cost and recovery time, suitable for 1-hour RPO and 4-hour RTO.",
     "Pilot Light sits between Backup/Restore and Warm Standby in terms of cost vs recovery speed.")

add_q(3, "Design Resilient Architectures",
     "Which AWS service provides automatic failover at the DNS level when an endpoint becomes unhealthy?",
     [("Route 53 Latency-Based Routing", False),
      ("Route 53 Health Checks and Failover Routing", True),
      ("CloudFront with Origin Failover", False),
      ("Elastic Load Balancing", False)],
     "Route 53 health checks can monitor endpoint health and automatically redirect traffic to a healthy endpoint using failover routing policies. This provides DNS-level failover for disaster recovery scenarios.",
     "Route 53 can automate DNS failover based on health check status.")

add_q(4, "Design Resilient Architectures",
     "What is the durability SLA for Amazon S3 Standard storage class?",
     [("99.9%", False),
      ("99.99%", False),
      ("99.999999999%", True),
      ("100%", False)],
     "Amazon S3 Standard is designed for 99.999999999% (11 nines) durability, meaning if you store 10,000 objects, you can expect to lose one object once every 10 million years on average.",
     "S3 Standard has 11 nines of durability.")

add_q(5, "Design Resilient Architectures",
     "A company has an application that must survive the failure of an entire AWS Region. What architecture pattern should they implement?",
     [("Multi-AZ deployment within a single Region", False),
      ("Cross-Region replication with active-passive failover", True),
      ("Single EC2 instance with EBS snapshots", False),
      ("AWS OpsWorks Stacks", False)],
     "Cross-Region replication with active-passive failover ensures that if an entire AWS Region goes down, traffic can be redirected to the secondary Region. Multi-AZ only protects against AZ-level failures, not Region-level.",
     "Region-level resilience requires cross-Region replication and failover.")

add_q(6, "Design Resilient Architectures",
     "Which S3 feature allows you to maintain copies of objects across different AWS Regions for disaster recovery?",
     [("S3 Versioning", False),
      ("S3 Cross-Region Replication (CRR)", True),
      ("S3 Transfer Acceleration", False),
      ("S3 Object Lock", False)],
     "S3 Cross-Region Replication automatically replicates objects to a destination bucket in another Region. This is essential for disaster recovery when you need data redundancy across Regions.",
     "CRR replicates S3 objects to another Region for DR purposes.")

add_q(7, "Design Resilient Architectures",
     "A solutions architect needs to ensure that an Amazon RDS database can automatically fail over to a standby instance when the primary fails. Which RDS feature should be used?",
     [("Read Replicas", False),
      ("Multi-AZ Deployment", True),
      ("RDS Snapshots", False),
      ("RDS Proxy", False)],
     "RDS Multi-AZ deployment provides automatic failover to a standby instance in a different AZ. The primary and standby instances are synchronously replicated, ensuring no data loss during failover.",
     "Multi-AZ provides automatic failover with synchronous replication.")

add_q(8, "Design Resilient Architectures",
     "An application running on EC2 instances behind an ALB experiences a sudden traffic spike. What should the architect configure to handle this automatically?",
     [("AWS Shield", False),
      ("Target Tracking Scaling Policy based on ALB request count", True),
      ("Scheduled Scaling", False),
      ("EC2 Instance Store", False)],
     "A Target Tracking scaling policy can automatically adjust the number of EC2 instances based on a metric like ALB request count per target. This ensures the application scales out when traffic increases.",
     "Auto Scaling with target tracking automatically adjusts capacity based on demand.")

add_q(9, "Design Resilient Architectures",
     "What is the minimum availability SLA for Amazon S3 Standard?",
     [("99.9%", False),
      ("99.99%", True),
      ("99.999%", False),
      ("99.999999999%", False)],
     "Amazon S3 Standard is designed for 99.99% availability. Durability (11 nines) and availability (4 nines) are different SLAs. Durability refers to data persistence, while availability refers to the ability to access the service.",
     "S3 availability is 99.99% (4 nines).")

add_q(10, "Design Resilient Architectures",
     "A company needs to distribute content globally with low latency. Which AWS service provides this capability?",
     [("Amazon S3 Transfer Acceleration", False),
      ("AWS Global Accelerator", False),
      ("Amazon CloudFront", True),
      ("AWS Direct Connect", False)],
     "CloudFront is a Content Delivery Network (CDN) with a global network of edge locations. It caches content at the edge to deliver low-latency access to users worldwide.",
     "CloudFront is AWS's CDN for global content distribution with low latency.")

add_q(11, "Design Resilient Architectures",
     "Which of the following is a benefit of using AWS Elastic Beanstalk for application deployment?",
     [("It automatically provisions servers and manages capacity", False),
      ("It provides a fully managed database service", False),
      ("It handles deployment, capacity provisioning, load balancing, and auto scaling automatically", True),
      ("It provides DDoS protection at no extra cost", False)],
     "Elastic Beanstalk is a PaaS service that automatically handles the deployment details, from capacity provisioning and load balancing to auto scaling and application health monitoring, based on the code you provide.",
     "Elastic Beanstalk automates the entire deployment pipeline including scaling.")

add_q(12, "Design Resilient Architectures",
     "A company uses Amazon DynamoDB and needs a multi-Region active-active setup with automatic conflict resolution. Which feature should they use?",
     [("DynamoDB Global Tables", True),
      ("DynamoDB Streams", False),
      ("DynamoDB Accelerator (DAX)", False),
      ("DynamoDB Point-in-Time Recovery", False)],
     "DynamoDB Global Tables provide a fully managed multi-Region active-active database with automatic conflict resolution. Last writer wins (LWW) is the default conflict resolution strategy.",
     "Global Tables enable active-active multi-Region DynamoDB with conflict resolution.")

add_q(13, "Design Resilient Architectures",
     "What happens to data stored on an EC2 instance's instance store when the instance is stopped or terminated?",
     [("Data persists after stop and terminate", False),
      ("Data persists after stop but is lost on terminate", False),
      ("Data is lost when the instance is stopped or terminated", True),
      ("Data is automatically backed up to S3", False)],
     "Instance store volumes are ephemeral storage physically attached to the host computer. Data in instance store is lost when the instance is stopped, terminated, or if the underlying host fails.",
     "Instance store is ephemeral - data is lost on stop or terminate.")

add_q(14, "Design Resilient Architectures",
     "Which AWS service helps protect applications from Distributed Denial of Service (DDoS) attacks?",
     [("AWS WAF", False),
      ("AWS Shield Standard", True),
      ("AWS GuardDuty", False),
      ("AWS Inspector", False)],
     "AWS Shield Standard provides automatic, always-on DDoS protection for all AWS customers at no additional cost. It protects against common network and transport layer DDoS attacks. AWS Shield Advanced provides enhanced protection for a fee.",
     "AWS Shield Standard provides free automatic DDoS protection for all AWS customers.")

add_q(15, "Design Resilient Architectures",
     "A company needs to design a fault-tolerant architecture for a stateless web application. Which combination provides the highest fault tolerance?",
     [("Single EC2 instance with EBS", False),
      ("Multiple EC2 instances across AZs with ALB and Auto Scaling", True),
      ("Single Lambda function in one Region", False),
      ("ECS on a single EC2 instance", False)],
     "Multiple EC2 instances across multiple AZs with an ALB and Auto Scaling provides the highest fault tolerance. If any single instance or even an entire AZ fails, the application continues to serve traffic from healthy instances in other AZs.",
     "Maximum fault tolerance requires distributing compute across multiple AZs with a load balancer.")

add_q(16, "Design Resilient Architectures",
     "What is the difference between a Warm Standby and a Multi-Site Active-Active DR strategy?",
     [("Warm Standby runs in one Region; Multi-Site runs in two", False),
      ("Warm Standby has a scaled-down secondary environment; Multi-Site runs full capacity in both Regions", True),
      ("There is no difference", False),
      ("Warm Standby is faster to failover than Multi-Site", False)],
     "Warm Standby maintains a scaled-down version of your environment in the DR Region that you scale up during failover. Multi-Site Active-Active runs full capacity in both Regions simultaneously, providing the fastest recovery but at the highest cost.",
     "Warm Standby is scaled down in DR; Active-Active runs full capacity everywhere.")

add_q(17, "Design Resilient Architectures",
     "Which Route 53 routing policy routes traffic to multiple resources and returns multiple values?",
     [("Simple Routing", False),
      ("Weighted Routing", False),
      ("Multivalue Answer Routing", True),
      ("Geolocation Routing", False)],
     "Multivalue Answer routing lets Route 53 respond to DNS queries with up to eight healthy records. It can return multiple IP addresses and the client chooses one, providing basic load balancing and health checking at the DNS level.",
     "Multivalue Answer routing returns multiple healthy IPs for a query.")

add_q(18, "Design Resilient Architectures",
     "A company uses Amazon Aurora and needs to replicate data across AWS Regions for disaster recovery. Which Aurora feature provides this?",
     [("Aurora Read Replicas in the same Region", False),
      ("Aurora Global Database", True),
      ("Aurora Fast Database Cloning", False),
      ("Aurora Backtrack", False)],
     "Aurora Global Database replicates data across AWS Regions with typically less than 1 second replication lag. It supports fast failover (under 1 minute) and provides a fully managed cross-Region disaster recovery solution.",
     "Aurora Global Database provides cross-Region replication for disaster recovery.")

add_q(19, "Design Resilient Architectures",
     "When an EC2 instance in an Auto Scaling group fails health checks, what happens by default?",
     [("It is immediately terminated and replaced", True),
      ("It is left running but marked as unhealthy", False),
      ("The ASG waits 300 seconds before taking action", False),
      ("The instance is stopped and restarted", False)],
     "When an EC2 instance fails EC2 or ELB health checks, the Auto Scaling group marks it unhealthy and by default terminates and replaces it with a new instance. This ensures the desired capacity is maintained.",
     "Auto Scaling automatically replaces unhealthy instances.")

add_q(20, "Design Resilient Architectures",
     "Which AWS service provides a managed service for running containers without needing to manage the underlying infrastructure?",
     [("Amazon EC2", False),
      ("AWS Elastic Beanstalk", False),
      ("AWS Fargate", True),
      ("Amazon Lightsail", False)],
     "AWS Fargate is a serverless compute engine for containers. It works with both ECS and EKS, allowing you to run containers without having to manage servers, handle capacity planning, or isolate workloads.",
     "Fargate provides serverless container execution without managing infrastructure.")

add_q(21, "Design Resilient Architectures",
     "A company needs to ensure that their on-premises data center can fail over to AWS during a disaster. Which AWS service facilitates this hybrid DR scenario?",
     [("AWS Storage Gateway", True),
      ("AWS Snowball", False),
      ("AWS Direct Connect", False),
      ("AWS VPN CloudHub", False)],
     "AWS Storage Gateway connects on-premises software appliances with cloud-based storage. The File Gateway, Volume Gateway, and Tape Gateway modes allow seamless hybrid cloud integration and disaster recovery scenarios.",
     "Storage Gateway bridges on-premises infrastructure with AWS for DR.")

add_q(22, "Design Resilient Architectures",
     "Which type of health check does an Application Load Balancer perform?",
     [("TCP-level health checks only", False),
      ("HTTP/HTTPS health checks at the target level", True),
      ("DNS-level health checks", False),
      ("ICMP ping health checks", False)],
     "ALB performs health checks at the application layer (Layer 7) using HTTP or HTTPS requests. It checks the health of individual targets (EC2 instances, Lambda functions, or other targets) and routes traffic only to healthy ones.",
     "ALB performs Layer 7 HTTP/HTTPS health checks on individual targets.")

add_q(23, "Design Resilient Architectures",
     "A company wants to use CloudFront to serve content from an S3 bucket, but also wants a failover origin if the primary S3 bucket becomes unavailable. How can this be achieved?",
     [("Use CloudFront Origin Groups", True),
      ("Use Route 53 Failover Routing", False),
      ("Use two CloudFront distributions", False),
      ("Use S3 Cross-Region Replication only", False)],
     "CloudFront Origin Groups allow you to specify a primary and secondary origin. If the primary origin returns specific error codes (403, 404, 500, 502, 503, 504), CloudFront automatically fails over to the secondary origin.",
     "CloudFront Origin Groups provide failover between primary and secondary origins.")

add_q(24, "Design Resilient Architectures",
     "Which Auto Scaling group attribute determines the minimum number of instances that must remain healthy in order to be considered successful?",
     [("Desired capacity", False),
      ("Min size", False),
      ("Health check grace period", False),
      ("Default instance warmup", False)],
     "The min size defines the minimum number of instances the ASG will maintain. If the number of healthy instances falls below this threshold, Auto Scaling will launch new instances to replace unhealthy ones and maintain the minimum.",
     "Min size ensures the ASG always maintains at least that many instances.")

add_q(25, "Design Resilient Architectures",
     "Which AWS service provides automated cross-region disaster recovery for EC2 instances?",
     [("AWS Elastic Disaster Recovery (DRS)", True),
      ("AWS Systems Manager", False),
      ("AWS Migration Hub", False),
      ("AWS Application Migration Service", False)],
     "AWS Elastic Disaster Recovery (DRS) minimizes downtime and data loss with fast, reliable recovery of on-premises and cloud-based applications. It provides automated server replication, continuous data protection, and streamlined recovery.",
     "AWS DRS provides automated cross-Region disaster recovery for EC2.")

add_q(26, "Design Resilient Architectures",
     "What is the primary advantage of using Amazon S3 Object Lock for compliance requirements?",
     [("Faster upload speeds", False),
      ("Prevents objects from being deleted or overwritten for a retention period", True),
      ("Reduces storage costs", False),
      ("Enables cross-region replication", False)],
     "S3 Object Lock helps prevent objects from being deleted or overwritten for a fixed amount of time or indefinitely. It supports two retention modes: Governance mode and Compliance mode, helping meet regulatory compliance requirements.",
     "Object Lock provides Write-Once-Read-Many (WORM) protection for compliance.")

add_q(27, "Design Resilient Architectures",
     "A solutions architect needs to design a system that processes messages in a queue with exactly-once processing semantics. Which service should they choose?",
     [("Amazon SQS Standard", False),
      ("Amazon SQS FIFO", True),
      ("Amazon SNS", False),
      ("Amazon Kinesis Data Streams", False)],
     "Amazon SQS FIFO queues provide exactly-once processing by ensuring that messages are delivered once and remain available until a consumer processes them and deletes them. Duplicate messages are prevented through deduplication.",
     "SQS FIFO queues provide exactly-once processing semantics.")

add_q(28, "Design Resilient Architectures",
     "Which AWS feature allows you to run EC2 instances in multiple Regions and route traffic to the closest Region?",
     [("Amazon Route 53 Geoproximity Routing", True),
      ("Amazon CloudFront", False),
      ("AWS Global Accelerator", False),
      ("Amazon VPC Peering", False)],
     "Route 53 Geoproximity routing lets you route traffic based on the geographic location of users and resources. You can bias traffic routing to shift more traffic to one Region using a bias value, providing flexible traffic management across Regions.",
     "Route 53 Geoproximity routing sends traffic to the closest Region with bias control.")

add_q(29, "Design Resilient Architectures",
     "A company uses an Amazon EKS cluster and needs to ensure pods are distributed across multiple AZs for high availability. Which Kubernetes feature should they configure?",
     [("Horizontal Pod Autoscaler", False),
      ("Pod Disruption Budgets", False),
      ("Topology Spread Constraints", True),
      ("Resource Quotas", False)],
     "Topology Spread Constraints in Kubernetes allow you to control how pods are spread across failure domains like AZs or nodes. This ensures that pods are evenly distributed across multiple AZs, improving application availability.",
     "Topology Spread Constraints distribute pods across AZs in EKS.")

add_q(30, "Design Resilient Architectures",
     "Which Amazon EBS volume type provides the highest durability?",
     [("EBS Cold HDD", False),
      ("EBS Throughput Optimized HDD", False),
      ("All EBS volume types have the same durability SLA", True),
      ("EBS General Purpose SSD (gp3)", False)],
     "All Amazon EBS volume types provide the same durability: 99.8% - 99.9%. The differences between EBS volume types are in performance (IOPS, throughput) and cost, not durability.",
     "All EBS volume types share the same durability SLA.")

# ============================================================
# Domain 2: Design High-Performing Architectures (30 questions)
# ============================================================
add_q(31, "Design High-Performing Architectures",
     "Which EC2 instance type family is optimized for applications requiring high memory capacity?",
     [("C family (Compute Optimized)", False),
      ("M family (General Purpose)", False),
      ("R family (Memory Optimized)", True),
      ("I family (Storage Optimized)", False)],
     "R family instances are optimized for memory-intensive applications such as large in-memory databases, real-time big data analytics, and in-memory caching. They offer high memory-to-CPU ratios.",
     "R (memory optimized) family is best for high memory workloads.")

add_q(32, "Design High-Performing Architectures",
     "Which AWS storage service provides the highest IOPS performance for EC2 workloads?",
     [("Amazon S3", False),
      ("Amazon EBS Provisioned IOPS SSD (io2)", True),
      ("Amazon EFS", False),
      ("Amazon Instance Store", False)],
     "Amazon EBS Provisioned IOPS SSD volumes (io2) deliver the highest performance for EBS, with up to 64,000 IOPS per volume. They are designed for I/O-intensive database and application workloads.",
     "EBS io2 volumes provide the highest IOPS for block storage.")

add_q(33, "Design High-Performing Architectures",
     "A company needs a shared file system that can be accessed simultaneously by hundreds of EC2 instances across multiple AZs. Which service should they use?",
     [("Amazon EBS", False),
      ("Amazon S3", False),
      ("Amazon EFS", True),
      ("AWS Storage Gateway", False)],
     "Amazon EFS is a serverless, elastic file system that can be mounted by thousands of EC2 instances simultaneously across multiple AZs. It provides a simple, scalable, and elastic NFS file system for Linux-based workloads.",
     "EFS provides a scalable shared file system accessible from multiple EC2 instances.")

add_q(34, "Design High-Performing Architectures",
     "Which caching strategy uses Amazon ElastiCache to reduce database load by caching query results?",
     [("Write-through caching", True),
      ("Lazy loading", False),
      ("Read replicas only", False),
      ("Database sharding", False)],
     "Write-through caching writes data to the cache whenever data is written to the database. When reading, the cache is checked first. This ensures data consistency and reduces database read load significantly.",
     "Write-through caching keeps the cache synchronized with the database.")

add_q(35, "Design High-Performing Architectures",
     "A company wants to reduce latency for their global API users. Which combination of services provides the best performance?",
     [("Amazon API Gateway + Lambda in us-east-1", False),
      ("Amazon CloudFront + Lambda@Edge + API Gateway", True),
      ("AWS Global Accelerator + EC2 in one Region", False),
      ("Amazon Route 53 + EC2 in one AZ", False)],
     "CloudFront with Lambda@Edge and API Gateway provides the best global performance. CloudFront caches responses at edge locations worldwide, and Lambda@Edge executes code at the edge to minimize latency for API requests.",
     "CloudFront + Lambda@Edge minimizes global API latency.")

add_q(36, "Design High-Performing Architectures",
     "Which S3 storage class is designed for frequently accessed data with the lowest latency?",
     [("S3 Standard", True),
      ("S3 Standard-IA", False),
      ("S3 One Zone-IA", False),
      ("S3 Glacier", False)],
     "S3 Standard is designed for frequently accessed data and provides the lowest latency among S3 storage classes. It delivers high throughput and low latency for a wide variety of workloads.",
     "S3 Standard provides the lowest latency for frequently accessed data.")

add_q(37, "Design High-Performing Architectures",
     "Which Amazon DynamoDB feature improves read performance by caching query results?",
     [("DynamoDB Streams", False),
      ("DynamoDB Accelerator (DAX)", True),
      ("DynamoDB Global Tables", False),
      ("DynamoDB Point-in-Time Recovery", False)],
     "DAX is a fully managed, highly available, in-memory cache for DynamoDB. It delivers up to 10x performance improvement by reducing read latency from milliseconds to microseconds, even at millions of requests per second.",
     "DAX caches DynamoDB data in memory for microsecond read latency.")

add_q(38, "Design High-Performing Architectures",
     "A database workload requires consistent, sub-millisecond latency and single-digit millisecond response times. Which AWS database service is best suited?",
     [("Amazon RDS MySQL", False),
      ("Amazon DynamoDB", True),
      ("Amazon Redshift", False),
      ("Amazon Neptune", False)],
     "DynamoDB provides single-digit millisecond performance at any scale. Its serverless, distributed architecture ensures consistent, low-latency response times regardless of the size of the dataset or the request rate.",
     "DynamoDB delivers consistent single-digit millisecond latency at any scale.")

add_q(39, "Design High-Performing Architectures",
     "Which AWS service provides a managed NoSQL database with flexible schema that supports both document and key-value data models?",
     [("Amazon RDS", False),
      ("Amazon DynamoDB", False),
      ("Amazon DocumentDB", True),
      ("Amazon Neptune", False)],
     "Amazon DocumentDB is a fully managed, MongoDB-compatible database service. It supports document data models, providing the flexibility of NoSQL with the familiarity of MongoDB APIs.",
     "DocumentDB is AWS's managed MongoDB-compatible document database.")

add_q(40, "Design High-Performing Architectures",
     "A company needs to accelerate data transfer between their on-premises data center and AWS. Which service provides the lowest, consistent network latency?",
     [("AWS Site-to-Site VPN", False),
      ("AWS Direct Connect", True),
      ("AWS Transit Gateway", False),
      ("Amazon CloudFront", False)],
     "AWS Direct Connect establishes a dedicated private network connection between your on-premises data center and AWS. It provides lower latency, higher bandwidth, and more consistent network performance than internet-based connections.",
     "Direct Connect provides dedicated, low-latency connectivity to AWS.")

add_q(41, "Design High-Performing Architectures",
     "Which EC2 instance type is best suited for graphics-intensive workloads like machine learning training?",
     [("P family (GPU instances)", True),
      ("T family (Burstable)", False),
      ("M family (General Purpose)", False),
      ("D family (Dense Storage)", False)],
     "P family instances (GPU instances) are optimized for graphics-intensive and machine learning workloads. They feature NVIDIA GPUs that are ideal for parallel processing tasks like ML training, rendering, and video encoding.",
     "P family GPU instances are designed for ML training and graphics workloads.")

add_q(42, "Design High-Performing Architectures",
     "A company wants to use a caching layer to improve database read performance. Which ElastiCache engine supports both cluster mode and replication groups for horizontal scaling?",
     [("Memcached", False),
      ("Redis", True),
      ("Both support cluster mode equally", False),
      ("Neither supports cluster mode", False)],
     "ElastiCache for Redis supports cluster mode for horizontal partitioning (sharding) of data across multiple nodes, as well as replication groups for high availability. Memcached only supports basic partitioning via client-side sharding.",
     "ElastiCache Redis supports cluster mode and replication groups.")

add_q(43, "Design High-Performing Architectures",
     "Which Amazon RDS feature allows read-heavy database workloads to scale read capacity independently of write capacity?",
     [("Multi-AZ Deployment", False),
      ("Read Replicas", True),
      ("RDS Proxy", False),
      ("RDS Custom", False)],
     "RDS Read Replicas allow you to create one or more read-only copies of your database. This enables you to scale read capacity horizontally by distributing read queries across multiple replicas.",
     "Read Replicas offload read traffic from the primary database instance.")

add_q(44, "Design High-Performing Architectures",
     "What is the maximum throughput supported by Amazon S3 Standard for a single object?",
     [("100 MB/s per object", False),
      ("3,500 PUT/COPY/POST/LIST requests per second per prefix", True),
      ("10,000 requests per second per prefix", False),
      ("Unlimited with no throttling", False)],
     "S3 Standard supports 3,500 PUT/COPY/POST/LIST requests per second per prefix, and 5,500 GET/SELECT requests per second per prefix. There are no limits to the number of prefixes in a bucket.",
     "S3 supports 3,500 write and 5,500 read requests per second per prefix.")

add_q(45, "Design High-Performing Architectures",
     "Which AWS service provides a fully managed, petabyte-scale data warehouse for analytics workloads?",
     [("Amazon Aurora", False),
      ("Amazon DynamoDB", False),
      ("Amazon Redshift", True),
      ("Amazon EMR", False)],
     "Amazon Redshift is a fully managed, petabyte-scale data warehouse service. It uses columnar storage, parallel query execution, and result caching to deliver fast query performance on large datasets.",
     "Redshift is AWS's petabyte-scale data warehouse for analytics.")

add_q(46, "Design High-Performing Architectures",
     "Which VPC feature allows you to improve network performance by bypassing intermediate network appliances for EC2 instances in the same subnet?",
     [("VPC Peering", False),
      ("Placement Groups - Cluster", True),
      ("Elastic Network Adapter (ENA)", False),
      ("VPC Flow Logs", False)],
     "Cluster placement groups pack instances close together in an AZ, achieving the highest possible network performance through low-latency, high-bandwidth connections. This is ideal for HPC and tightly-coupled application workloads.",
     "Cluster placement groups maximize network performance between instances.")

add_q(47, "Design High-Performing Architectures",
     "Which Amazon S3 storage class is optimized for long-lived data that is infrequently accessed but requires fast access when needed?",
     [("S3 Standard", False),
      ("S3 Standard-IA", True),
      ("S3 One Zone-IA", False),
      ("S3 Glacier Deep Archive", False)],
     "S3 Standard-IA is designed for data that is less frequently accessed but requires rapid access when needed. It offers the same high durability and throughput as S3 Standard but with a lower storage price and a per-GB retrieval fee.",
     "Standard-IA is for infrequently accessed data with fast retrieval.")

add_q(48, "Design High-Performing Architectures",
     "A company needs to process streaming data in real-time. Which AWS service should they use for real-time data processing?",
     [("Amazon Kinesis Data Streams", True),
      ("AWS Batch", False),
      ("Amazon SNS", False),
      ("Amazon SQS", False)],
     "Amazon Kinesis Data Streams allows you to build custom applications that process or analyze streaming data in real-time. It can continuously capture gigabytes of data per second from hundreds of thousands of sources.",
     "Kinesis Data Streams enables real-time processing of streaming data.")

add_q(49, "Design High-Performing Architectures",
     "Which compute option is best for running code in response to events without provisioning servers?",
     [("Amazon EC2", False),
      ("AWS Lambda", True),
      ("Amazon ECS", False),
      ("AWS Fargate", False)],
     "AWS Lambda is a serverless compute service that runs your code in response to events. It automatically scales from a few requests per day to thousands per second, and you only pay for the compute time you consume.",
     "Lambda runs code in response to events with automatic scaling and no server management.")

add_q(50, "Design High-Performing Architectures",
     "Which EBS volume type provides a balance of price and performance for general-purpose workloads?",
     [("EBS Cold HDD (sc1)", False),
      ("EBS Throughput Optimized HDD (st1)", False),
      ("EBS General Purpose SSD (gp3)", True),
      ("EBS Provisioned IOPS SSD (io2)", False)],
     "EBS gp3 volumes provide a balance of price and performance for a wide variety of workloads. They offer baseline performance of 3,000 IOPS and 125 MB/s throughput included in the price, with the ability to scale up.",
     "gp3 provides the best price-performance balance for general-purpose workloads.")

add_q(51, "Design High-Performing Architectures",
     "Which database is best suited for a graph data model such as social networking or recommendation engines?",
     [("Amazon RDS", False),
      ("Amazon DynamoDB", False),
      ("Amazon Neptune", True),
      ("Amazon DocumentDB", False)],
     "Amazon Neptune is a fully managed graph database service optimized for storing billions of relationships and querying the graph with milliseconds latency. It supports both Property Graph and RDF graph models.",
     "Neptune is AWS's managed graph database for relationship-heavy data models.")

add_q(52, "Design High-Performing Architectures",
     "A company needs to ingest large amounts of structured data into Redshift for analytics. Which AWS service is purpose-built for this data loading workflow?",
     [("AWS Direct Connect", False),
      ("AWS Glue", False),
      ("Amazon Kinesis Data Firehose", True),
      ("Amazon SQS", False)],
     "Kinesis Data Firehose is the easiest way to reliably load streaming data into data lakes, data stores, and analytics tools. It can capture, transform, and deliver streaming data to Redshift, S3, Elasticsearch, and more.",
     "Firehose loads streaming data into Redshift and other analytics destinations.")

add_q(53, "Design High-Performing Architectures",
     "Which AWS service uses AWS-managed edge locations to improve the availability and performance of global applications?",
     [("Amazon CloudFront", True),
      ("Amazon Route 53", False),
      ("AWS WAF", False),
      ("Amazon API Gateway", False)],
     "CloudFront uses a global network of edge locations to cache content and reduce latency. It integrates with other AWS services and can improve both availability and performance of web applications through intelligent routing and caching.",
     "CloudFront uses edge locations to reduce latency and improve performance globally.")

add_q(54, "Design High-Performing Architectures",
     "Which Amazon Aurora feature separates compute from storage, allowing you to scale each independently?",
     [("Aurora Serverless v2", True),
      ("Aurora Read Replicas", False),
      ("Aurora Multi-Master", False),
      ("Aurora Parallel Query", False)],
     "Aurora Serverless v2 automatically scales compute capacity up and down based on application demand. It instantaneously scales to hundreds of thousands of transactions and can scale down to zero when not in use.",
     "Aurora Serverless v2 scales compute and storage independently.")

add_q(55, "Design High-Performing Architectures",
     "A company wants to reduce the latency of EC2 instances connecting to a database. Which Elastic Network Adapter feature provides enhanced network performance?",
     [("Elastic Fabric Adapter (EFA)", True),
      ("Enhanced Networking", False),
      ("Elastic IP", False),
      ("Network Load Balancer", False)],
     "EFA enables an EC2 instance to bypass the OS kernel and communicate directly with AWS network hardware, providing lower and more consistent latency and higher throughput. It is designed for HPC and ML applications.",
     "EFA provides the lowest latency networking for HPC and ML workloads.")

add_q(56, "Design High-Performing Architectures",
     "Which caching pattern loads data into the cache only when it is requested by the application?",
     [("Write-through caching", False),
      ("Lazy loading", True),
      ("Cache aside", False),
      ("Write-behind caching", False)],
     "Lazy loading (also known as cache-aside) only loads data into the cache when it is first requested. If the data is not in the cache, the application reads from the database and populates the cache. This avoids filling the cache with unused data.",
     "Lazy loading loads data into cache only on first request.")

add_q(57, "Design High-Performing Architectures",
     "Which AWS service provides a managed, high-performance message broker that supports JMS, NMS, AMQP, and STOMP protocols?",
     [("Amazon SQS", False),
      ("Amazon SNS", False),
      ("Amazon MQ", True),
      ("Amazon Kinesis", False)],
     "Amazon MQ is a managed message broker service that supports Apache ActiveMQ and RabbitMQ. It provides compatibility with popular messaging protocols (JMS, AMQP, MQTT, STOMP) for migrating existing message broker workloads.",
     "Amazon MQ provides managed ActiveMQ/RabbitMQ with standard protocols.")

add_q(58, "Design High-Performing Architectures",
     "Which storage solution provides the fastest block storage performance for EC2 instances?",
     [("Amazon EBS Provisioned IOPS SSD (io2 Block Express)", True),
      ("Amazon EBS General Purpose SSD (gp3)", False),
      ("Amazon Instance Store NVMe", False),
      ("Amazon EFS", False)],
     "EBS io2 Block Express volumes are the highest performance EBS storage option, delivering up to 256,000 IOPS, 4,000 MB/s throughput, and 64 TiB storage per volume. They are designed for the most demanding workloads.",
     "io2 Block Express delivers the highest EBS performance with up to 256K IOPS.")

add_q(59, "Design High-Performing Architectures",
     "Which CloudFront feature allows you to serve different content based on the geographic location of the user?",
     [("Lambda@Edge", True),
      ("Origin Access Control", False),
      ("Signed URLs", False),
      ("Custom Error Pages", False)],
     "Lambda@Edge allows you to run Lambda functions at CloudFront edge locations, enabling you to customize content based on user location, device type, headers, or cookies without needing to modify the origin.",
     "Lambda@Edge runs custom code at the edge for personalized content delivery.")

add_q(60, "Design High-Performing Architectures",
     "A company needs to serve static content from S3 with the lowest possible latency to users in Asia. What is the BEST approach?",
     [("Use S3 Transfer Acceleration", False),
      ("Enable S3 Cross-Region Replication to an Asia bucket", False),
      ("Use Amazon CloudFront with an S3 origin and edge locations in Asia", True),
      ("Use AWS Global Accelerator", False)],
     "CloudFront with an S3 origin automatically caches content at edge locations closest to users. By serving from edge locations in Asia, users experience the lowest possible latency. CRR alone does not provide edge caching.",
     "CloudFront provides the lowest latency by caching at edge locations near users.")

# ============================================================
# Domain 3: Design Secure Architectures (30 questions)
# ============================================================
add_q(61, "Design Secure Architectures",
     "Which AWS service allows you to create and manage users, groups, roles, and permissions for AWS resources?",
     [("AWS Organizations", False),
      ("AWS IAM", True),
      ("AWS STS", False),
      ("AWS Cognito", False)],
     "AWS Identity and Access Management (IAM) enables you to securely manage access to AWS services and resources. With IAM, you can create and manage AWS users, groups, roles, and permissions to control access to your AWS resources.",
     "IAM manages identities and permissions for AWS resources.")

add_q(62, "Design Secure Architectures",
     "Which IAM policy type is attached to an IAM identity (user, group, or role) and defines what actions they can perform?",
     [("Resource-based policy", False),
      ("Identity-based policy", True),
      ("Permissions boundary", False),
      ("Service control policy (SCP)", False)],
     "Identity-based policies are attached to IAM identities (users, groups, or roles) and specify what actions the identity can perform on which resources, and under what conditions. They are JSON documents following the IAM policy language.",
     "Identity-based policies are attached to users, groups, or roles.")

add_q(63, "Design Secure Architectures",
     "What is the purpose of AWS Key Management Service (KMS) Customer Master Keys (CMKs)?",
     [("To manage EC2 instance metadata", False),
      ("To create and manage encryption keys for data protection", True),
      ("To manage SSL/TLS certificates", False),
      ("To control API rate limiting", False)],
     "AWS KMS allows you to create and manage cryptographic keys and control their use across AWS services and applications. CMKs are used to encrypt and decrypt data, and are integrated with many AWS services for encryption.",
     "KMS CMKs are used to create and manage encryption keys.")

add_q(64, "Design Secure Architectures",
     "What is the key difference between Security Groups and Network ACLs in a VPC?",
     [("Security Groups are stateless; NACLs are stateful", False),
      ("Security Groups are stateful; NACLs are stateless", True),
      ("Security Groups operate at the subnet level; NACLs operate at the instance level", False),
      ("NACLs support allow rules only; Security Groups support deny rules", False)],
     "Security Groups are stateful - if you allow inbound traffic, the response traffic is automatically allowed regardless of outbound rules. NACLs are stateless - both inbound and outbound rules must be explicitly configured.",
     "Security Groups are stateful; NACLs are stateless and operate at the subnet level.")

add_q(65, "Design Secure Architectures",
     "Which AWS service provides protection against SQL injection, cross-site scripting (XSS), and other web exploits?",
     [("AWS Shield", False),
      ("AWS WAF", True),
      ("AWS GuardDuty", False),
      ("AWS Inspector", False)],
     "AWS WAF (Web Application Firewall) helps protect web applications from common web exploits that could affect application availability, compromise security, or consume excessive resources. It includes managed rule groups for OWASP Top 10 vulnerabilities.",
     "WAF protects against common web exploits like SQL injection and XSS.")

add_q(66, "Design Secure Architectures",
     "Under the AWS Shared Responsibility Model, which of the following is AWS's responsibility?",
     [("Managing IAM user access policies", False),
      ("Encrypting data in transit using customer-provided certificates", False),
      ("Physical security of the data centers", True),
      ("Configuring Security Group rules", False)],
     "Under the Shared Responsibility Model, AWS is responsible for the security OF the cloud - physical security, hardware, networking, and managed service infrastructure. The customer is responsible for security IN the cloud - data, access management, and configuration.",
     "AWS is responsible for physical security; customers are responsible for data and configuration.")

add_q(67, "Design Secure Architectures",
     "Which IAM feature provides temporary, limited-privilege credentials that can be used to access AWS resources?",
     [("IAM Access Keys", False),
      ("AWS STS AssumeRole", True),
      ("IAM Password Policy", False),
      ("IAM Group", False)],
     "AWS Security Token Service (STS) AssumeRole returns a set of temporary security credentials consisting of an access key ID, a secret access key, and a security token. These credentials are valid for a limited duration and inherit the permissions of the assumed role.",
     "STS AssumeRole provides temporary credentials with role-based permissions.")

add_q(68, "Design Secure Architectures",
     "Which S3 feature allows you to grant temporary access to objects without making them publicly accessible?",
     [("S3 bucket policies", False),
      ("S3 presigned URLs", True),
      ("S3 Access Control Lists (ACLs)", False),
      ("S3 Versioning", False)],
     "S3 presigned URLs generate time-limited URLs that grant temporary access to specific S3 objects without making them publicly accessible. They work with both authenticated and anonymous requests and can include custom expiration times.",
     "Presigned URLs provide time-limited access to private S3 objects.")

add_q(69, "Design Secure Architectures",
     "Which AWS service should you use to automatically rotate database credentials and other secrets?",
     [("AWS Systems Manager Parameter Store", False),
      ("AWS Secrets Manager", True),
      ("AWS KMS", False),
      ("AWS Certificate Manager", False)],
     "AWS Secrets Manager helps you protect secrets needed to access applications, services, and IT resources. It enables you to easily rotate, manage, and retrieve database credentials, API keys, and other secrets throughout their lifecycle.",
     "Secrets Manager manages and automatically rotates secrets like database credentials.")

add_q(70, "Design Secure Architectures",
     "Which AWS service provides intelligent threat detection for your AWS account by continuously monitoring for malicious behavior?",
     [("Amazon Inspector", False),
      ("Amazon Macie", False),
     ("Amazon GuardDuty", True),
      ("AWS Config", False)],
     "Amazon GuardDuty is a threat detection service that continuously monitors for malicious activity and unauthorized behavior to protect your AWS accounts, workloads, and data stored in S3. It uses ML and threat intelligence feeds.",
     "GuardDuty provides intelligent threat detection for your AWS environment.")

add_q(71, "Design Secure Architectures",
     "A company wants to enforce MFA for all IAM users accessing the AWS Management Console. How can this be achieved?",
     [("Enable MFA at the account level using AWS Organizations", False),
      ("Create an IAM policy requiring MFA", True),
      ("Use AWS Shield to enforce MFA", False),
      ("Enable MFA in AWS Config rules", False)],
     "You can enforce MFA by creating an IAM policy with the aws:MultiFactorAuthAge condition key. This condition checks whether MFA was used when the request was authenticated and denies access if MFA was not used within a specified time period.",
     "Use an IAM policy with the aws:MultiFactorAuthAge condition to enforce MFA.")

add_q(72, "Design Secure Architectures",
     "Which type of KMS key can be used outside of the AWS account where it was created?",
     [("AWS managed CMK", False),
      ("Customer managed CMK with cross-account key policy", True),
      ("AWS owned CMK", False),
      ("Data key", False)],
     "Customer managed CMKs can be shared across AWS accounts by modifying the key policy to allow cross-account access. AWS managed CMKs and AWS owned CMKs cannot be used outside their account.",
     "Customer managed CMKs with cross-account policies enable key sharing.")

add_q(73, "Design Secure Architectures",
     "Which AWS Config feature allows you to define how your AWS resources should be configured and automatically check for compliance?",
     [("AWS Config Rules", True),
      ("AWS Config Aggregators", False),
      ("AWS Config Conformance Packs", False),
      ("AWS Config Recorders", False)],
     "AWS Config Rules evaluate the configuration of your AWS resources against desired settings. You can create custom rules or use managed rules to automatically check whether resources comply with your organization's policies.",
     "Config Rules evaluate resource configuration against desired settings.")

add_q(74, "Design Secure Architectures",
     "Which AWS service provides managed, automated vulnerability scanning for container images stored in Amazon ECR?",
     [("Amazon Inspector", True),
      ("Amazon GuardDuty", False),
      ("AWS WAF", False),
      ("Amazon Macie", False)],
     "Amazon Inspector is an automated vulnerability management service that continually scans AWS workloads for software vulnerabilities and unintended network exposure. It supports EC2 instances, container images in ECR, and Lambda functions.",
     "Inspector scans container images in ECR for vulnerabilities.")

add_q(75, "Design Secure Architectures",
     "Which parameter type in AWS Systems Manager Parameter Store provides additional security for sensitive data?",
     [("String type", False),
      ("StringList type", False),
      ("SecureString type", True),
      ("Encrypted type", False)],
     "SecureString parameters use AWS KMS to encrypt the parameter value. This is the recommended type for storing sensitive data like passwords, API keys, and database connection strings in Parameter Store.",
     "SecureString parameters are encrypted with KMS for sensitive data.")

add_q(76, "Design Secure Architectures",
     "Which AWS service provides DDoS protection with enhanced capabilities and access to the AWS DDoS Response Team?",
     [("AWS Shield Standard", False),
      ("AWS Shield Advanced", True),
      ("AWS WAF", False),
      ("AWS Firewall Manager", False)],
     "AWS Shield Advanced provides expanded DDoS protection beyond the free Shield Standard. It includes financial protection, 24/7 access to the DDoS Response Team (DRT), and integration with CloudFront, Route 53, ALB, and NLB.",
     "Shield Advanced provides enhanced DDoS protection and DDoS Response Team access.")

add_q(77, "Design Secure Architectures",
     "Which IAM best practice recommends using roles instead of long-term access keys for applications running on EC2?",
     [("Rotate access keys regularly", False),
      ("Use IAM roles for EC2 instances", True),
      ("Create individual IAM users", False),
      ("Use resource-based policies", False)],
     "IAM roles provide temporary credentials that are automatically rotated. Applications running on EC2 should use IAM roles (via instance profiles) rather than hardcoded or manually managed access keys. This eliminates the need to distribute and manage long-term credentials.",
     "IAM roles provide automatic temporary credentials for EC2 applications.")

add_q(78, "Design Secure Architectures",
     "Which AWS service centralizes security management across multiple AWS accounts?",
     [("AWS IAM", False),
      ("AWS Organizations", False),
      ("AWS Firewall Manager", True),
      ("AWS CloudTrail", False)],
     "AWS Firewall Manager centrally manages and configures AWS WAF, AWS Shield Advanced, and Amazon VPC security groups across all your accounts and resources in AWS Organizations. It simplifies security administration across multiple accounts.",
     "Firewall Manager centralizes security management across multiple accounts.")

add_q(79, "Design Secure Architectures",
     "What is the Principle of Least Privilege in the context of AWS IAM?",
     [("Grant users the maximum permissions they might need", False),
      ("Grant only the permissions necessary for a user or role to perform their tasks", True),
      ("Grant all users administrator access", False),
      ("Use root account for all operations", False)],
     "The Principle of Least Privilege means granting only the minimum permissions necessary for users and roles to perform their intended tasks. This reduces the risk of unauthorized access and limits the potential impact of compromised credentials.",
     "Least privilege means granting only the minimum required permissions.")

add_q(80, "Design Secure Architectures",
     "Which AWS service records API calls made in your AWS account for security auditing and compliance?",
     [("AWS Config", False),
      ("AWS CloudTrail", True),
      ("AWS X-Ray", False),
      ("Amazon VPC Flow Logs", False)],
     "AWS CloudTrail records API calls made on your account, including calls from the console, SDKs, CLI, and AWS services. It provides event history of your account activity, including actions taken through AWS services.",
     "CloudTrail records all API calls for security auditing and compliance.")

add_q(81, "Design Secure Architectures",
     "Which S3 bucket policy element allows you to restrict access based on the source IP address?",
     [("Condition", True),
      ("Action", False),
      ("Resource", False),
      ("Principal", False)],
     "The Condition element in a bucket policy allows you to specify additional constraints on the policy statement, such as restricting access based on source IP address, VPC endpoint, time of day, or other contextual factors.",
     "Condition elements enable access control based on context like IP address.")

add_q(82, "Design Secure Architectures",
     "Which service provides centralized management of firewall rules across multiple accounts using AWS Organizations?",
     [("AWS WAF", False),
      ("AWS Firewall Manager", True),
      ("AWS Shield", False),
      ("Amazon Inspector", False)],
     "AWS Firewall Manager works in conjunction with AWS Organizations to centrally configure and manage firewall rules across all accounts. It simplifies administration of WAF rules, security groups, and Shield Advanced protections.",
     "Firewall Manager centrally manages firewall rules across Organizations.")

add_q(83, "Design Secure Architectures",
     "Which encryption method does Amazon S3 use by default when you upload an object?",
     [("Server-side encryption with S3-managed keys (SSE-S3)", True),
      ("Server-side encryption with KMS keys (SSE-KMS)", False),
      ("Server-side encryption with customer-provided keys (SSE-C)", False),
      ("Client-side encryption", False)],
     "S3 applies server-side encryption by default using S3-managed keys (SSE-S3) for every object uploaded. This basic encryption is applied automatically at no additional cost and uses AES-256 encryption.",
     "S3 uses SSE-S3 encryption by default for all new objects.")

add_q(84, "Design Secure Architectures",
     "Which IAM feature limits the maximum permissions an IAM entity can have?",
     [("IAM policy", False),
      ("IAM permissions boundary", True),
      ("IAM role", False),
      ("IAM group", False)],
     "IAM permissions boundaries are advanced policy features that set the maximum permissions that an identity-based policy can grant to an IAM entity. They are used to delegate administrative control while maintaining guardrails.",
     "Permissions boundaries define the maximum permissions an entity can have.")

add_q(85, "Design Secure Architectures",
     "Which VPC component acts as a firewall at the subnet level to control inbound and outbound traffic?",
     [("Security Group", False),
      ("Network ACL", True),
      ("Internet Gateway", False),
      ("NAT Gateway", False)],
     "Network ACLs (NACLs) operate at the subnet level and provide a layer of security that acts as a firewall for controlling traffic in and out of a subnet. They are stateless and support both allow and deny rules.",
     "NACLs are stateless subnet-level firewalls with allow and deny rules.")

add_q(86, "Design Secure Architectures",
     "Which AWS service helps protect sensitive data stored in S3 by discovering and classifying sensitive data using ML?",
     [("Amazon Inspector", False),
      ("Amazon GuardDuty", False),
      ("Amazon Macie", True),
      ("AWS Config", False)],
     "Amazon Macie uses machine learning and pattern matching to discover and protect sensitive data such as personally identifiable information (PII) in S3. It automatically classifies data and provides dashboards for visibility.",
     "Macie uses ML to discover and classify sensitive data in S3.")

add_q(87, "Design Secure Architectures",
     "Which security practice ensures that EC2 instances in a private subnet can access the internet without being directly accessible from the internet?",
     [("Internet Gateway", False),
      ("NAT Gateway", True),
      ("VPC Peering", False),
      ("VPN Gateway", False)],
     "A NAT Gateway enables instances in private subnets to connect to services outside your VPC (including the internet) while preventing external connections from initiating connections to those instances. It performs source/destination network address translation.",
     "NAT Gateway allows outbound internet access from private subnets.")

add_q(88, "Design Secure Architectures",
     "Which AWS service provides managed, automated security assessments for applications running on EC2?",
     [("Amazon Inspector", True),
      ("Amazon GuardDuty", False),
      ("AWS WAF", False),
      ("Amazon Macie", False)],
     "Amazon Inspector automatically assesses applications for exposure, vulnerabilities, and deviations from best practices. It performs network assessments to check for unintended network accessibility and EC2 instance assessments for vulnerabilities.",
     "Inspector provides automated security assessments for EC2 applications.")

add_q(89, "Design Secure Architectures",
     "Which type of S3 endpoint provides private connectivity between VPC resources and S3 without requiring a NAT gateway or internet gateway?",
     [("Internet Gateway", False),
      ("S3 VPC Endpoint (Gateway Endpoint)", True),
      ("S3 VPC Endpoint (Interface Endpoint)", False),
      ("AWS Direct Connect", False)],
     "S3 Gateway Endpoints are VPC endpoints powered by AWS PrivateLink that provide private connectivity between VPC resources and S3. Traffic between the VPC and S3 does not leave the Amazon network, and no NAT gateway or internet gateway is needed.",
     "S3 Gateway Endpoints provide private connectivity without NAT or internet gateway.")

add_q(90, "Design Secure Architectures",
     "Which AWS feature allows you to require all new S3 buckets to use default encryption with a specific KMS key?",
     [("S3 bucket policy", False),
      ("S3 Bucket Keys", False),
      ("Amazon Macie", False),
      ("AWS Organizations Service Control Policy", False)],
     "You can use an S3 bucket policy with the s3:ServerSideEncryption condition to require specific encryption settings for objects uploaded to the bucket. Additionally, you can use AWS Organizations SCPs to enforce encryption requirements across all accounts.",
     "Bucket policies with conditions or SCPs enforce encryption requirements on S3.")

# ============================================================
# Domain 4: Design Cost-Optimized Architectures (30 questions)
# ============================================================
add_q(91, "Design Cost-Optimized Architectures",
     "Which AWS pricing model provides the highest discount (up to 72%) for EC2 instances with a 1-year commitment?",
     [("On-Demand Instances", False),
      ("Reserved Instances", True),
      ("Spot Instances", False),
      ("Savings Plans", False)],
     "Reserved Instances provide up to 72% discount compared to On-Demand pricing with a 1-year or 3-year commitment. They are ideal for steady-state workloads with predictable usage patterns.",
     "Reserved Instances offer up to 72% off with a commitment.")

add_q(92, "Design Cost-Optimized Architectures",
     "Which pricing option allows you to bid on unused EC2 capacity at up to 90% discount?",
     [("On-Demand Instances", False),
      ("Reserved Instances", False),
      ("Spot Instances", True),
      ("Dedicated Instances", False)],
     "Amazon EC2 Spot Instances allow you to bid on unused EC2 capacity at steep discounts (up to 90% off On-Demand). Instances can be interrupted with short notice, making them ideal for fault-tolerant, flexible workloads.",
     "Spot Instances offer up to 90% discount for fault-tolerant workloads.")

add_q(93, "Design Cost-Optimized Architectures",
     "Which AWS pricing model offers a flexible discount model that applies across EC2, Fargate, and Lambda?",
     [("Reserved Instances", False),
      ("Savings Plans", True),
      ("Spot Instances", False),
      ("Dedicated Hosts", False)],
     "Savings Plans offer significant savings (up to 72%) on AWS compute usage with a flexible commitment. They apply across EC2, Fargate, and Lambda, providing more flexibility than Reserved Instances which are specific to instance types and regions.",
     "Savings Plans provide flexible compute discounts across EC2, Fargate, and Lambda.")

add_q(94, "Design Cost-Optimized Architectures",
     "Which S3 storage class automatically moves objects between storage tiers based on access patterns to optimize costs?",
     [("S3 Standard", False),
      ("S3 Intelligent-Tiering", True),
      ("S3 Standard-IA", False),
      ("S3 One Zone-IA", False)],
     "S3 Intelligent-Tiering is the only storage class that automatically moves objects between access tiers (frequent, infrequent, and archive instant access) based on changing access patterns. It optimizes costs by moving objects that are rarely accessed to cheaper tiers.",
     "Intelligent-Tiering automatically moves objects to cheaper tiers based on access.")

add_q(95, "Design Cost-Optimized Architectures",
     "Which AWS tool helps you visualize, understand, and manage your AWS costs and usage over time?",
     [("AWS CloudWatch", False),
      ("AWS Cost Explorer", True),
      ("AWS Trusted Advisor", False),
      ("AWS Budgets", False)],
     "AWS Cost Explorer allows you to analyze your cost and usage data using an interactive interface. You can view data up to the last 12 months, forecast costs, and identify areas for optimization.",
     "Cost Explorer visualizes and analyzes AWS costs and usage over time.")

add_q(96, "Design Cost-Optimized Architectures",
     "Which AWS service provides alerts when your costs exceed predefined thresholds?",
     [("AWS Cost Explorer", False),
      ("AWS Budgets", True),
      ("AWS Trusted Advisor", False),
      ("Amazon CloudWatch Alarms", False)],
     "AWS Budgets allows you to set custom cost and usage budgets and receive alerts when your actual costs or usage exceed (or are forecasted to exceed) your budgeted amounts. You can also take automated actions when thresholds are exceeded.",
     "AWS Budgets sends alerts when costs exceed predefined thresholds.")

add_q(97, "Design Cost-Optimized Architectures",
     "Which S3 feature automatically transitions objects to cheaper storage classes after a defined time period?",
     [("S3 Versioning", False),
      ("S3 Lifecycle Policies", True),
      ("S3 Object Lock", False),
      ("S3 Replication", False)],
     "S3 Lifecycle policies allow you to define rules that automatically transition objects to cheaper storage classes (like Standard-IA, Glacier, or Glacier Deep Archive) after a specified number of days. This optimizes storage costs without manual intervention.",
     "Lifecycle policies automatically transition objects to cheaper storage tiers.")

add_q(98, "Design Cost-Optimized Architectures",
     "Which AWS service provides recommendations to help you right-size your EC2 instances and optimize costs?",
     [("AWS Cost Explorer", False),
      ("AWS Trusted Advisor", True),
      ("AWS Config", False),
      ("AWS CloudTrail", False)],
     "AWS Trusted Advisor provides real-time guidance to help you provision your resources following AWS best practices. It includes cost optimization checks such as identifying idle EC2 instances, unattached EBS volumes, and right-sizing recommendations.",
     "Trusted Advisor provides right-sizing and cost optimization recommendations.")

add_q(99, "Design Cost-Optimized Architectures",
     "A company has a batch processing workload that runs for 4 hours every night. Which EC2 pricing model is MOST cost-effective?",
     [("On-Demand Instances", False),
      ("Reserved Instances", False),
      ("Spot Instances", True),
      ("Dedicated Hosts", False)],
     "Spot Instances are ideal for batch processing workloads because they can tolerate interruptions. If a Spot Instance is interrupted, the job can be restarted on another instance. The steep discount (up to 90%) makes them very cost-effective.",
     "Spot Instances are ideal for batch processing with steep discounts.")

add_q(100, "Design Cost-Optimized Architectures",
     "Which S3 storage class offers the lowest storage cost for data that is rarely accessed and can tolerate retrieval times of 12-48 hours?",
     [("S3 Standard-IA", False),
      ("S3 Glacier Instant Retrieval", False),
      ("S3 Glacier Flexible Retrieval", False),
      ("S3 Glacier Deep Archive", True)],
     "S3 Glacier Deep Archive is the lowest-cost storage class in AWS, designed for data that is rarely accessed and can tolerate retrieval times of 12-48 hours. It costs roughly 1/4 the price of S3 Glacier Flexible Retrieval.",
     "Deep Archive offers the lowest storage cost with 12-48 hour retrieval time.")

add_q(101, "Design Cost-Optimized Architectures",
     "What is right-sizing in the context of AWS cost optimization?",
     [("Moving to a larger instance type for better performance", False),
      ("Analyzing resource utilization and downsizing to the most appropriate instance type", True),
      ("Using only On-Demand instances", False),
      ("Deploying instances across multiple Regions", False)],
     "Right-sizing involves analyzing actual resource utilization metrics (CPU, memory, network) and selecting the most cost-effective instance type that meets your workload requirements. This prevents paying for unused capacity.",
     "Right-sizing matches instance capacity to actual workload needs.")

add_q(102, "Design Cost-Optimized Architectures",
     "Which Savings Plans type offers discounts based on a commitment to spend a specific dollar amount per hour on compute usage?",
     [("EC2 Instance Savings Plans", False),
      ("Compute Savings Plans", True),
      ("Reserved Instance Savings Plans", False),
      ("No Savings Plans type offers this", False)],
     "Compute Savings Plans offer the most flexible discount by committing to a dollar amount per hour of compute usage. They apply across EC2, Fargate, and Lambda, and can be shared across instance families, regions, and OS types.",
     "Compute Savings Plans commit to a dollar amount per hour across all compute services.")

add_q(103, "Design Cost-Optimized Architectures",
     "Which Trusted Advisor check identifies EBS volumes that have low utilization and could be deleted to save costs?",
     [("Low Utilization Amazon EC2 Instances", False),
      ("Unassociated Elastic IP Addresses", False),
      ("Underutilized Amazon EBS Volumes", True),
      ("Amazon RDS Idle DB Instances", False)],
     "The Underutilized Amazon EBS Volumes check identifies provisioned EBS volumes with very low write I/O activity over the past 7 days. These volumes may be candidates for deletion or downgrading to save costs.",
     "Trusted Advisor identifies underutilized EBS volumes for potential deletion.")

add_q(104, "Design Cost-Optimized Architectures",
     "A company wants to optimize costs for their AWS account and automatically implement cost-saving recommendations. Which service provides this capability?",
     [("AWS Cost Explorer", False),
      ("AWS Trusted Advisor", False),
      ("AWS Compute Optimizer", True),
      ("AWS Budgets", False)],
     "AWS Compute Optimizer recommends optimal AWS resources for your workloads using machine learning to analyze historical utilization metrics. It provides right-sizing recommendations for EC2, ECS, Lambda, and EBS volumes.",
     "Compute Optimizer uses ML to recommend optimal resource configurations.")

add_q(105, "Design Cost-Optimized Architectures",
     "Which AWS feature allows you to consolidate billing across multiple AWS accounts to get volume discounts?",
     [("AWS Organizations Consolidated Billing", True),
      ("AWS Cost Explorer", False),
      ("AWS Budgets", False),
      ("AWS Marketplace", False)],
     "AWS Organizations Consolidated Billing allows you to combine usage across all accounts in your organization to receive volume discounts for Reserved Instances and Savings Plans. The combined usage may qualify for lower pricing tiers.",
     "Consolidated Billing combines usage across accounts for volume discounts.")

add_q(106, "Design Cost-Optimized Architectures",
     "Which pricing model charges based on the actual compute time consumed with no upfront commitment?",
     [("Reserved Instances", False),
      ("Spot Instances", False),
      ("AWS Lambda Pay-as-you-go", True),
      ("Savings Plans", False)],
     "AWS Lambda charges based on the number of requests and the duration of code execution. There are no upfront commitments or minimum fees. You pay only for the compute time you consume, measured in milliseconds.",
     "Lambda charges only for actual compute time consumed, with no upfront commitment.")

add_q(107, "Design Cost-Optimized Architectures",
     "Which S3 feature reduces the cost of Server-Side Encryption with KMS (SSE-KMS) when uploading many objects?",
     [("S3 Bucket Keys", True),
      ("S3 Lifecycle Policies", False),
      ("S3 Object Lock", False),
      ("S3 Versioning", False)],
     "S3 Bucket Keys reduce the cost of SSE-KMS by decreasing the number of AWS KMS API requests when uploading objects. A bucket key is used at the bucket level to reduce KMS request costs from thousands to just a few per operation.",
     "S3 Bucket Keys reduce KMS API costs for SSE-KMS encrypted uploads.")

add_q(108, "Design Cost-Optimized Architectures",
     "Which AWS tool allows you to generate cost forecasts based on historical usage patterns?",
     [("AWS Budgets", False),
      ("AWS Cost Explorer Forecasting", True),
      ("AWS Trusted Advisor", False),
      ("AWS Compute Optimizer", False)],
     "AWS Cost Explorer includes a forecasting feature that uses machine learning to predict your future AWS costs based on historical usage patterns. You can forecast costs up to 12 months ahead, filtered by service, account, or region.",
     "Cost Explorer provides ML-based cost forecasting up to 12 months ahead.")

add_q(109, "Design Cost-Optimized Architectures",
     "Which option is MOST cost-effective for running a relational database with consistent, predictable workloads?",
     [("Amazon RDS with Reserved Instances", True),
      ("Amazon RDS with On-Demand instances", False),
      ("Amazon DynamoDB On-Demand", False),
      ("Self-managed database on EC2", False)],
     "Using Amazon RDS with Reserved Instances provides the most cost-effective option for predictable database workloads. You save up to 40% compared to On-Demand pricing by committing to a 1 or 3-year term for the database instance.",
     "RDS with Reserved Instances is most cost-effective for predictable workloads.")

add_q(110, "Design Cost-Optimized Architectures",
     "Which AWS pricing feature allows you to pay a lower rate the more you use a service?",
     [("Spot pricing", False),
      ("Volume-based tiered pricing", True),
      ("Savings Plans", False),
      ("Reserved Instances", False)],
     "AWS offers volume-based tiered pricing for many services, meaning the per-unit price decreases as usage increases. This is common for services like S3, data transfer, and Lambda, where higher usage automatically qualifies for lower rates.",
     "Tiered pricing reduces per-unit costs as usage increases.")

add_q(111, "Design Cost-Optimized Architectures",
     "Which AWS service helps identify idle or underutilized resources across your AWS account?",
     [("AWS CloudWatch", False),
      ("AWS Trusted Advisor", True),
      ("Amazon Inspector", False),
      ("AWS X-Ray", False)],
     "AWS Trusted Advisor provides cost optimization checks that identify idle or underutilized resources including low-utilization EC2 instances, unattached EBS volumes, unassociated Elastic IPs, and idle RDS instances.",
     "Trusted Advisor identifies idle and underutilized resources for cost savings.")

add_q(112, "Design Cost-Optimized Architectures",
     "A company needs to run a containerized application with variable traffic. Which option is MOST cost-effective?",
     [("EC2 instances with Reserved Instances", False),
      ("Amazon ECS on EC2 with Savings Plans", False),
      ("AWS Fargate with per-second billing", True),
      ("Amazon EC2 Spot Instances for containers", False)],
     "Fargate provides per-second billing with no upfront cost, automatically scaling based on application demand. For variable traffic, you only pay for the compute resources actually consumed, making it more cost-effective than provisioned EC2.",
     "Fargate with per-second billing is cost-effective for variable container workloads.")

add_q(113, "Design Cost-Optimized Architectures",
     "Which AWS Budgets feature allows you to automatically take action when costs exceed a threshold?",
     [("AWS Lambda integration", True),
      ("SNS notifications only", False),
      ("CloudWatch Events", False),
      ("Auto Scaling", False)],
     "AWS Budgets Actions allow you to define automated actions that execute when your costs exceed (or are forecasted to exceed) your budget. Actions can include applying an IAM policy, sending a message, or executing a Lambda function.",
     "Budgets Actions automate responses when costs exceed thresholds.")

add_q(114, "Design Cost-Optimized Architectures",
     "Which S3 storage class is designed for data that is stored for long periods and accessed less than once per quarter?",
     [("S3 Standard", False),
      ("S3 Standard-IA", False),
      ("S3 One Zone-IA", False),
      ("S3 Glacier Flexible Retrieval", True)],
     "S3 Glacier Flexible Retrieval is designed for long-term archival data accessed less than once per quarter. It provides fast retrieval options (expedited, standard, bulk) with storage costs significantly lower than Standard-IA.",
     "Glacier Flexible Retrieval is for long-term archival data with infrequent access.")

add_q(115, "Design Cost-Optimized Architectures",
     "Which feature of EC2 Auto Scaling helps optimize costs by automatically terminating instances during low-demand periods?",
     [("Target Tracking Policy", False),
      ("Scheduled Scaling", True),
      ("Step Scaling", False),
      ("Simple Scaling", False)],
     "Scheduled Scaling allows you to scale your Auto Scaling group based on a schedule. You can reduce the minimum and desired capacity during off-peak hours to minimize costs, and increase it during expected peak periods.",
     "Scheduled Scaling adjusts capacity based on predictable demand patterns to save costs.")

add_q(116, "Design Cost-Optimized Architectures",
     "Which pricing model provides a discounted hourly rate in exchange for a commitment to use a specific EC2 instance type in a specific region?",
     [("Spot Instances", False),
      ("Savings Plans", False),
      ("Standard Reserved Instances", True),
      ("Dedicated Instances", False)],
     "Standard Reserved Instances provide a significant discount (up to 72%) in exchange for a commitment to use a specific instance type in a specific region for a 1 or 3-year term. They are ideal for steady-state, predictable workloads.",
     "Standard Reserved Instances discount specific instance types in specific regions.")

add_q(117, "Design Cost-Optimized Architectures",
     "Which AWS tool provides a monthly report summarizing your AWS usage and costs?",
     [("AWS Cost Explorer", False),
      ("AWS Cost and Usage Report", True),
      ("AWS Budgets", False),
      ("AWS Trusted Advisor", False)],
     "The AWS Cost and Usage Report contains the most comprehensive set of cost and usage data available. It can be delivered to an S3 bucket at hourly or daily granularity, enabling detailed analysis and custom reporting.",
     "Cost and Usage Report provides the most comprehensive cost data available.")

add_q(118, "Design Cost-Optimized Architectures",
     "Which type of Reserved Instance allows you to change the instance type, operating system, or tenancy after purchase?",
     [("Standard Reserved Instances", False),
      ("Convertible Reserved Instances", True),
      ("Scheduled Reserved Instances", False),
      ("Dedicated Reserved Instances", False)],
     "Convertible Reserved Instances offer a lower discount (up to 54%) but provide the flexibility to change instance family, OS, tenancy, or payment option. This is useful when workload requirements may change over the commitment period.",
     "Convertible Reserved Instances allow flexibility to change instance attributes.")

add_q(119, "Design Cost-Optimized Architectures",
     "Which service provides recommendations to optimize the cost of your AWS environment based on best practices?",
     [("AWS CloudWatch", False),
      ("AWS Trusted Advisor", True),
      ("AWS Systems Manager", False),
      ("AWS CloudFormation", False)],
     "AWS Trusted Advisor checks for cost optimization opportunities including underutilized resources, idle resources, and right-sizing recommendations. It provides actionable advice to reduce costs while maintaining performance.",
     "Trusted Advisor provides cost optimization recommendations based on best practices.")

add_q(120, "Design Cost-Optimized Architectures",
     "A company is spending too much on data transfer between Availability Zones. Which architecture change could reduce these costs?",
     [("Use AWS Direct Connect instead of VPC peering", False),
      ("Ensure resources in the same VPC communicate within the same AZ when possible", True),
      ("Use S3 Transfer Acceleration for all transfers", False),
      ("Migrate to AWS Snowball", False)],
     "Data transfer between AZs incurs charges. By co-locating resources that communicate frequently within the same AZ, you can reduce or eliminate inter-AZ data transfer costs. This is a common cost optimization strategy.",
     "Co-locating communicating resources in the same AZ reduces inter-AZ data transfer costs.")

# ============================================================
# EC2 & Compute (30 questions)
# ============================================================
add_q(121, "EC2 & Compute",
     "Which EC2 instance type family provides the best price-performance for general-purpose workloads?",
     [("T family (Burstable Performance)", False),
      ("C family (Compute Optimized)", False),
      ("M family (General Purpose)", True),
      ("R family (Memory Optimized)", False)],
     "M family instances (like m6i) provide a balance of compute, memory, and networking resources, making them ideal for general-purpose workloads such as web servers, application servers, and small databases.",
     "M family is the best general-purpose EC2 instance type.")

add_q(122, "EC2 & Compute",
     "Which T-family feature allows instances to burst above their baseline CPU performance when needed?",
     [("Unlimited mode", True),
      ("Dedicated tenancy", False),
      ("Placement groups", False),
      ("Enhanced networking", False)],
     "T3/T3a instances use CPU credits to burst above their baseline performance. When the instance uses fewer CPU credits than it earns, surplus credits are stored. In Unlimited mode, instances can burst beyond the credit balance at On-Demand rates.",
     "T-family instances use CPU credits to burst above baseline performance.")

add_q(123, "EC2 & Compute",
     "What is the maximum execution time for an AWS Lambda function?",
     [("1 minute", False),
      ("5 minutes", False),
      ("15 minutes", True),
      ("1 hour", False)],
     "Lambda has a maximum execution timeout of 15 minutes. This is important when designing architectures - long-running processes should use Step Functions or other services to coordinate work beyond this limit.",
     "Lambda has a 15-minute maximum execution time.")

add_q(124, "EC2 & Compute",
     "Which service provides automatic scaling for EC2 instances based on demand?",
     [("AWS Elastic Beanstalk", False),
      ("Amazon EC2 Auto Scaling", True),
      ("AWS Lambda", False),
      ("AWS Systems Manager", False)],
     "EC2 Auto Scaling automatically adjusts the number of EC2 instances based on demand. You can use scaling policies (target tracking, step scaling, or scheduled) to maintain application availability and optimize costs.",
     "EC2 Auto Scaling automatically adjusts instance count based on demand.")

add_q(125, "EC2 & Compute",
     "Which type of AMI is provided by AWS and contains common software stacks?",
     [("Community AMI", False),
      ("Marketplace AMI", False),
      ("AWS managed AMI", False),
      ("Quick Start AMI", True)],
     "AWS Quick Start AMIs (often referred to as Amazon AMIs or AWS-managed AMIs) come pre-configured with common software like operating systems and are maintained by AWS. They are a good starting point for new instances.",
     "AWS provides pre-configured AMIs with common software stacks.")

add_q(126, "EC2 & Compute",
     "Which AWS service allows you to deploy containers without managing the underlying EC2 instances?",
     [("Amazon EKS with EC2 nodes", False),
      ("Amazon ECS with EC2 launch type", False),
      ("Amazon ECS with Fargate launch type", True),
      ("Amazon Lightsail", False)],
     "ECS Fargate launch type runs containers without requiring you to manage the underlying EC2 instances. You specify the task requirements (CPU, memory), and Fargate handles the server provisioning and scaling.",
     "Fargate launch type runs containers without managing EC2 instances.")

add_q(127, "EC2 & Compute",
     "Which EC2 purchasing option provides dedicated hardware that meets regulatory compliance requirements?",
     [("On-Demand Instances", False),
      ("Spot Instances", False),
      ("Dedicated Instances", True),
      ("Reserved Instances", False)],
     "Dedicated Instances run on hardware that is dedicated to a single customer. They provide physical isolation from other AWS accounts and are suitable for workloads with regulatory or compliance requirements for dedicated hardware.",
     "Dedicated Instances provide physical hardware isolation for compliance.")

add_q(128, "EC2 & Compute",
     "Which AWS service enables you to orchestrate multiple Lambda functions into a serverless workflow?",
     [("Amazon API Gateway", False),
      ("AWS Step Functions", True),
      ("Amazon SQS", False),
      ("AWS Lambda Layers", False)],
     "AWS Step Functions is a serverless orchestration service that lets you coordinate multiple AWS services into serverless workflows. You can build complex, multi-step Lambda workflows with error handling and retry logic.",
     "Step Functions orchestrates multiple Lambda functions into serverless workflows.")

add_q(129, "EC2 & Compute",
     "Which EC2 feature improves network performance by providing enhanced networking capabilities?",
     [("Elastic Network Interface (ENI)", False),
      ("Elastic Fabric Adapter (EFA)", True),
      ("Placement Groups", False),
      ("Auto Scaling", False)],
     "Elastic Fabric Adapter (EFA) provides enhanced networking capabilities for HPC applications. It enables applications to bypass the OS kernel and communicate directly with network hardware for lower latency and higher throughput.",
     "EFA provides enhanced networking for HPC workloads.")

add_q(130, "EC2 & Compute",
     "Which AWS service provides a managed Kubernetes environment?",
     [("Amazon ECS", False),
      ("Amazon EKS", True),
      ("AWS Fargate", False),
      ("AWS App Runner", False)],
     "Amazon EKS (Elastic Kubernetes Service) provides a managed Kubernetes control plane. AWS manages the Kubernetes masters and etcd cluster, while you manage the worker nodes (or use Fargate for serverless compute).",
     "EKS is AWS's managed Kubernetes service.")

add_q(131, "EC2 & Compute",
     "What happens when a Spot Instance is terminated by AWS?",
     [("The instance is stopped and you are charged until you terminate it", False),
      ("The instance is terminated and you receive a 2-minute warning", True),
      ("The instance continues running at On-Demand rates", False),
      ("The instance is migrated to another Availability Zone", False)],
     "When AWS needs to reclaim Spot capacity, it issues a 2-minute warning via the Instance Metadata Service. The instance is then terminated. Your application should handle Spot interruptions gracefully.",
     "Spot Instances receive a 2-minute warning before termination.")

add_q(132, "EC2 & Compute",
     "Which AWS service simplifies the process of deploying code to EC2 instances?",
     [("AWS CodeDeploy", True),
      ("AWS CodePipeline", False),
      ("AWS CodeCommit", False),
      ("AWS CodeBuild", False)],
     "AWS CodeDeploy automates code deployments to EC2 instances, on-premises instances, Lambda functions, and ECS services. It handles the deployment process including rolling updates, traffic shifting, and rollback.",
     "CodeDeploy automates code deployments to EC2 instances.")

add_q(133, "EC2 & Compute",
     "Which EC2 placement group strategy places instances in different hardware to reduce correlated failures?",
     [("Cluster", False),
      ("Spread", True),
      ("Partition", False),
      ("Default", False)],
     "Spread placement groups place each instance on a distinct hardware rack, reducing correlated failures. They are ideal for critical applications where a small number of instances need high isolation from each other.",
     "Spread placement groups isolate instances on different hardware racks.")

add_q(134, "EC2 & Compute",
     "Which AWS service provides a serverless application deployment platform for web applications?",
     [("AWS Elastic Beanstalk", False),
      ("AWS Amplify", True),
      ("AWS AppSync", False),
      ("AWS SAM", False)],
     "AWS Amplify provides a complete set of tools and services for building full-stack web and mobile applications, including hosting, CI/CD, authentication, APIs, and analytics. It simplifies frontend deployment.",
     "Amplify is a full-stack serverless application deployment platform.")

add_q(135, "EC2 & Compute",
     "Which Lambda feature allows you to share common code and dependencies across multiple functions?",
     [("Lambda Layers", True),
      ("Lambda Aliases", False),
      ("Lambda Versions", False),
      ("Lambda Destinations", False)],
     "Lambda Layers let you manage shared code and dependencies (like SDKs, libraries, and custom runtimes) in a separate layer that can be used by multiple Lambda functions. This reduces deployment package size and simplifies updates.",
     "Lambda Layers share common code across multiple functions.")

add_q(136, "EC2 & Compute",
     "Which AWS service provides a managed service for running Apache Kafka?",
     [("Amazon Kinesis", False),
      ("Amazon MSK (Managed Streaming for Apache Kafka)", True),
      ("Amazon SQS", False),
      ("Amazon SNS", False)],
     "Amazon MSK is a fully managed service for Apache Kafka that makes it easy to build and run applications that use Kafka to process streaming data. AWS handles the infrastructure provisioning, configuration, and maintenance.",
     "MSK is AWS's managed Apache Kafka service.")

add_q(137, "EC2 & Compute",
     "Which EC2 feature allows you to launch instances with a specific IAM role attached?",
     [("IAM policies", False),
      ("Instance profiles", True),
      ("IAM groups", False),
      ("Resource tags", False)],
     "An instance profile is a container for an IAM role that you can use to pass role information to an EC2 instance when the instance starts. Applications on the instance can then use the role's temporary credentials.",
     "Instance profiles attach IAM roles to EC2 instances.")

add_q(138, "EC2 & Compute",
     "Which service provides automatic scaling for ECS tasks based on CloudWatch metrics?",
     [("EC2 Auto Scaling", False),
      ("Application Auto Scaling", True),
      ("Target Tracking Policy", False),
      ("Lambda Concurrency", False)],
     "Application Auto Scaling automatically adjusts the number of ECS tasks, DynamoDB capacity, and other scalable resources. For ECS, it can scale task count based on CPU utilization, memory utilization, or custom CloudWatch metrics.",
     "Application Auto Scaling scales ECS tasks based on CloudWatch metrics.")

add_q(139, "EC2 & Compute",
     "Which AWS Batch feature is useful for managing compute resources for batch processing workloads?",
     [("Job queues and compute environments", True),
      ("Continuous deployment", False),
      ("Real-time streaming", False),
      ("Serverless execution", False)],
     "AWS Batch uses job queues to prioritize and schedule jobs, and compute environments to manage the EC2 or Fargate resources that execute them. This managed service handles the provisioning and scaling of compute resources for batch workloads.",
     "AWS Batch manages job queues and compute environments for batch processing.")

add_q(140, "EC2 & Compute",
     "Which launch type for ECS allows you to specify CPU and memory requirements without managing instances?",
     [("EC2 launch type", False),
      ("Fargate launch type", True),
      ("External launch type", False),
      ("Default launch type", False)],
     "Fargate launch type allows you to run ECS tasks without managing the underlying EC2 instances. You simply specify the CPU and memory requirements for each task or service, and Fargate handles the rest.",
     "Fargate launch type abstracts away instance management for ECS.")

add_q(141, "EC2 & Compute",
     "Which AWS service provides a fully managed web application hosting platform with CI/CD built in?",
     [("Amazon Lightsail", False),
      ("AWS Elastic Beanstalk", True),
      ("AWS Amplify", False),
      ("AWS App Runner", False)],
     "Elastic Beanstalk is a PaaS service that automatically handles deployment, capacity provisioning, load balancing, auto scaling, and application health monitoring. It supports multiple programming languages and frameworks.",
     "Elastic Beanstalk is a fully managed PaaS with auto-scaling and CI/CD.")

add_q(142, "EC2 & Compute",
     "Which placement group strategy divides instances into partitions (groups of racks) to reduce the impact of hardware failures?",
     [("Cluster", False),
      ("Spread", False),
      ("Partition", True),
      ("None", False)],
     "Partition placement groups divide instances into logical partitions (groups of racks within an AZ). Each partition has its own set of racks, reducing the blast radius of hardware failures. This is ideal for large distributed systems like Hadoop and Cassandra.",
     "Partition placement groups reduce the blast radius of hardware failures.")

add_q(143, "EC2 & Compute",
     "Which AWS service automatically provisions and scales serverless containers for web applications?",
     [("AWS Fargate", False),
      ("AWS App Runner", True),
      ("AWS Lambda", False),
      ("Amazon ECS", False)],
     "AWS App Runner is a fully managed service that makes it easy to deploy web applications and APIs from source code or a container image. It automatically builds, deploys, and scales the application without requiring infrastructure management.",
     "App Runner automatically deploys and scales containerized web applications.")

add_q(144, "EC2 & Compute",
     "Which tool helps you package and deploy Lambda functions using infrastructure-as-code?",
     [("AWS CloudFormation", False),
      ("AWS SAM (Serverless Application Model)", True),
      ("AWS CDK", False),
      ("Terraform", False)],
     "AWS SAM is an open-source framework for building serverless applications. It extends CloudFormation with simplified syntax for defining Lambda functions, APIs, DynamoDB tables, and other serverless resources.",
     "SAM simplifies serverless application packaging and deployment.")

add_q(145, "EC2 & Compute",
     "Which feature of Lambda allows you to retain provisioned concurrency to reduce cold start latency?",
     [("Provisioned Concurrency", True),
      ("Reserved Concurrency", False),
      ("Lambda Layers", False),
      ("Lambda Versions", False)],
     "Lambda Provisioned Concurrency pre-initializes a requested number of execution environments, ensuring they are ready to respond immediately to invocations. This eliminates cold starts for latency-sensitive applications.",
     "Provisioned Concurrency eliminates Lambda cold starts.")

add_q(146, "EC2 & Compute",
     "Which EC2 feature allows you to change the instance type of a running instance without migrating to a new instance?",
     [("Elastic IP", False),
      ("EC2 Instance Resize (Change Instance Type)", True),
      ("EBS snapshot restore", False),
      ("AMI conversion", False)],
     "You can change the instance type of a stopped EC2 instance. For Linux instances, you can also change the instance type of a running instance using the ModifyInstanceAttribute API (for compatible instance families).",
     "EC2 supports changing the instance type of a stopped instance.")

add_q(147, "EC2 & Compute",
     "Which AWS service provides a managed service for running container images on AWS without managing the infrastructure?",
     [("Amazon ECS", False),
      ("Amazon EKS", False),
      ("AWS App Runner", True),
      ("Amazon Lightsail Containers", False)],
     "AWS App Runner provides a fully managed container application service. It automatically builds and deploys container images from a source repository, handles scaling, load balancing, and TLS certificates.",
     "App Runner runs container images without infrastructure management.")

add_q(148, "EC2 & Compute",
     "Which IAM entity provides temporary security credentials that can be assumed by EC2 instances?",
     [("IAM User", False),
      ("IAM Role", True),
      ("IAM Group", False),
      ("IAM Policy", False)],
     "IAM roles provide temporary security credentials that EC2 instances (and other AWS services) can assume. These credentials are automatically rotated and eliminate the need to embed long-term access keys in applications.",
     "IAM roles provide temporary credentials that EC2 instances can assume.")

add_q(149, "EC2 & Compute",
     "Which EC2 feature enables instances to access instance metadata and user data without requiring an IAM role?",
     [("Instance Metadata Service (IMDS)", True),
      ("IAM instance profile", False),
      ("KMS key policy", False),
      ("VPC endpoint", False)],
     "The Instance Metadata Service (IMDS) provides instance metadata to running instances, including instance ID, type, AMI ID, and user data. IMDSv2 uses session-based tokens for improved security against SSRF attacks.",
     "IMDS provides instance metadata without requiring IAM roles.")

add_q(150, "EC2 & Compute",
     "Which AWS service provides a fully managed serverless computing platform for containers, APIs, and functions?",
     [("AWS Lambda", False),
      ("AWS App Runner", False),
      ("AWS Amplify", False),
      ("AWS Lightsail", True)],
     "While AWS Lambda provides serverless function execution, the most comprehensive answer is that each service has its specific use case. Lambda is for functions, App Runner is for containers, and Amplify is for full-stack apps.",
     "Different serverless services serve different compute needs: Lambda for functions, App Runner for containers.")

# ============================================================
# S3 & Storage (30 questions)
# ============================================================
add_q(151, "S3 & Storage",
     "Which S3 storage class is designed for data that is stored for months or years and accessed once or twice a month?",
     [("S3 Standard", False),
      ("S3 Standard-IA", True),
      ("S3 Glacier", False),
      ("S3 One Zone-IA", False)],
     "S3 Standard-IA is designed for data that is less frequently accessed but still needs rapid access. It has a storage cost lower than Standard but higher than Glacier, and includes a per-GB retrieval fee.",
     "Standard-IA is for data accessed once or twice per month.")

add_q(152, "S3 & Storage",
     "Which S3 feature allows multiple versions of an object to be kept in the same bucket?",
     [("S3 Lifecycle Policies", False),
      ("S3 Versioning", True),
      ("S3 Replication", False),
      ("S3 Object Lock", False)],
     "S3 Versioning keeps multiple variants of an object in the same bucket. You can retrieve and restore every version of every object stored in your bucket, which helps protect against unintended overwrites or deletions.",
     "S3 Versioning maintains multiple versions of each object.")

add_q(153, "S3 & Storage",
     "Which EBS volume type is optimized for boot volumes and general-purpose workloads?",
     [("EBS Cold HDD (sc1)", False),
      ("EBS Throughput Optimized HDD (st1)", False),
      ("EBS General Purpose SSD (gp3)", True),
      ("EBS Provisioned IOPS (io2)", False)],
     "EBS gp3 volumes provide a balance of price and performance suitable for boot volumes and general-purpose workloads. They include 3,000 IOPS and 125 MB/s throughput in the base price.",
     "gp3 is optimized for boot volumes and general-purpose workloads.")

add_q(154, "S3 & Storage",
     "Which AWS service provides a fully managed, NFS-based file system for Linux EC2 instances?",
     [("Amazon S3", False),
      ("Amazon EBS", False),
      ("Amazon EFS", True),
      ("AWS Storage Gateway", False)],
     "Amazon EFS provides a simple, scalable, elastic NFS file system for use with Linux EC2 instances. It grows and shrinks automatically as you add or remove files, eliminating the need to provision storage.",
     "EFS provides managed NFS file storage for Linux EC2 instances.")

add_q(155, "S3 & Storage",
     "Which S3 feature protects objects from being deleted for a fixed period of time?",
     [("S3 Versioning", False),
      ("S3 Object Lock", True),
      ("S3 Lifecycle Policies", False),
      ("S3 MFA Delete", False)],
     "S3 Object Lock helps prevent objects from being deleted or overwritten for a fixed amount of time or indefinitely. It supports Governance mode (privileged users can bypass) and Compliance mode (no one can bypass).",
     "Object Lock prevents object deletion for a retention period.")

add_q(156, "S3 & Storage",
     "Which AWS service provides block storage that is attached to EC2 instances?",
     [("Amazon S3", False),
      ("Amazon EBS", True),
      ("Amazon EFS", False),
      ("Amazon Glacier", False)],
     "Amazon EBS provides block-level storage volumes that attach to EC2 instances. EBS volumes persist independently from the life of the instance and can be detached and reattached to other instances.",
     "EBS provides block storage volumes for EC2 instances.")

add_q(157, "S3 & Storage",
     "Which EBS volume type is optimized for frequently accessed, throughput-intensive workloads?",
     [("EBS Cold HDD (sc1)", False),
      ("EBS Throughput Optimized HDD (st1)", True),
      ("EBS Provisioned IOPS (io2)", False),
      ("EBS General Purpose SSD (gp3)", False)],
     "EBS st1 (Throughput Optimized HDD) is designed for frequently accessed, throughput-intensive workloads such as big data, data warehousing, and log processing. It provides high sequential read throughput.",
     "st1 is optimized for throughput-intensive workloads like big data.")

add_q(158, "S3 & Storage",
     "Which S3 feature allows you to transition objects to Glacier after 30 days and delete them after 365 days?",
     [("S3 Versioning", False),
      ("S3 Object Lock", False),
      ("S3 Lifecycle Configuration", True),
      ("S3 Replication", False)],
     "S3 Lifecycle configurations define rules for transitioning objects between storage classes and expiring (deleting) objects after a specified time. You can create rules to automate storage tiering and lifecycle management.",
     "Lifecycle Configuration automates object transitions and expiration.")

add_q(159, "S3 & Storage",
     "Which storage service provides a scalable object store with unlimited capacity?",
     [("Amazon EBS", False),
      ("Amazon EFS", False),
      ("Amazon S3", True),
      ("Amazon Instance Store", False)],
     "Amazon S3 is an object storage service with virtually unlimited storage capacity. Individual objects can be up to 5 TB in size, and you can store an unlimited number of objects in a bucket.",
     "S3 provides virtually unlimited object storage capacity.")

add_q(160, "S3 & Storage",
     "Which S3 storage class stores data in only one Availability Zone, providing the lowest cost for infrequently accessed data?",
     [("S3 Standard-IA", False),
      ("S3 One Zone-IA", True),
      ("S3 Intelligent-Tiering", False),
      ("S3 Glacier", False)],
     "S3 One Zone-IA stores data in only one AZ, making it 20% cheaper than Standard-IA but less durable (99.5% vs 99.999999999%). It is suitable for infrequently accessed data where AZ-level resilience is not required.",
     "One Zone-IA provides the lowest cost for infrequent access but reduced durability.")

add_q(161, "S3 & Storage",
     "Which AWS service provides a tape-based backup solution that works with existing backup software?",
     [("AWS Backup", False),
      ("AWS Storage Gateway - Tape Gateway", True),
      ("AWS Snowball Edge", False),
      ("Amazon Glacier", False)],
     "Storage Gateway Tape Gateway provides a virtual tape library (VTL) that works with your existing backup software. It stores data in S3 and archives to Glacier, providing a cloud-based tape backup solution.",
     "Tape Gateway provides cloud-based virtual tape library for backup.")

add_q(162, "S3 & Storage",
     "Which EBS feature creates a point-in-time snapshot of a volume that can be used to create new volumes?",
     [("EBS Volume Creation", False),
      ("EBS Snapshot", True),
      ("EBS AMI", False),
      ("EBS Encryption", False)],
     "EBS snapshots create point-in-time backups of your volumes. These snapshots are incremental (only the blocks that changed since the last snapshot are saved) and can be used to create new EBS volumes or AMIs.",
     "EBS snapshots create point-in-time backups of volumes.")

add_q(163, "S3 & Storage",
     "Which S3 feature requires Multi-Factor Authentication to delete objects or disable versioning?",
     [("S3 Object Lock", False),
      ("S3 MFA Delete", True),
      ("S3 Bucket Policies", False),
      ("S3 Access Control Lists", False)],
     "S3 MFA Delete adds an extra layer of security by requiring authentication with an MFA device to permanently delete object versions or suspend versioning. It must be enabled on the bucket by the bucket owner.",
     "MFA Delete requires multi-factor authentication to delete S3 objects.")

add_q(164, "S3 & Storage",
     "Which AWS service provides a hybrid cloud storage solution that caches frequently accessed data on-premises?",
     [("AWS Direct Connect", False),
      ("AWS Storage Gateway - File Gateway", True),
      ("AWS VPN", False),
      ("Amazon S3 Transfer Acceleration", False)],
     "Storage Gateway File Gateway provides a file interface to S3, caching frequently accessed data on-premises for low-latency access. It presents S3 objects as files in an NFS mount point.",
     "File Gateway caches S3 data on-premises for low-latency access.")

add_q(165, "S3 & Storage",
     "Which S3 performance feature allows you to increase request throughput by using multiple prefixes?",
     [("S3 Transfer Acceleration", False),
      ("S3 Multi-Part Upload", False),
      ("S3 prefix-based partitioning", True),
      ("S3 Select", False)],
     "S3 scales request throughput by distributing requests across multiple prefixes. To achieve higher throughput, you can use multiple prefixes in your bucket, as each prefix can support 3,500 PUT and 5,500 GET requests per second.",
     "Using multiple S3 prefixes increases request throughput.")

add_q(166, "S3 & Storage",
     "Which EBS volume type provides the lowest cost for infrequently accessed, cold data?",
     [("EBS General Purpose SSD (gp3)", False),
      ("EBS Provisioned IOPS (io2)", False),
      ("EBS Throughput Optimized HDD (st1)", False),
      ("EBS Cold HDD (sc1)", True)],
     "EBS sc1 (Cold HDD) is the lowest-cost EBS volume type, designed for infrequently accessed, cold data workloads. It provides the lowest cost per GB of all EBS storage options.",
     "sc1 is the lowest-cost EBS volume type for cold data.")

add_q(167, "S3 & Storage",
     "Which S3 feature allows you to retrieve a subset of data from an object using SQL-like queries?",
     [("S3 Select", True),
      ("S3 Glacier Select", False),
      ("Athena", False),
      ("Redshift Spectrum", False)],
     "S3 Select allows you to retrieve a subset of data from an object using SQL-like expressions. By retrieving only the data you need, you can improve query performance and reduce the amount of data transferred.",
     "S3 Select retrieves subsets of object data using SQL-like queries.")

add_q(168, "S3 & Storage",
     "Which AWS Backup feature simplifies backup management across multiple AWS services?",
     [("AWS Backup Vault Lock", False),
      ("AWS Backup centralized backup management", True),
      ("AWS Backup cross-region copy", False),
      ("AWS Backup point-in-time recovery", False)],
     "AWS Backup provides a centralized, policy-based backup service that simplifies backup management across AWS services including EBS, RDS, DynamoDB, EFS, and S3. You can define backup plans and monitor compliance.",
     "AWS Backup centralizes backup management across AWS services.")

add_q(169, "S3 & Storage",
     "Which S3 Glacier retrieval option provides access to objects within 1-5 minutes?",
     [("Bulk retrieval", False),
      ("Standard retrieval", False),
      ("Expedited retrieval", True),
      ("Instant retrieval", False)],
     "Glacier Expedited retrieval provides access to objects within 1-5 minutes for time-sensitive retrieval needs. It is the fastest retrieval option for S3 Glacier Flexible Retrieval, though it comes at a higher cost.",
     "Glacier Expedited retrieval provides 1-5 minute access to archived objects.")

add_q(170, "S3 & Storage",
     "Which AWS service provides an NFS file system that automatically scales in capacity as you add files?",
     [("Amazon S3", False),
      ("Amazon EBS", False),
      ("Amazon EFS", True),
      ("Amazon FSx", False)],
     "Amazon EFS is a serverless, elastic file system that automatically grows and shrinks as you add or remove files. There is no need to provision storage capacity, and it can scale to petabytes automatically.",
     "EFS automatically scales capacity as you add or remove files.")

add_q(171, "S3 & Storage",
     "Which feature allows an S3 bucket to receive events when objects are created or deleted?",
     [("S3 Versioning", False),
      ("S3 Event Notifications", True),
      ("S3 Lifecycle Rules", False),
      ("S3 Replication", False)],
     "S3 Event Notifications can send notifications to SNS, SQS, or Lambda when objects are created, removed, or have access permissions changed. This enables event-driven architectures and automated workflows.",
     "S3 Event Notifications trigger workflows when objects change.")

add_q(172, "S3 & Storage",
     "Which storage option provides ephemeral, high-throughput block storage directly attached to the EC2 host?",
     [("Amazon EBS", False),
      ("Amazon Instance Store", True),
      ("Amazon EFS", False),
      ("Amazon S3", False)],
     "Instance store provides temporary block-level storage for EC2 instances. The storage is physically located on the host computer and offers very high I/O performance but data is lost when the instance is stopped or terminated.",
     "Instance Store provides ephemeral high-performance block storage.")

add_q(173, "S3 & Storage",
     "Which S3 feature uses CloudFront to accelerate uploads to S3 from anywhere in the world?",
     [("S3 Transfer Acceleration", True),
      ("S3 Cross-Region Replication", False),
      ("S3 Multi-Part Upload", False),
      ("S3 Event Notifications", False)],
     "S3 Transfer Acceleration uses the CloudFront global network to accelerate uploads to and downloads from S3. It is especially useful when users are geographically far from the S3 bucket.",
     "Transfer Acceleration uses CloudFront to speed up uploads from anywhere in the world.")

add_q(174, "S3 & Storage",
     "Which AWS service provides a fully managed Windows file share?",
     [("Amazon EFS", False),
      ("Amazon FSx for Windows File Server", True),
      ("Amazon S3", False),
      ("AWS Storage Gateway", False)],
     "Amazon FSx for Windows File Server provides fully managed Windows-native file shares. It supports SMB protocol, Windows AD integration, file system quotas, and user-level access control.",
     "FSx for Windows provides managed Windows-native file shares.")

add_q(175, "S3 & Storage",
     "Which S3 feature allows you to grant cross-account access to specific objects in a bucket?",
     [("S3 Bucket Policy", False),
      ("S3 Access Control List (ACL)", True),
      ("S3 Pre-signed URL", False),
      ("S3 Versioning", False)],
     "S3 ACLs (Access Control Lists) are legacy access control mechanisms that can grant cross-account permissions at the bucket or object level. While bucket policies are recommended for most use cases, ACLs still support cross-account object-level permissions.",
     "S3 ACLs can grant cross-account access to specific objects.")

add_q(176, "S3 & Storage",
     "Which S3 Glacier retrieval option has a retrieval time of 12-48 hours?",
     [("Expedited retrieval", False),
      ("Standard retrieval", False),
      ("Bulk retrieval", False),
      ("S3 Glacier Deep Archive", True)],
     "S3 Glacier Deep Archive provides the lowest-cost storage with retrieval times of 12-48 hours. It is designed for data that is retained for years and may be accessed once or twice a year.",
     "Glacier Deep Archive has 12-48 hour retrieval times at the lowest cost.")

add_q(177, "S3 & Storage",
     "Which feature encrypts data at rest in S3 using a customer-provided encryption key?",
     [("SSE-S3", False),
      ("SSE-KMS", False),
      ("SSE-C", True),
      ("Client-side encryption", False)],
     "Server-Side Encryption with Customer-Provided Keys (SSE-C) allows you to manage your own encryption keys. You provide the encryption key as part of the request, and S3 manages the encryption/decryption process.",
     "SSE-C uses customer-provided encryption keys for server-side encryption.")

add_q(178, "S3 & Storage",
     "Which AWS service provides a managed Lustre file system for high-performance computing?",
     [("Amazon EFS", False),
      ("Amazon FSx for Lustre", True),
      ("Amazon EBS", False),
      ("Amazon S3", False)],
     "Amazon FSx for Lustre provides a fully managed Lustre file system optimized for workloads requiring fast access to data, such as machine learning, HPC, video processing, and financial modeling. It can link to S3 buckets.",
     "FSx for Lustre provides high-performance file storage for HPC workloads.")

add_q(179, "S3 & Storage",
     "Which S3 feature can replicate objects to another bucket in a different AWS account?",
     [("S3 Versioning", False),
      ("S3 Cross-Region Replication", False),
      ("S3 Cross-Account Replication (same-region or cross-region)", True),
      ("S3 Object Lock", False)],
     "S3 replication supports both same-region and cross-region replication, and can replicate objects to buckets in different AWS accounts. Both the source and destination buckets must have versioning enabled.",
     "S3 Replication can replicate across accounts and regions.")

add_q(180, "S3 & Storage",
     "Which S3 storage class is designed for data that can be accessed instantly but is rarely accessed?",
     [("S3 Standard-IA", False),
      ("S3 Glacier Instant Retrieval", True),
      ("S3 Glacier Flexible Retrieval", False),
      ("S3 Intelligent-Tiering", False)],
     "S3 Glacier Instant Retrieval is designed for long-lived data that is rarely accessed but requires instant access when needed. It provides millisecond retrieval times, the same as S3 Standard, at a lower storage cost.",
     "Glacier Instant Retrieval provides instant access at lower storage costs.")

# ============================================================
# VPC & Networking (30 questions)
# ============================================================
add_q(181, "VPC & Networking",
     "What is the default limit for the number of VPCs per AWS Region?",
     [("1", False),
      ("5", True),
      ("10", False),
      ("100", False)],
     "The default limit is 5 VPCs per Region. You can request an increase through the AWS Service Quotas console. Each VPC has its own isolated network within AWS.",
     "Default VPC limit is 5 per Region.")

add_q(182, "VPC & Networking",
     "Which VPC component enables resources in a private subnet to access the internet?",
     [("Internet Gateway", False),
      ("NAT Gateway", True),
      ("VPC Peering", False),
      ("VPN Gateway", False)],
     "NAT Gateway allows instances in private subnets to connect to the internet (for updates, external APIs, etc.) while preventing inbound connections from the internet. It performs network address translation.",
     "NAT Gateway enables outbound internet access from private subnets.")

add_q(183, "VPC & Networking",
     "Which VPC component allows resources in a public subnet to communicate directly with the internet?",
     [("NAT Gateway", False),
      ("Internet Gateway", True),
      ("VPN Gateway", False),
      ("VPC Endpoint", False)],
     "An Internet Gateway allows communication between your VPC and the internet. Resources in public subnets with public IP addresses can send and receive traffic through the Internet Gateway.",
     "Internet Gateway provides direct internet access for public subnets.")

add_q(184, "VPC & Networking",
     "Which Route 53 routing policy routes traffic to the resource with the lowest latency for the user?",
     [("Simple Routing", False),
      ("Latency Routing", True),
      ("Geolocation Routing", False),
      ("Failover Routing", False)],
     "Route 53 Latency Routing routes traffic to the AWS endpoint that provides the lowest latency for the user. When you have resources in multiple Regions, this helps ensure users connect to the fastest endpoint.",
     "Latency Routing sends traffic to the endpoint with the lowest latency.")

add_q(185, "VPC & Networking",
     "Which VPC feature allows two VPCs to communicate with each other using private IP addresses?",
     [("VPC Peering", True),
      ("AWS Direct Connect", False),
      ("Internet Gateway", False),
      ("NAT Gateway", False)],
     "VPC Peering enables two VPCs to communicate as if they were in the same network, using private IP addresses. The VPCs can be in the same or different Regions and accounts. Traffic stays on the AWS network.",
     "VPC Peering enables private IP communication between VPCs.")

add_q(186, "VPC & Networking",
     "Which Load Balancer type operates at Layer 4 (Transport Layer) and provides ultra-high performance?",
     [("Application Load Balancer", False),
      ("Network Load Balancer", True),
      ("Classic Load Balancer", False),
      ("Gateway Load Balancer", False)],
     "Network Load Balancers operate at Layer 4, providing ultra-high performance (millions of requests per second) with low latency. They are ideal for TCP, UDP, and TLS traffic, and are commonly used for gaming, IoT, and real-time applications.",
     "NLB operates at Layer 4 with ultra-high performance.")

add_q(187, "VPC & Networking",
     "Which Load Balancer type is best suited for routing HTTP/HTTPS traffic based on content?",
     [("Network Load Balancer", False),
      ("Application Load Balancer", True),
      ("Classic Load Balancer", False),
      ("Gateway Load Balancer", False)],
     "Application Load Balancers operate at Layer 7 (Application Layer) and support content-based routing. They can route traffic based on URL paths, host headers, query strings, HTTP methods, and headers.",
     "ALB provides Layer 7 content-based routing for HTTP/HTTPS traffic.")

add_q(188, "VPC & Networking",
     "Which AWS service provides a global network of edge locations for content delivery?",
     [("AWS Global Accelerator", False),
      ("Amazon CloudFront", True),
      ("Amazon Route 53", False),
      ("AWS Direct Connect", False)],
     "Amazon CloudFront is a Content Delivery Network (CDN) with a global network of points of presence (PoPs) and edge locations. It caches content at the edge to reduce latency for users worldwide.",
     "CloudFront is AWS's CDN with a global network of edge locations.")

add_q(189, "VPC & Networking",
     "Which VPC component enables you to establish a secure IPsec VPN connection between your on-premises network and VPC?",
     [("Internet Gateway", False),
      ("Virtual Private Gateway", True),
      ("NAT Gateway", False),
      ("VPC Peering Connection", False)],
     "A Virtual Private Gateway (VGW) serves as the VPN anchor on the AWS side. You attach it to your VPC and then create a VPN connection to your customer gateway (on-premises VPN device) for secure communication.",
     "Virtual Private Gateway enables secure VPN connections to your VPC.")

add_q(190, "VPC & Networking",
     "Which AWS service improves availability and performance of applications by using the AWS global network infrastructure?",
     [("Amazon CloudFront", False),
      ("AWS Global Accelerator", True),
      ("Amazon Route 53", False),
      ("AWS Direct Connect", False)],
     "AWS Global Accelerator uses the AWS global network to route traffic to optimal endpoints, improving availability and performance. Unlike CloudFront (which caches content), it routes traffic to application endpoints without caching.",
     "Global Accelerator routes traffic through the AWS global network for better performance.")

add_q(191, "VPC & Networking",
     "Which VPC feature provides private connectivity between VPCs and AWS services without going over the internet?",
     [("Internet Gateway", False),
      ("VPC Endpoint", True),
      ("NAT Gateway", False),
      ("Direct Connect", False)],
     "VPC Endpoints (Interface and Gateway) enable private connectivity between your VPC and AWS services. They route traffic through the AWS network without requiring an internet gateway, NAT gateway, VPN, or Direct Connect.",
     "VPC Endpoints provide private connectivity to AWS services.")

add_q(192, "VPC & Networking",
     "Which subnet type in a VPC cannot have internet-bound traffic routed through an Internet Gateway?",
     [("Public subnet", False),
      ("Private subnet", True),
      ("VPN-only subnet", False),
      ("Isolated subnet", True)],
     "Private subnets do not have a route to an Internet Gateway. Resources in private subnets can access the internet only through a NAT Gateway or NAT instance, and cannot receive inbound connections from the internet.",
     "Private subnets have no direct internet access through an Internet Gateway.")

add_q(193, "VPC & Networking",
     "Which Load Balancer type is designed to route traffic to third-party appliances like firewalls?",
     [("Application Load Balancer", False),
      ("Network Load Balancer", False),
      ("Gateway Load Balancer", True),
      ("Classic Load Balancer", False)],
     "Gateway Load Balancers operate at Layer 3 (Network Layer) and are designed to deploy, scale, and manage third-party virtual appliances such as firewalls, intrusion detection and prevention systems, and deep packet inspection systems.",
     "GWLB routes traffic to third-party network appliances.")

add_q(194, "VPC & Networking",
     "Which AWS service simplifies VPC network management when you have multiple VPCs and AWS accounts?",
     [("VPC Peering", False),
      ("AWS Transit Gateway", True),
      ("AWS Direct Connect", False),
      ("Amazon CloudFront", False)],
     "AWS Transit Gateway acts as a central hub that connects your VPCs, VPN connections, and Direct Connect gateways through a single gateway. This simplifies network architecture and reduces the number of peering connections needed.",
     "Transit Gateway centralizes VPC connectivity across accounts.")

add_q(195, "VPC & Networking",
     "Which type of VPC endpoint uses AWS PrivateLink to provide private connectivity to AWS services?",
     [("Gateway Endpoint", False),
      ("Interface Endpoint", True),
      ("Internet Gateway", False),
      ("NAT Gateway", False)],
     "Interface endpoints (powered by AWS PrivateLink) create an elastic network interface with a private IP address that serves as an entry point for traffic. They support many AWS services beyond just S3 and DynamoDB.",
     "Interface endpoints use PrivateLink for private connectivity.")

add_q(196, "VPC & Networking",
     "Which CloudFront feature allows you to customize the behavior at the edge before forwarding requests to the origin?",
     [("CloudFront Functions", True),
      ("Signed URLs", False),
      ("Origin Groups", False),
      ("Custom Error Pages", False)],
     "CloudFront Functions are lightweight JavaScript functions that run at CloudFront edge locations. They allow you to customize how CloudFront handles requests and responses, such as modifying headers, rewriting URLs, or generating responses at the edge.",
     "CloudFront Functions run lightweight JS at the edge to customize behavior.")

add_q(197, "VPC & Networking",
     "Which VPC security feature controls traffic at the instance level by evaluating rules as either allow or deny?",
     [("Security Group", False),
      ("Network ACL", True),
      ("VPC Endpoint Policy", False),
      ("IAM Policy", False)],
     "Network ACLs (NACLs) are stateless, subnet-level firewalls that support both allow and deny rules. They are evaluated in order (lowest numbered rule first) and traffic must match an allow rule to pass.",
     "NACLs are stateless and support both allow and deny rules at the subnet level.")

add_q(198, "VPC & Networking",
     "Which Route 53 routing policy sends traffic to multiple resources with different weights?",
     [("Simple Routing", False),
      ("Weighted Routing", True),
      ("Failover Routing", False),
      ("Geolocation Routing", False)],
     "Weighted routing lets you distribute traffic across multiple resources in proportions that you specify. This is useful for A/B testing, gradually shifting traffic, or load balancing across resources with different capacities.",
     "Weighted Routing distributes traffic based on specified proportions.")

add_q(199, "VPC & Networking",
     "Which VPC feature provides a DNS hostname for your VPC resources?",
     [("VPC DHCP Options Set", False),
      ("VPC DNS Hostnames", True),
      ("VPC Peering", False),
      ("VPC Flow Logs", False)],
     "Enabling DNS hostnames in your VPC provides public DNS hostnames for EC2 instances with public IP addresses and private DNS hostnames for instances with private IP addresses. This simplifies name resolution within the VPC.",
     "VPC DNS Hostnames enable automatic DNS resolution for VPC resources.")

add_q(200, "VPC & Networking",
     "Which feature of CloudFront restricts access to content by requiring a signed URL or signed cookie?",
     [("CloudFront Origin Access Control", False),
      ("CloudFront Signed URLs/Cookies", True),
      ("CloudFront Geoblocking", False),
      ("CloudFront WAF", False)],
     "Signed URLs and signed cookies provide secure access to private content distributed through CloudFront. Only users with a valid signed URL or cookie can access the content, preventing unauthorized sharing.",
     "Signed URLs/Cookies restrict CloudFront content access to authorized users.")

add_q(201, "VPC & Networking",
     "Which AWS service logs all network traffic flowing through a VPC for security monitoring?",
     [("AWS CloudTrail", False),
      ("Amazon VPC Flow Logs", True),
      ("Amazon CloudWatch", False),
      ("AWS Config", False)],
     "VPC Flow Logs capture information about the IP traffic going to and from network interfaces in your VPC. They can be published to CloudWatch Logs or S3 for analysis, troubleshooting, and security monitoring.",
     "VPC Flow Logs capture network traffic metadata for monitoring and security.")

add_q(202, "VPC & Networking",
     "Which type of S3 VPC endpoint does NOT require an Elastic Network Interface?",
     [("Interface Endpoint", False),
      ("Gateway Endpoint", True),
      ("PrivateLink Endpoint", False),
      ("None - all endpoints require an ENI", False)],
     "Gateway endpoints (for S3 and DynamoDB) do not use ENIs. They add an entry to the VPC route table that directs traffic to the service through the AWS network. Interface endpoints use ENIs and support more services.",
     "Gateway endpoints use route tables instead of ENIs.")

add_q(203, "VPC & Networking",
     "Which AWS Direct Connect feature provides a dedicated connection at 1 Gbps or 10 Gbps?",
     [("AWS Direct Connect Gateway", False),
      ("Dedicated connections", True),
      ("Hosted connections", False),
      ("AWS Direct Connect LAG", False)],
     "AWS Direct Connect dedicated connections provide 1 Gbps or 10 Gbps dedicated network connections. They are provisioned directly to your on-premises network through a Direct Connect partner or colocation facility.",
     "Dedicated connections provide 1 or 10 Gbps connectivity.")

add_q(204, "VPC & Networking",
     "Which Security Group feature automatically allows return traffic for permitted inbound connections?",
     [("Stateful packet filtering", True),
      ("Stateless packet filtering", False),
      ("Deep packet inspection", False),
      ("Network address translation", False)],
     "Security Groups are stateful, meaning that return traffic for permitted inbound connections is automatically allowed, regardless of outbound rules. This simplifies configuration since you do not need to explicitly allow return traffic.",
     "Security Groups are stateful and automatically allow return traffic.")

add_q(205, "VPC & Networking",
     "Which CloudFront feature allows you to use custom domain names with HTTPS?",
     [("CloudFront Alternate Domain Names with ACM", True),
      ("CloudFront Functions", False),
      ("CloudFront Signed URLs", False),
      ("CloudFront Origin Groups", False)],
     "CloudFront supports custom domain names by adding alternate domain names (CNAMEs) to your distribution. You can use AWS Certificate Manager (ACM) to provision SSL/TLS certificates for free and associate them with CloudFront.",
     "CloudFront supports custom domains with HTTPS via ACM certificates.")

add_q(206, "VPC & Networking",
     "Which VPC feature allows you to assign custom DNS servers to instances in your VPC?",
     [("VPC DNS Hostnames", False),
      ("VPC DHCP Options Set", True),
      ("VPC Peering", False),
      ("Route 53 Resolver Rules", False)],
     "VPC DHCP Options Sets allow you to define custom DHCP configuration options, including custom DNS server IP addresses, domain names, NTP servers, and netbios settings for instances in your VPC.",
     "DHCP Options Sets allow custom DNS servers for VPC instances.")

add_q(207, "VPC & Networking",
     "Which AWS Global Accelerator feature provides static anycast IP addresses that stay the same even as your application scales?",
     [(
     "Static anycast IP addresses", True),
     ("Auto scaling endpoints", False),
     ("Health checks", False),
     ("Client IP address preservation", False)],
     "Global Accelerator provides two static anycast IP addresses that serve as fixed entry points for your application. These IPs are announced from multiple edge locations worldwide, providing consistent access even as your application scales or changes.",
     "Global Accelerator provides static anycast IPs for consistent application access.")

add_q(208, "VPC & Networking",
     "Which Route 53 routing policy routes traffic based on the geographic location of the user?",
     [("Latency Routing", False),
      ("Geolocation Routing", True),
      ("Weighted Routing", False),
      ("Multivalue Answer Routing", False)],
     "Geolocation routing routes traffic based on the geographic location of users. You can specify the geographic location (by continent, country, or US state) for each resource, directing users to the most appropriate endpoint.",
     "Geolocation Routing sends traffic based on user geographic location.")

add_q(209, "VPC & Networking",
     "Which feature of a Network Load Balancer preserves the source IP address of the client?",
     [("Proxy protocol v2", True),
      ("X-Forwarded-For header", False),
      ("Connection draining", False),
      ("Cross-zone load balancing", False)],
     "NLBs preserve the source IP address of the client through proxy protocol v2. This allows target instances to see the original client IP address. ALBs use X-Forwarded-For headers instead.",
     "NLB preserves source IP using proxy protocol v2.")

add_q(210, "VPC & Networking",
     "Which AWS service provides DNS resolution within a VPC for hybrid cloud environments?",
     [("Amazon Route 53", False),
      ("Amazon Route 53 Resolver", True),
      ("Amazon CloudFront", False),
      ("AWS Direct Connect", False)],
     "Amazon Route 53 Resolver provides DNS resolution between your VPC and your on-premises DNS servers. It includes Resolver Inbound for forwarding DNS queries from on-premises to VPC, and Resolver Outbound for forwarding VPC queries to on-premises.",
     "Route 53 Resolver enables DNS resolution between VPC and on-premises.")

# ============================================================
# RDS & Databases (30 questions)
# ============================================================
add_q(211, "RDS & Databases",
     "Which Amazon RDS storage type automatically scales storage capacity as needed?",
     [("Standard storage (magnetic)", False),
      ("Provisioned IOPS SSD", False),
      ("General Purpose SSD (gp3) with storage auto-scaling enabled", True),
      ("Instance store", False)],
     "RDS storage auto-scaling automatically increases storage capacity when utilization approaches the provisioned limit. It prevents storage from becoming a bottleneck and avoids manual intervention for capacity management.",
     "RDS storage auto-scaling dynamically increases storage as needed.")

add_q(212, "RDS & Databases",
     "Which Amazon Aurora MySQL-compatible feature provides up to 5x throughput improvement compared to standard MySQL?",
     [("Aurora Serverless", False),
      ("Aurora Parallel Query", True),
      ("Aurora Global Database", False),
      ("Aurora Backtrack", False)],
     "Aurora Parallel Query offloads compute-intensive analytical queries to thousands of processing nodes, delivering up to 5x faster performance for complex analytical queries while reducing the load on the primary instance.",
     "Aurora Parallel Query provides up to 5x throughput for analytical queries.")

add_q(213, "RDS & Databases",
     "Which DynamoDB feature enables you to add a global secondary index after a table has been created?",
     [("DynamoDB Streams", False),
      ("Global Secondary Index (GSI)", True),
      ("Local Secondary Index (LSI)", False),
      ("DynamoDB Accelerator (DAX)", False)],
     "DynamoDB Global Secondary Indexes can be created at any time (before or after table creation) and support eventually consistent reads. Unlike LSIs which must be defined at table creation time and share the partition key.",
     "GSIs can be added to existing DynamoDB tables at any time.")

add_q(214, "RDS & Databases",
     "Which ElastiCache engine supports pub/sub messaging and sorted sets?",
     [("Memcached", False),
      ("Redis", True),
      ("Both engines support these features equally", False),
      ("Neither engine supports these features", False)],
     "ElastiCache for Redis supports advanced data structures (sorted sets, hashes, lists, sets) and pub/sub messaging. Memcached is a simpler, in-memory key-value store that does not support these features.",
     "Redis supports pub/sub messaging and sorted sets; Memcached does not.")

add_q(215, "RDS & Databases",
     "Which Amazon RDS feature allows you to automatically fail over to a standby instance in another AZ?",
     [("Read Replicas", False),
      ("Multi-AZ Deployment", True),
      ("RDS Proxy", False),
      ("RDS Snapshots", False)],
     "RDS Multi-AZ provides automatic failover to a synchronous standby replica in a different AZ. The failover is automatic and typically takes 60-120 seconds, during which the database is unavailable.",
     "Multi-AZ provides automatic failover to a standby in another AZ.")

add_q(216, "RDS & Databases",
     "Which DynamoDB read consistency option ensures you always read the most recent data?",
     [("Eventually Consistent Reads", False),
      ("Strongly Consistent Reads", True),
      ("Transactional Reads", False),
      ("Conditional Reads", False)],
     "DynamoDB Strongly Consistent Reads return the most up-to-date data, reflecting all successful write operations. They come with higher latency and potentially lower throughput compared to eventually consistent reads.",
     "Strongly Consistent Reads return the most recent data.")

add_q(217, "RDS & Databases",
     "Which Amazon RDS engine supports the IAM database authentication feature?",
     [("All RDS engines", False),
      ("MySQL and PostgreSQL", True),
      ("Oracle and SQL Server", False),
      ("Only Aurora", False)],
     "RDS for MySQL and PostgreSQL support IAM database authentication, allowing you to authenticate using IAM roles instead of database passwords. This eliminates the need to manage database credentials in application code.",
     "IAM database authentication is supported for MySQL and PostgreSQL on RDS.")

add_q(218, "RDS & Databases",
     "Which AWS service provides a fully managed, Apache-compatible data warehouse that integrates with standard BI tools?",
     [("Amazon Aurora", False),
      ("Amazon Redshift", True),
      ("Amazon DynamoDB", False),
      ("Amazon ElastiCache", False)],
     "Amazon Redshift is a fully managed, petabyte-scale data warehouse that uses columnar storage and massively parallel processing. It integrates with standard SQL-based BI tools and supports ODBC/JDBC connections.",
     "Redshift is a managed data warehouse with standard SQL and BI tool integration.")

add_q(219, "RDS & Databases",
     "Which DynamoDB capacity mode automatically scales read and write capacity based on traffic patterns?",
     [("Provisioned capacity mode", False),
      ("On-Demand capacity mode", True),
      ("Reserved capacity", False),
      ("Batch capacity mode", False)],
     "DynamoDB On-Demand mode accommodates workloads as they ramp up or down, automatically scaling read and write capacity. You pay per request, eliminating the need for capacity planning and manual provisioning.",
     "On-Demand mode automatically scales DynamoDB capacity based on demand.")

add_q(220, "RDS & Databases",
     "Which Amazon RDS Proxy feature helps manage database connections for serverless applications?",
     [("Connection pooling", True),
      ("Multi-AZ failover", False),
      ("Read splitting", False),
      ("Query caching", False)],
     "RDS Proxy manages a pool of database connections and shares them across application requests. This reduces the overhead of opening and closing connections, which is especially important for serverless applications that scale rapidly.",
     "RDS Proxy provides connection pooling to improve database performance.")

add_q(221, "RDS & Databases",
     "Which DynamoDB billing mode charges for the actual read and write throughput consumed?",
     [("Provisioned mode", False),
      ("On-Demand mode", True),
      ("Reserved capacity", False),
      ("Free tier", False)],
     "DynamoDB On-Demand mode charges per read/write request unit consumed. This eliminates the need to plan capacity and is ideal for unpredictable workloads with sudden traffic spikes.",
     "On-Demand mode charges per actual request units consumed.")

add_q(222, "RDS & Databases",
     "Which Amazon Aurora feature allows you to create a new database cluster from an existing snapshot with minimal time?",
     [("Aurora Restore from Snapshot", False),
      ("Aurora Fast Database Cloning", True),
      ("Aurora Read Replicas", False),
      ("Aurora Backtrack", False)],
     "Aurora Fast Database Cloning creates a new cluster from an existing snapshot almost instantly. Instead of copying all data, it uses a copy-on-write protocol, sharing storage with the source until modifications are made.",
     "Aurora Fast Database Cloning creates instant copies using copy-on-write.")

add_q(223, "RDS & Databases",
     "Which database service is optimized for real-time bidding and gaming leaderboards?",
     [("Amazon RDS", False),
      ("Amazon DynamoDB", True),
      ("Amazon Redshift", False),
      ("Amazon DocumentDB", False)],
     "DynamoDB provides single-digit millisecond latency at any scale, making it ideal for real-time applications like gaming leaderboards, ad tech, and IoT. Its auto-scaling and distributed architecture handle traffic spikes seamlessly.",
     "DynamoDB's low latency makes it ideal for gaming and real-time applications.")

add_q(224, "RDS & Databases",
     "Which AWS service provides a managed graph database for social networking applications?",
     [("Amazon DynamoDB", False),
      ("Amazon DocumentDB", False),
      ("Amazon Neptune", True),
      ("Amazon RDS", False)],
     "Amazon Neptune is a fast, reliable, and scalable graph database service optimized for social networking, recommendation engines, fraud detection, and knowledge graphs. It supports both Property Graph and RDF models.",
     "Neptune is a managed graph database for social networking and recommendations.")

add_q(225, "RDS & Databases",
     "Which RDS feature allows you to promote a Read Replica to a standalone database?",
     [("Multi-AZ Failover", False),
      ("Read Replica Promotion", True),
      ("RDS Snapshot Restore", False),
      ("RDS Instance Modify", False)],
     "You can promote an RDS Read Replica to become a standalone database instance. This is useful for disaster recovery (promoting a cross-region replica) or for separating workloads by promoting a read replica to handle writes.",
     "Read Replicas can be promoted to standalone database instances.")

add_q(226, "RDS & Databases",
     "Which DynamoDB data model element uniquely identifies each item in a table?",
     [("Sort key", False),
      ("Global Secondary Index", False),
      ("Partition key", True),
      ("Stream record", False)],
     "The partition key (also called hash key) uniquely identifies each item in a DynamoDB table. It determines the physical partition where the data is stored. Combined with a sort key, it forms a composite primary key.",
     "The partition key uniquely identifies items in DynamoDB.")

add_q(227, "RDS & Databases",
     "Which Amazon Aurora feature allows you to query data across multiple Aurora clusters?",
     [("Aurora Global Database", False),
      ("Aurora Federation Query", True),
      ("Aurora Parallel Query", False),
      ("Aurora Serverless", False)],
     "Aurora Federation Query allows you to run queries across multiple Aurora MySQL clusters and external databases. It enables data integration without requiring data migration or ETL processes.",
     "Aurora Federation Query enables cross-cluster data querying.")

add_q(228, "RDS & Databases",
     "Which cache eviction policy is commonly used when memory is full and older items need to be removed?",
     [("allkeys-lru", True),
      ("volatile-ttl", False),
      ("noeviction", False),
      ("allkeys-random", False)],
     "The allkeys-lru (Least Recently Used) eviction policy removes the least recently used keys first when memory is full. This is the default and most commonly used eviction policy for Redis caches.",
     "LRU eviction removes the least recently used keys when memory is full.")

add_q(229, "RDS & Databases",
     "Which Amazon RDS feature allows you to create a time-stamped copy of your DB instance?",
     [("RDS Snapshot", True),
      ("RDS Read Replica", False),
      ("RDS Multi-AZ", False),
      ("RDS Proxy", False)],
     "RDS Snapshots are point-in-time backups of your DB instance. You can create manual snapshots at any time, and automated snapshots are taken daily during your backup window. Snapshots can be used to restore a new instance.",
     "RDS Snapshots create point-in-time backups of database instances.")

add_q(230, "RDS & Databases",
     "Which DynamoDB feature captures item-level modifications in your table in chronological order?",
     [("DynamoDB Global Tables", False),
      ("DynamoDB Accelerator (DAX)", False),
      ("DynamoDB Streams", True),
      ("DynamoDB TTL", False)],
     "DynamoDB Streams capture item-level modifications in your table in chronological order. Each stream record contains information about the modified item, including the type of modification (insert, modify, delete).",
     "DynamoDB Streams capture item-level modifications in chronological order.")

add_q(231, "RDS & Databases",
     "Which AWS service provides a managed, PostgreSQL-compatible database with advanced extensions?",
     [("Amazon RDS for PostgreSQL", False),
      ("Amazon Aurora PostgreSQL", True),
      ("Amazon Redshift", False),
      ("Amazon Neptune", False)],
     "Aurora PostgreSQL combines the performance and availability of Aurora with PostgreSQL compatibility. It provides faster performance than standard RDS PostgreSQL through its distributed storage architecture.",
     "Aurora PostgreSQL provides high-performance PostgreSQL with Aurora architecture.")

add_q(232, "RDS & Databases",
     "Which caching strategy ensures that the cache and database remain synchronized by writing to both simultaneously?",
     [("Lazy loading", False),
      ("Write-through caching", True),
      ("Cache aside", False),
      ("Write-behind caching", False)],
     "Write-through caching writes data to both the cache and the database simultaneously. This ensures data consistency between the cache and database but adds write latency. It prevents stale data in the cache.",
     "Write-through caching keeps cache and database synchronized.")

add_q(233, "RDS & Databases",
     "Which RDS feature allows you to create a standby in a different AWS Region for disaster recovery?",
     [("RDS Multi-AZ (same Region)", False),
      ("RDS Read Replica in a different Region", True),
      ("RDS Snapshot cross-Region copy", False),
      ("RDS Blue/Green Deployments", False)],
     "Cross-Region Read Replicas provide disaster recovery capability by maintaining a read-only copy of your database in a different Region. If the primary Region fails, you can promote the Read Replica to become the new primary.",
     "Cross-Region Read Replicas enable disaster recovery across Regions.")

add_q(234, "RDS & Databases",
     "Which Amazon Redshift feature allows you to query data directly in S3 without loading it into Redshift?",
     [("Redshift Spectrum", True),
      ("Redshift Federated Query", False),
      ("Redshift Materialized Views", False),
      ("Redshift Concurrency Scaling", False)],
     "Redshift Spectrum allows you to run SQL queries directly against exabytes of data in S3 without needing to load the data into Redshift tables. This enables you to query data in your data lake alongside data in Redshift.",
     "Redshift Spectrum queries data in S3 without loading it.")

add_q(235, "RDS & Databases",
     "Which DynamoDB feature automatically deletes items after a specified time period?",
     [("DynamoDB Streams", False),
      ("DynamoDB TTL (Time to Live)", True),
      ("DynamoDB Lifecycle Policies", False),
      ("DynamoDB Point-in-Time Recovery", False)],
     "DynamoDB TTL automatically deletes items after a specified time period, reducing storage costs and managing data lifecycle. TTL is useful for session data, event logs, and other time-bounded data.",
     "DynamoDB TTL automatically expires items after a specified time.")

add_q(236, "RDS & Databases",
     "Which Amazon RDS backup feature allows you to restore to any point within the retention period?",
     [("Automated Snapshots", False),
      ("Point-in-Time Recovery (PITR)", True),
      ("Manual Snapshots", False),
      ("RDS Blue/Green Deployments", False)],
     "RDS PITR allows you to restore your database instance to any specific point in time within your backup retention period (up to 35 days). It creates a new DB instance with the data from the specified time.",
     "PITR restores database to any point within the retention period.")

add_q(237, "RDS & Databases",
     "Which Amazon ElastiCache feature provides automatic failover for Redis clusters?",
     [("ElastiCache for Memcached with Auto Discovery", False),
      ("ElastiCache for Redis with Multi-AZ", True),
      ("ElastiCache Global Datastore", False),
      ("ElastiCache Replication Groups", False)],
     "ElastiCache for Redis Multi-AZ provides automatic failover by detecting primary node failures and promoting a replica to primary. This ensures high availability with minimal downtime.",
     "Redis Multi-AZ provides automatic failover for cache clusters.")

add_q(238, "RDS & Databases",
     "Which AWS service provides a serverless, auto-scaling relational database?",
     [("Amazon RDS", False),
      ("Amazon Aurora Serverless v2", True),
      ("Amazon DynamoDB", False),
      ("Amazon DocumentDB", False)],
     "Aurora Serverless v2 automatically scales compute capacity up and down based on application demand. It provides the full Aurora experience without managing instances, making it ideal for unpredictable workloads.",
     "Aurora Serverless v2 provides serverless auto-scaling relational database.")

add_q(239, "RDS & Databases",
     "Which type of DynamoDB index must share the same partition key as the table?",
     [("Global Secondary Index", False),
      ("Local Secondary Index", True),
      ("Composite Secondary Index", False),
      ("Sparse Index", False)],
     "Local Secondary Indexes (LSIs) share the same partition key as the table but can have a different sort key. LSIs must be defined at table creation time and are limited to 5 per table.",
     "LSIs share the same partition key as the base table.")

add_q(240, "RDS & Databases",
     "Which feature of Amazon RDS Blue/Green Deployments creates a staging environment that mirrors your production environment?",
     [("Blue/Green deployment creates a copy of the production database in a separate environment", True),
      ("Blue/Green deployment uses read replicas", False),
      ("Blue/Green deployment creates snapshots only", False),
      ("Blue/Green deployment uses Multi-AZ standby", False)],
     "RDS Blue/Green Deployments create a staging environment (green) that synchronously replicates from your production environment (blue). You can test changes in the green environment and switch over with minimal downtime.",
     "Blue/Green Deployments create a staging copy for zero-downtime changes.")

# ============================================================
# IAM & Security (30 questions)
# ============================================================
add_q(241, "IAM & Security",
     "Which IAM entity is best suited for granting cross-account access?",
     [("IAM User with access keys", False),
      ("IAM Role", True),
      ("IAM Group", False),
      ("IAM Policy", False)],
     "IAM roles are designed for cross-account access. The trusting account creates a role with a trust policy that allows the trusted account to assume the role. This provides temporary credentials without sharing long-term access keys.",
     "IAM roles are designed for cross-account access through trust policies.")

add_q(242, "IAM & Security",
     "Which IAM condition key can be used to restrict access based on the IP address of the requester?",
     [("aws:SourceIp", True),
      ("aws:PrincipalOrgID", False),
      ("aws:UserAgent", False),
      ("aws:CurrentTime", False)],
     "The aws:SourceIp condition key matches the IP address of the requester. You can use it to allow or deny access based on the source IP address, which is useful for restricting access to specific networks.",
     "aws:SourceIp restricts access based on the requester's IP address.")

add_q(243, "IAM & Security",
     "Which AWS service provides temporary credentials for federated users who sign in through an external identity provider?",
     [("IAM Roles", False),
      ("AWS STS AssumeRoleWithWebIdentity", True),
      ("IAM Users", False),
      ("AWS Cognito Identity Pools", False)],
     "AWS STS AssumeRoleWithWebIdentity returns temporary security credentials for users who have been authenticated through a web identity provider like Amazon Cognito, Login with Amazon, Facebook, Google, or any OIDC provider.",
     "AssumeRoleWithWebIdentity provides temporary credentials for federated users.")

add_q(244, "IAM & Security",
     "Which S3 bucket policy configuration prevents objects from being uploaded without encryption?",
     [("Using the s3:x-amz-server-side-encryption condition", True),
      ("Using the s3:Versioning condition", False),
      ("Using S3 Object Lock", False),
      ("Using S3 ACLs", False)],
     "You can use the s3:x-amz-server-side-encryption condition in a bucket policy to require that all uploaded objects use server-side encryption. If the condition is not met, the upload is denied.",
     "Bucket policy with s3:x-amz-server-side-encryption enforces encryption on uploads.")

add_q(245, "IAM & Security",
     "Which AWS feature provides centralized management of IAM permissions across multiple AWS accounts?",
     [("AWS IAM", False),
      ("AWS Organizations Service Control Policies (SCPs)", True),
      ("AWS Config Rules", False),
      ("AWS Resource Groups", False)],
     "SCPs are organizational policy types that specify the maximum permissions for member accounts in an organization. They act as guardrails, ensuring accounts stay within the permission boundaries defined by the management account.",
     "SCPs centrally manage permission boundaries across AWS accounts.")

add_q(246, "IAM & Security",
     "Which type of IAM policy is attached directly to an AWS resource like an S3 bucket or SQS queue?",
     [("Identity-based policy", False),
      ("Resource-based policy", True),
      ("Permissions boundary", False),
      ("Service control policy", False)],
     "Resource-based policies (also called bucket policies, queue policies, etc.) are attached to AWS resources. They specify what principals can perform actions on that resource, enabling cross-account access at the resource level.",
     "Resource-based policies are attached to resources like S3 buckets or SQS queues.")

add_q(247, "IAM & Security",
     "Which AWS service provides managed web identity federation with social login providers?",
     [("AWS IAM", False),
      ("AWS STS", False),
      ("Amazon Cognito", True),
      ("AWS Directory Service", False)],
     "Amazon Cognito provides user authentication, authorization, and user management for web and mobile applications. It supports social login providers (Google, Facebook, Amazon, Apple) and enterprise identity providers via SAML and OIDC.",
     "Cognito provides managed web identity federation with social login support.")

add_q(248, "IAM & Security",
     "Which IAM feature rotates access keys automatically on a schedule?",
     [("IAM access key last used", False),
      ("IAM credential report", False),
      ("IAM does not auto-rotate access keys; use AWS Secrets Manager", True),
      ("IAM groups", False)],
     "IAM itself does not automatically rotate access keys. For automatic rotation, use AWS Secrets Manager, which can automatically rotate secrets including database credentials, API keys, and other secrets on a schedule you define.",
     "Use Secrets Manager for automatic credential rotation; IAM does not auto-rotate.")

add_q(249, "IAM & Security",
     "Which KMS feature allows you to control which principals can use a CMK for encryption operations?",
     [("KMS key policy", True),
      ("KMS alias", False),
      ("KMS key rotation", False),
      ("KMS grant", False)],
     "KMS key policies define who can use the CMK and for which operations. They are the primary way to control access to KMS keys, just like IAM policies control access to AWS resources.",
     "KMS key policies control access to CMKs for encryption operations.")

add_q(250, "IAM & Security",
     "Which AWS service provides managed, single sign-on access to AWS accounts and business applications?",
     [("AWS IAM Identity Center (formerly AWS SSO)", True),
      ("AWS Cognito", False),
      ("Amazon Directory Service", False),
      ("AWS STS", False)],
     "AWS IAM Identity Center (formerly AWS SSO) provides managed SSO access to all AWS accounts and business applications. It integrates with existing identity providers like Active Directory, Okta, and Azure AD.",
     "IAM Identity Center provides managed SSO for AWS accounts and applications.")

add_q(251, "IAM & Security",
     "Which S3 feature prevents public access to all S3 buckets and objects at the account level?",
     [("S3 Bucket Policies", False),
      ("S3 Block Public Access", True),
      ("S3 Object Lock", False),
      ("S3 Versioning", False)],
     "S3 Block Public Access provides account-level and bucket-level settings to block public access to S3 resources. It has four individual controls that can be combined, and an 'Block all' option that enables all four controls at once.",
     "Block Public Access prevents S3 buckets from becoming publicly accessible.")

add_q(252, "IAM & Security",
     "Which AWS service detects unauthorized API calls and unauthorized deployments in your AWS environment?",
     [("Amazon GuardDuty", True),
      ("Amazon Inspector", False),
      ("Amazon Macie", False),
      ("AWS Config", False)],
     "Amazon GuardDuty is a threat detection service that monitors for unauthorized API calls, unauthorized deployments, credential misuse, and other malicious behavior across your AWS environment.",
     "GuardDuty detects unauthorized API calls and deployments.")

add_q(253, "IAM & Security",
     "Which encryption option for RDS uses AWS KMS to encrypt data at rest?",
     [("Transparent Data Encryption (TDE)", False),
      ("AWS KMS encryption", True),
      ("Native database encryption", False),
      ("SSL/TLS encryption", False)],
     "RDS encryption using AWS KMS encrypts data at rest for the DB instance, read replicas, snapshots, and logs. It uses the AES-256 encryption algorithm and integrates with AWS KMS for key management.",
     "AWS KMS encryption encrypts RDS data at rest.")

add_q(254, "IAM & Security",
     "Which AWS service provides managed certificate provisioning and renewal for use with CloudFront and ALB?",
     [("AWS KMS", False),
      ("AWS Certificate Manager (ACM)", True),
      ("AWS Secrets Manager", False),
      ("AWS IAM Server Certificates", False)],
     "AWS Certificate Manager (ACM) handles the process of provisioning, managing, and renewing SSL/TLS certificates. ACM certificates can be used with CloudFront distributions, Application Load Balancers, and API Gateway.",
     "ACM manages SSL/TLS certificates for CloudFront and ALB.")

add_q(255, "IAM & Security",
     "Which AWS Config rule type checks whether your AWS resources comply with specific configuration requirements?",
     [("Managed rules", False),
      ("Custom rules", False),
      ("Both managed and custom rules are available", True),
      ("Only managed rules are available", False)],
     "AWS Config provides both managed rules (predefined by AWS for common use cases) and custom rules (defined by you using AWS Lambda functions) to check whether your resources comply with your desired configuration.",
     "Config supports both managed and custom rules for compliance checking.")

add_q(256, "IAM & Security",
     "Which IAM feature generates a report listing all users, groups, roles, and their access keys?",
     [("IAM Credential Report", True),
      ("IAM Access Analyzer", False),
      ("IAM Policy Simulator", False),
      ("CloudTrail", False)],
     "The IAM Credential Report generates a report that lists all users in the account and the status of their credentials, including access keys, MFA devices, and passwords. It helps identify unused credentials and security gaps.",
     "IAM Credential Report lists all users and their credential status.")

add_q(257, "IAM & Security",
     "Which AWS service helps identify resources in your account that are shared with external entities?",
     [("AWS Config", False),
      ("IAM Access Analyzer", True),
      ("AWS CloudTrail", False),
      ("Amazon Inspector", False)],
     "IAM Access Analyzer identifies resources in your organization and accounts (like S3 buckets, IAM roles, Lambda functions) that are shared with external entities. It uses mathematical analysis to determine trust relationships.",
     "Access Analyzer identifies externally shared resources.")

add_q(258, "IAM & Security",
     "Which security best practice recommends never using the root account for daily operations?",
     [("Use the root account only for initial setup and tasks that require root credentials", True),
      ("Use the root account for all operations to simplify access management", False),
      ("There is no restriction on root account usage", False),
      ("Use the root account only for billing", False)],
     "The AWS root account has full, unrestricted access to all resources. Best practice is to create IAM users or roles for daily operations and only use the root account for initial setup, billing, and tasks that specifically require root credentials.",
     "Root account should only be used for tasks requiring root-level access.")

add_q(259, "IAM & Security",
     "Which AWS service provides managed, single sign-on with Active Directory integration?",
     [("Amazon Cognito", False),
      ("AWS IAM Identity Center", False),
      ("AWS Directory Service - AWS Managed Microsoft AD", True),
      ("AWS STS", False)],
     "AWS Managed Microsoft AD provides a managed Active Directory in AWS. It integrates with your on-premises AD, supports Group Policy, and provides Kerberos-based SSO for applications and resources.",
     "AWS Managed Microsoft AD provides Active Directory integration for SSO.")

add_q(260, "IAM & Security",
     "Which type of KMS key is created and managed by AWS for use with specific AWS services?",
     [("Customer managed CMK", False),
      ("AWS managed CMK", True),
      ("AWS owned CMK", False),
      ("Data key", False)],
     "AWS managed CMKs are created and managed by AWS for use with specific services (like s3 for S3 bucket encryption, rds for RDS encryption). You cannot view, manage, or rotate these keys, but you can use them through the associated service.",
     "AWS managed CMKs are created by AWS for specific services.")

add_q(261, "IAM & Security",
     "Which IAM policy evaluation logic is used when both allow and deny statements exist?",
     [("Default deny - an explicit deny always overrides an allow", True),
      ("Explicit allow always wins", False),
      ("The last policy evaluated wins", False),
      ("Allow and deny are evaluated equally", False)],
     "IAM policy evaluation follows a specific order: default deny, then explicit deny (always wins), then explicit allow. If there is no matching allow statement after all policy evaluations, access is implicitly denied.",
     "Explicit deny always overrides allow in IAM policy evaluation.")

add_q(262, "IAM & Security",
     "Which AWS service provides managed, automated cross-region backup for compliance?",
     [("AWS Backup", True),
      ("Amazon S3 Cross-Region Replication", False),
      ("AWS CloudFormation", False),
      ("AWS Systems Manager", False)],
     "AWS Backup is a centralized, fully managed backup service that supports cross-region and cross-account backup copying. It provides automated backup schedules, retention policies, and compliance reporting.",
     "AWS Backup provides automated cross-region backup management.")

add_q(263, "IAM & Security",
     "Which feature of KMS automatically rotates encryption keys on a yearly basis?",
     [("Manual key rotation", False),
      ("Automatic key rotation", True),
      ("Key alias rotation", False),
      ("Data key rotation", False)],
     "KMS automatic key rotation creates new key material for a CMK every year while keeping the same key ID. This maintains the ability to decrypt data encrypted with previous versions of the key.",
     "KMS automatic key rotation creates new key material yearly.")

add_q(264, "IAM & Security",
     "Which Amazon S3 feature provides fine-grained access control using attributes like department or role?",
     [("S3 Bucket Policies with conditions", False),
      ("S3 Access Grants", True),
      ("S3 ACLs", False),
      ("IAM policies", False)],
     "S3 Access Grants provide a secure and scalable way to share S3 data with users and applications using their corporate directory identities. It maps identities to S3 data permissions, simplifying data access management.",
     "S3 Access Grants map corporate identities to S3 data permissions.")

add_q(265, "IAM & Security",
     "Which CloudTrail feature ensures no log records are deleted or modified?",
     [("CloudTrail Log File Validation", True),
      ("CloudTrail Multi-Region Trail", False),
      ("CloudTrail Organization Trail", False),
      ("CloudTrail Data Events", False)],
     "CloudTrail Log File Validation creates a digest file that contains a hash of each log file. You can use this to verify that log files have not been modified or deleted since CloudTrail delivered them.",
     "Log File Validation ensures CloudTrail logs have not been tampered with.")

add_q(266, "IAM & Security",
     "Which AWS service provides a managed WAF that can be deployed at the CloudFront edge?",
     [("AWS Firewall Manager", False),
      ("AWS WAF", True),
      ("AWS Shield", False),
      ("Amazon Inspector", False)],
     "AWS WAF is a web application firewall that helps protect your web applications from common web exploits. When associated with CloudFront, WAF rules are evaluated at edge locations worldwide.",
     "AWS WAF can be deployed at CloudFront edge locations.")

add_q(267, "IAM & Security",
     "Which IAM feature allows you to test whether a policy provides the intended access without actually applying it?",
     [("IAM Policy Simulator", True),
      ("IAM Access Analyzer", False),
      ("IAM Credential Report", False),
      ("AWS Config", False)],
     "The IAM Policy Simulator allows you to test the effects of IAM policies on your resources without actually applying them. You can simulate different scenarios to verify that policies grant or deny the intended permissions.",
     "Policy Simulator tests IAM policies without applying them.")

add_q(268, "IAM & Security",
     "Which AWS feature provides hardware security module (HSM) backing for encryption keys?",
     [("AWS KMS", True),
      ("AWS CloudHSM", False),
      ("Both KMS and CloudHSM use HSMs", False),
      ("Neither service uses HSMs", False)],
     "AWS KMS uses hardware security modules (HSMs) that have been validated under FIPS 140-2 (or FIPS 140-3 for newer modules). AWS CloudHSM provides dedicated HSMs in your VPC for more control over key management.",
     "AWS KMS uses FIPS-validated HSMs for key protection.")

add_q(269, "IAM & Security",
     "Which security practice requires IAM users to change their password every 90 days?",
     [("IAM Password Policy with expiration", True),
      ("IAM Group Policy", False),
      ("AWS Config Rule", False),
      ("SCP Policy", False)],
     "IAM password policies can require users to change their passwords at a specified interval (e.g., every 90 days). You can also set minimum length, require specific character types, and prevent password reuse.",
     "IAM Password Policy with expiration enforces periodic password changes.")

add_q(270, "IAM & Security",
     "Which AWS service provides network-level isolation between compute resources within the same VPC?",
     [("VPC Security Groups", False),
      ("VPC Subnets", True),
      ("NACLs", False),
      ("Route Tables", False)],
     "VPC subnets provide network-level isolation by segmenting a VPC into one or more subnets. Each subnet resides in one AZ and has its own route table, providing isolation of resources at the network level.",
     "VPC Subnets provide network-level isolation within a VPC.")

# ============================================================
# Monitoring & Logging (30 questions)
# ============================================================
add_q(271, "Monitoring & Logging",
     "Which AWS service provides customizable dashboards and alarms for monitoring AWS resources?",
     [("AWS CloudTrail", False),
      ("Amazon CloudWatch", True),
      ("AWS Config", False),
      ("AWS X-Ray", False)],
     "Amazon CloudWatch provides monitoring and observability for AWS resources and applications. It collects metrics, logs, and events, and provides dashboards, alarms, and automated actions based on metric thresholds.",
     "CloudWatch provides monitoring dashboards, metrics, and alarms.")

add_q(272, "Monitoring & Logging",
     "Which CloudWatch feature allows you to visualize metrics and logs on a single dashboard?",
     [("CloudWatch Alarms", False),
      ("CloudWatch Dashboards", True),
      ("CloudWatch Logs Insights", False),
      ("CloudWatch Metrics", False)],
     "CloudWatch Dashboards are customizable home pages that display metrics and alarms from multiple AWS services in a single view. You can create cross-account and cross-Region dashboards for centralized monitoring.",
     "CloudWatch Dashboards visualize metrics and logs on a single view.")

add_q(273, "Monitoring & Logging",
     "Which CloudWatch feature allows you to query and analyze log data using a SQL-like syntax?",
     [("CloudWatch Metrics", False),
      ("CloudWatch Logs Insights", True),
      ("CloudWatch Alarms", False),
      ("CloudWatch Events", False)],
     "CloudWatch Logs Insights enables you to interactively search and analyze log data in CloudWatch Logs using a query language. It helps you quickly answer questions about your applications and resolve operational issues.",
     "Logs Insights queries log data using SQL-like syntax.")

add_q(274, "Monitoring & Logging",
     "Which AWS service provides distributed tracing for microservices to analyze and debug requests?",
     [("Amazon CloudWatch", False),
      ("AWS X-Ray", True),
      ("AWS CloudTrail", False),
      ("Amazon Inspector", False)],
     "AWS X-Ray helps developers analyze and debug distributed applications. It traces requests as they travel through your application, showing how your application components interact and identifying performance bottlenecks.",
     "X-Ray provides distributed tracing for microservices.")

add_q(275, "Monitoring & Logging",
     "Which CloudWatch alarm action automatically stops, terminates, or reboots an EC2 instance?",
     [("Auto Scaling Action", False),
      ("EC2 Action", True),
      ("SNS Notification", False),
      ("Lambda Function", False)],
     "CloudWatch alarms can perform EC2 actions like stop, terminate, or reboot when an alarm state is triggered. This enables automated remediation, such as terminating an unresponsive instance or rebooting one with high memory usage.",
     "CloudWatch alarm EC2 actions can stop, terminate, or reboot instances.")

add_q(276, "Monitoring & Logging",
     "Which AWS service records API calls made to your AWS account for compliance auditing?",
     [("Amazon CloudWatch", False),
      ("AWS CloudTrail", True),
      ("AWS Config", False),
      ("Amazon Inspector", False)],
     "AWS CloudTrail records API calls made on your account and delivers log files to an S3 bucket. It provides visibility into user activity, API changes, and resource modifications for security analysis and compliance.",
     "CloudTrail records all API calls for compliance auditing.")

add_q(277, "Monitoring & Logging",
     "Which CloudWatch feature automatically responds to changes in metric values by scaling resources?",
     [("CloudWatch Alarms with Auto Scaling", True),
      ("CloudWatch Dashboards", False),
      ("CloudWatch Logs", False),
      ("CloudWatch Events", False)],
     "CloudWatch Alarms can trigger Auto Scaling policies when metric thresholds are crossed. This enables automatic scaling of EC2 instances, ECS tasks, or other resources based on CloudWatch metrics.",
     "CloudWatch Alarms trigger Auto Scaling actions based on metric thresholds.")

add_q(278, "Monitoring & Logging",
     "Which CloudWatch Logs feature exports log data to S3 for long-term archival?",
     [("CloudWatch Logs Export", True),
      ("CloudWatch Logs Insights", False),
      ("CloudWatch Logs Metrics", False),
      ("CloudWatch Logs Subscriptions", False)],
     "CloudWatch Logs can export log data to S3 for long-term archival, analysis with Athena, or processing with EMR. This is useful for compliance requirements that mandate log retention beyond the CloudWatch Logs default period.",
     "CloudWatch Logs exports to S3 for long-term archival.")

add_q(279, "Monitoring & Logging",
     "Which AWS service provides a managed service for collecting, storing, and accessing log data from various sources?",
     [("Amazon S3", False),
      ("Amazon CloudWatch Logs", True),
      ("Amazon Redshift", False),
      ("Amazon Kinesis", False)],
     "Amazon CloudWatch Logs provides a centralized log management service for AWS resources, applications, and on-premises servers. It supports log collection, storage, search, filtering, and export capabilities.",
     "CloudWatch Logs is a centralized log management service.")

add_q(280, "Monitoring & Logging",
     "Which AWS Config feature records configuration changes for your AWS resources?",
     [("AWS Config Rules", False),
      ("AWS Config Recorders", True),
      ("AWS Config Conformance Packs", False),
      ("AWS Config Aggregators", False)],
     "AWS Config Recorders capture configuration changes for supported AWS resources. They record details like resource type, resource ID, configuration, and relationships, providing a configuration history for compliance and auditing.",
     "Config Recorders capture configuration changes for AWS resources.")

add_q(281, "Monitoring & Logging",
     "Which X-Ray feature helps identify performance bottlenecks in distributed applications?",
     [("Service Maps", True),
      ("Traces", False),
      ("Segments", False),
      ("Annotations", False)],
     "X-Ray Service Maps provide a visual representation of your application's architecture, showing the connections between components and their health. Color-coded indicators highlight performance issues and errors.",
     "X-Ray Service Maps visualize application architecture and performance issues.")

add_q(282, "Monitoring & Logging",
     "Which CloudWatch metric statistic calculates the number of metric data points above a threshold?",
     [("Average", False),
      ("Sum", False),
      ("p99", False),
      ("Anomaly Detection", True)],
     "CloudWatch Anomaly Detection uses machine learning to continuously analyze metric data and automatically determine what is normal. It detects unusual behavior and creates a band around expected values to identify anomalies.",
     "Anomaly Detection uses ML to identify unusual metric behavior.")

add_q(283, "Monitoring & Logging",
     "Which AWS service provides a centralized location to manage operational events and incidents?",
     [("Amazon CloudWatch", False),
      ("AWS Systems Manager Incident Manager", True),
      ("AWS CloudTrail", False),
      ("AWS Config", False)],
     "AWS Systems Manager Incident Manager provides a central location to prepare for, track, and resolve operational events (incidents). It offers runbooks, escalation policies, and integration with ChatOps tools.",
     "Incident Manager centralizes operational incident management.")

add_q(284, "Monitoring & Logging",
     "Which CloudWatch Logs feature sends log data to a Lambda function for custom processing?",
     [("Subscription Filters", True),
      ("Metric Filters", False),
      ("Export to S3", False),
      ("Logs Insights", False)],
     "CloudWatch Logs Subscription Filters send log data to a Lambda function, Kinesis stream, or Kinesis Data Firehose for custom processing in near real-time. This enables custom log analysis, alerting, and archiving.",
     "Subscription Filters stream log data to Lambda for custom processing.")

add_q(285, "Monitoring & Logging",
     "Which AWS CloudTrail data event type records S3 object-level API calls?",
     [("Management events", False),
      ("Data events", True),
      ("Insight events", False),
      ("CloudWatch events", False)],
     "CloudTrail Data events record API activity on resources (like S3 object-level API calls or Lambda function invocations). By default, data events are not logged and must be explicitly configured for specific resources.",
     "Data events record S3 object-level and Lambda function-level API calls.")

add_q(286, "Monitoring & Logging",
     "Which CloudWatch feature aggregates metrics across multiple accounts and Regions?",
     [("CloudWatch Cross-Account Observability", True),
      ("CloudWatch Dashboards", False),
      ("CloudWatch Alarms", False),
      ("CloudWatch Namespaces", False)],
     "CloudWatch Cross-Account Observability allows you to monitor and troubleshoot applications that span multiple accounts and Regions. It uses CloudWatch Observability Access Manager to share metrics, logs, and traces.",
     "Cross-Account Observability aggregates metrics across accounts and Regions.")

add_q(287, "Monitoring & Logging",
     "Which AWS service provides automated reasoning to prove that your IAM policies enforce least privilege?",
     [("IAM Access Analyzer", True),
      ("AWS Config", False),
      ("AWS CloudTrail", False),
      ("Amazon GuardDuty", False)],
     "IAM Access Analyzer uses automated reasoning to analyze your IAM policies and determine if they follow the principle of least privilege. It generates findings for permissions that grant more access than needed.",
     "Access Analyzer uses automated reasoning to verify least privilege.")

add_q(288, "Monitoring & Logging",
     "Which CloudWatch alarm state triggers when a metric breaches a threshold for a specified number of periods?",
     [("OK state", False),
      ("ALARM state", True),
      ("INSUFFICIENT_DATA state", False),
      ("ERROR state", False)],
     "A CloudWatch alarm enters the ALARM state when the metric breaches the defined threshold for the specified number of evaluation periods. Actions configured for the ALARM state (like SNS notifications or Auto Scaling) are then triggered.",
     "CloudWatch alarm ALARM state triggers when threshold is breached.")

add_q(289, "Monitoring & Logging",
     "Which AWS Config feature groups multiple AWS Config rules into a single package for compliance assessment?",
     [("Config Rules", False),
      ("Config Conformance Packs", True),
      ("Config Aggregators", False),
      ("Config Advanced Queries", False)],
     "AWS Config Conformance Packs are collections of AWS Config rules and remediation actions that can be deployed as a single unit. They provide a simplified way to manage compliance across multiple accounts and Regions.",
     "Conformance Packs group Config rules for bulk compliance management.")

add_q(290, "Monitoring & Logging",
     "Which CloudWatch Logs feature creates custom metrics from log data patterns?",
     [("Metric Filters", True),
      ("Subscription Filters", False),
      ("Logs Insights", False),
      ("Log Groups", False)],
     "CloudWatch Logs Metric Filters extract metric values from log events based on filter patterns. You can then create CloudWatch alarms on these metrics to trigger notifications or actions when specific patterns appear in logs.",
     "Metric Filters create custom metrics from log data patterns.")

add_q(291, "Monitoring & Logging",
     "Which AWS service provides a centralized, near real-time stream of events describing changes in your AWS resources?",
     [("Amazon CloudWatch Events (EventBridge)", True),
      ("AWS CloudTrail", False),
      ("AWS Config", False),
      ("Amazon SNS", False)],
     "Amazon EventBridge (formerly CloudWatch Events) delivers a near real-time stream of system events that describe changes in AWS resources. You can create rules to match events and route them to targets like Lambda, SNS, or Step Functions.",
     "EventBridge provides a real-time stream of AWS resource change events.")

add_q(292, "Monitoring & Logging",
     "Which CloudWatch metric statistic represents the 99th percentile of latency?",
     [("Average", False),
      ("Maximum", False),
      ("p99", True),
      ("SampleCount", False)],
     "The p99 statistic shows the 99th percentile value, meaning 99% of requests had latency at or below this value. This is important for understanding tail latency and ensuring a good user experience for nearly all users.",
     "p99 shows the 99th percentile of latency values.")

add_q(293, "Monitoring & Logging",
     "Which X-Ray concept represents the entire end-to-end journey of a request through your application?",
     [("Trace", True),
      ("Segment", False),
      ("Subsegment", False),
      ("Sampling rule", False)],
     "A trace in X-Ray represents the complete journey of a request through your application. It consists of segments (one per service) and subsegments (for specific operations), providing a complete picture of the request path and timing.",
     "A Trace represents the complete end-to-end request journey.")

add_q(294, "Monitoring & Logging",
     "Which AWS Config feature allows you to query resource configurations using SQL-like syntax?",
     [("Config Rules", False),
      ("Config Advanced Queries", True),
      ("Config Conformance Packs", False),
      ("Config Recorders", False),
      ("Config Advanced Queries enable SQL-like queries over resource configurations", False)],
     "Config Advanced Queries allow you to query aggregated resource configuration data across accounts and Regions using SQL-like syntax. This makes it easier to search and analyze your resource configurations at scale.",
     "Config Advanced Queries use SQL-like syntax to query resource configurations.")

add_q(295, "Monitoring & Logging",
     "Which CloudWatch feature uses machine learning to detect anomalies in metrics automatically?",
     [("CloudWatch Alarms", False),
      ("CloudWatch Anomaly Detection", True),
      ("CloudWatch Contributor Insights", False),
      ("CloudWatch Canaries", False)],
     "CloudWatch Anomaly Detection applies machine learning algorithms to your metrics to automatically determine normal baselines and detect unusual behavior. It generates an expected band and alerts when metrics go outside this band.",
     "Anomaly Detection uses ML to detect unusual metric behavior.")

add_q(296, "Monitoring & Logging",
     "Which AWS service provides end-to-end observability by collecting metrics, logs, and traces together?",
     [("Amazon CloudWatch", True),
      ("AWS X-Ray", False),
      ("AWS CloudTrail", False),
      ("AWS Config", False)],
     "Amazon CloudWatch provides the most comprehensive observability by collecting metrics, logs, and traces. Combined with CloudWatch Embedded Metric Format and ServiceLens, it offers unified observability for applications.",
     "CloudWatch provides comprehensive metrics, logs, and traces collection.")

add_q(297, "Monitoring & Logging",
     "Which CloudTrail feature generates findings about unusual API activity?",
     [("CloudTrail Insights", True),
      ("CloudTrail Data Events", False),
      ("CloudTrail Management Events", False),
      ("CloudTrail Log Validation", False)],
     "CloudTrail Insights continuously analyzes write management events from your AWS account and uses machine learning to identify unusual API call rates. It generates insights when API activity deviates from the established baseline.",
     "CloudTrail Insights detects unusual API activity patterns using ML.")

add_q(298, "Monitoring & Logging",
     "Which CloudWatch feature monitors your API endpoints, websites, and web applications for availability and latency?",
     [("CloudWatch Synthetics Canaries", True),
      ("CloudWatch RUM", False),
      ("CloudWatch Alarms", False),
      ("CloudWatch Logs", False)],
     "CloudWatch Synthetics Canaries are scripts that monitor your endpoints and APIs from the outside, simulating user behavior to detect issues before real users do. They provide availability, latency, and performance metrics.",
     "Synthetics Canaries monitor endpoints and APIs for availability and performance.")

add_q(299, "Monitoring & Logging",
     "Which CloudWatch feature captures user-facing performance data from web applications in real-time?",
     [("CloudWatch RUM (Real User Monitoring)", True),
      ("CloudWatch Synthetics", False),
      ("CloudWatch Logs", False),
      ("AWS X-Ray", False)],
     "CloudWatch RUM collects telemetry data about the performance of your web applications from real user sessions. It captures page load times, JavaScript errors, and user interactions to help identify and resolve client-side issues.",
     "RUM captures real user performance data from web applications.")

add_q(300, "Monitoring & Logging",
     "Which AWS service provides operational insights by correlating metrics, logs, and traces across your application?",
     [("Amazon CloudWatch ServiceLens", True),
      ("AWS X-Ray", False),
      ("Amazon Inspector", False),
      ("AWS Config", False)],
     "CloudWatch ServiceLens connects traces, metrics, and logs from your application to provide a complete view of its health and performance. It integrates X-Ray traces with CloudWatch metrics and logs for unified observability.",
     "ServiceLens correlates metrics, logs, and traces for unified observability.")

# Write the JSON
with open(r'C:\Users\haro\.openclaw\workspace\aws-saa-study\src\data\aws-saa-exam.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, indent=2, ensure_ascii=False)

print(f"Generated {len(questions)} questions")
