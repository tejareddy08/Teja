Bigdata -- greater than 10 TB of data is known as bigdata
Bigdata Analytics -- to perform computation on huge volumns of data
characterstics -- 4v's 
  --Volume
  --Velocity
  --veracity 
  --value

Hadoop-- Bigadata analytics computation tool 
Hadoop Environment --
   --HDFS - to store data
   --MAP REDUCE - to process the data  -- replaced by spark engine - in later versions spark is colaborated with python and formed as pyspark
   --YARN - resource manager

How HDFS STORE HUGE AMAOUNTS OF DATA AND PROCESS HUGE AMOUNTS OF DATA?

--with the help of distributive network
--it has a master-slave(virtual machines/ instance) architecture
--master node - primary node / namenode/ driver node -- holds metadata of the worker nodes
--slave node - worker node  -- executes actual task

--cluster - group of nodes / group of instances
--instance - part of cluster- worker node

how data will store in hdfs?

s1- client submits the job
s2- master node/driver node seggregates the data and distributes among worker nodes
s3- actual task will be executed in worker nodes

--each worker node can hold 128 mb of data
--for every 10secs worker nodes will send heartbeat signals to driver node of exceeds 10 secs driver nodes assumes worker node to be died and creates another worker node with the duplicates
--each worker node have 3 duplicates also called as replication factor --- falut tolerance mechanism
--default replication factor - 3

--hadoop v1 - single point failure -- name node failure
--hadoop v2 - overcomed usimg secondary name node concept

--secondary name node comes into play whenever the primary name node fails











  
