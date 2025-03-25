--spark + python -- pyspark
--inmemory computation engine -- workernode will store data in ram memory cache so that it dont have to be fetch every time from hdfs -4min
--mapreduce -- workernode have to fetch data every time from hdfs  -- 10mins

pyspark architecture --
 --driver node
   --dag scheduler
 --worker node
   --executor
 --cluster manager

--client submits job to driver node
--driver node initiates spark environment nothing spark session(entry point to spark environment) object 
--dag scheduler creates logical plan and seggregates data and distributes it to worker nodes
--executor in worker nodes executes actual task
--cluster manager -- provide computational environment

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

types of operations - 
--transformations  -- actual operations 
  --narrow transformation -- no shuffling involved, no of partitions/worker nodes before and after will not change . exe -- filter, map, flatmap
  --wide transformation -- shuffling involves, no of partitions before and after will change . exe -- groupby, orderby, join, repartition
--actions -- converts dataframe to normal object

lazy evaluation -- execution of the code starts if and only if an action statement is triggered 
eager evaluation -- execution will start immediately when ever an action statement is triggers df.action, take, count, write

--DAG (direct acyclic graph) -- dag is responsible for creating logical plan and  seggregsting data 
--it also distributes data among worker nodes
--logical plan includes - job, stage and tasks

--job -- one action statement to other action statement
--stage -- part of job -- each wide transformation will create one new stage 
--task -- no .of partitions = no.of tasks. default partitions = 200

--------------------------------------------------------------------------------------------------------------------------------------------------------------------





