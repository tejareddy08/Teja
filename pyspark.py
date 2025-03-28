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

#spark session initiation- (driver program/main program ) -- this will be initiated by driver node/master node-- it is the entry point to spark environment
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("example").getOrCreate()

#--reading data 
df = spark.read.csv("path")
df = spark.read.format("csv or text or parquet orjson").option("inferschema", True).opation("header", True).load("path")

#--inferschema -- assigns datatype to the column based on column values
#--header -- aligns first row of the dataset as a header

#Assigning schema
#--schema -- defining a structure - column names and its corresponding datatypes
#method 1 of creating dataframe with schema
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

data = [(1,'abc'),(2,'def')]
schema = StructType([StructField("id", IntegerType(), True),
                     StructField("name", StringType(), True)]

df = spark.createDataFrame(data, schema)
df.display()

#method 2 of infering schema and creating dataframe 
df = spark.read.format("csv or text or parquet orjson").option("inferschema", True).opation("header", True).load("path")

#method 3 
df = df.select(col("id").cast("float")) #-- cast operator will convert the datatype of a column

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

#selecting columns 

df = df.select("*") #--select * from table 
df = df.select("col1", "col2") #--select col1, col2 from table
df = df.select(col("col1").alias("id") #--select col1 as id from table --alias is used tochange names or to give names

#filtering
df = df.filter(col("col1") == value) #select * from table where col1 = value
df = df.filter((col("col1") == value) and (col("col2") >= value)) #select * from table where col1 = value and col2 >= value
df = df.filter((col("col1").between(valu1, value2))) #select *  from table where col1 between a and b 
df = df.filter(col("col1").isin(value, value2)) # select * from table where col1 in (value, value2)
df = df.filter(col("col1").isnull()) #select * from table where col is null
df = df.filter(col("col1").like("Tej%")) #select * from table where col like 'Tej%'

#groupby
df = df.groupBy(col("col1").sum("col2") #select col1 , sum(col2 ) from table group by col1

#orderby

df = df.orderBy(col("col1")) #select * from table order by col1 
from pyspark.sql.functions import col, desc
df = df.orderBy(col("col1").desc()) #select * from table order by col1 desc

#joins
#inner join
#outer join
#left join
#right join
#broadcast join       

df = df.join(df2,'common col','inner') 
df = df.join(df2,'common col','left') 

#broadcast join
if we have one smaller data frame and a larger data frame we braodcast smaller dataframe among all worker nodes so that there wont be shuffling to perform join operation 
and hence will increase the performance
 we need to import first
 from pyspark.sql.functions import broadcast
df_broadcast = df.join(broadcast(df2, 'common col', 'inner')

#window functions
#rank, denserank,row number, lead , lag, sum, avg,count, min, max .
select col1, denserank() over ( order by col2) as dr from table 
from pyspark.sql import window
df_window = window.orderBy(col('colname').desc())
df_1 = df.withColumn('dr' , df.dense_rank(). over(df_window))

df_window = window.orderBy(col('colname').desc())
df_1 = df.withColumn('dr' , df.row_number(). over(df_window))

df_window = window.orderBy(col('colname').desc())
df_1 = df.withColumn('dr' , df.rank(). over(df_window))





                       




                










