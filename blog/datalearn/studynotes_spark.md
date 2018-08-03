# Apache Spark
## Download
https://spark.apache.org/downloads.html
### Install
http://spark.apache.org/docs/latest/
No real clue, just extract the tar and see the README
> tar -xvzf spark-2.3.1-bin-hadoop2.7.tgz -C ~/devtools/
Link for convenience:
> ln -s spark-2.3.1-bin-hadoop2.7.tgz ~/devtools/spark
## Tutorials
### Vendor Tutorial
Follow the quick-start.html ; the infoq one is basically just an amalgamation of 'installation' and 'quick-start.html'

https://spark.apache.org/
???
https://spark.apache.org/examples.html
simple high-level overview

https://spark.apache.org/docs/latest/quick-start.html
more complete
use Dataset (SQL Programming Guide) instead of RDD 

### Third Party Tutorial
https://www.infoq.com/articles/apache-spark-introduction
More linear than piecing together the official docs

# worklog
# worklog - tutorial
>>> tf=spark.read.text("README.md")
2018-08-02 17:25:35 WARN  ObjectStore:568 - Failed to get database global_temp, returning NoSuchObjectException
=> various blogs list this error, don't seem to be worried about it
src: https://medium.com/@shwetastha1/getting-started-with-spark-and-scala-7b422b143af
src: https://github.com/jaceklaskowski/mastering-apache-spark-book/blob/master/spark-shell.adoc

good:
>>> tf.count()
103

>>> linesWithSpark = tf.filter( tf.value.contains("Spark"))
>>> linesWithSpark.count()
20

"More on Dataset Operations"
This first maps a line to an integer value and aliases it as “numWords”, creating a new DataFrame.
'agg' is called on that DataFrame to find the largest word count.
The arguments to select and agg are both Column, we can use df.colName to get a column from a DataFrame.
We can also import pyspark.sql.functions, which provides a lot of convenient functions to build a new Column from an old one.
>>> tf.select(size(split(tf.value, "\s+")).name("numWords")).agg(max(col("numWords"))).collect()
[Row(max(numWords)=22)]

"MapReduce"
>>> wc = tf.select(explode(split(tf.value,"\s+")).alias("word")).groupBy("word").count()
not the complete output:
>>> wc.collect()
[Row(word='online', count=1), Row(word='graphs', count=1), Row(word='["Parallel', count=1), Row(word='["Building', count=1), Row(word='thread', count=1), Row(word='documentation', count=3), Row(word='command,', count=2), Row(word='abbreviated', count=1), ... ]

"Caching"
nothing to report



# worklog - installation and run
## Run
This is where VMs, containers, etc are useful.
spark incompatible with java versions >8

Fortunately, this machine only used for one thing at a time.

errors:
1) Unable to load native-hadoop library for your platform...
2) 

# resolving '1'
$ env JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/ bin/spark-shell 
2018-07-31 21:47:33 WARN  Utils:66 - Your hostname, myuser-host resolves to a loopback address: 192.xxx.xxx.xxx; using 192.xxx.xxx.xxx instead (on interface enp2s0)
2018-07-31 21:47:33 WARN  Utils:66 - Set SPARK_LOCAL_IP if you need to bind to another address
2018-07-31 21:47:34 WARN  NativeCodeLoader:62 - Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).

# suddenly it works
$ env JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/ bin/spark-shell 
2018-07-31 22:11:45 WARN  Utils:66 - Your hostname, myuser-host resolves to a loopback address: 192.xxx.xxx.xxx; using 192.xxx.xxx.xxx instead (on interface enp2s0)
2018-07-31 22:11:45 WARN  Utils:66 - Set SPARK_LOCAL_IP if you need to bind to another address
2018-07-31 22:11:46 WARN  NativeCodeLoader:62 - Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
Spark context Web UI available at http://192.xxx.xxx.xxx:port
Spark context available as 'sc' (master = local[*], app id = local-1533093129093).
Spark session available as 'spark'.
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /___/ .__/\_,_/_/ /_/\_\   version 2.3.1
      /_/
         
Using Scala version 2.11.8 (OpenJDK 64-Bit Server VM, Java 1.8.0_171)
Type in expressions to have them evaluated.
Type :help for more information.

scala> 
scala> sc.version
res0: String = 2.3.1                                                                                           
                                                                                                               
scala> sc.appName
res1: String = Spark shell

## workaround:
vim bin/spark-shell
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
=> ok, but hacky

More correct is to edit spark-env.sh
src: https://spark.apache.org/docs/latest/configuration.html#environment-variables
src: https://stackoverflow.com/a/40022657

cp conf/spark-env.sh{.template,}
vim conf/spark-env.sh
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64

# python working as well
$ ./bin/pyspark 
Python 3.6.0 |Continuum Analytics, Inc.| (default, Dec 23 2016, 12:22:00) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)] on linux
Type "help", "copyright", "credits" or "license" for more information.
2018-07-31 22:14:47 WARN  Utils:66 - Your hostname, myuser-host resolves to a loopback address: 192.xxx.xxx.xxx; using 192.xxx.xxx.xxx instead (on interface enp2s0)
2018-07-31 22:14:47 WARN  Utils:66 - Set SPARK_LOCAL_IP if you need to bind to another address
WARNING: An illegal reflective access operation has occurred
WARNING: Illegal reflective access by org.apache.hadoop.security.authentication.util.KerberosUtil (file:/home/myuser/devtools/spark-2.3.1-bin-hadoop2.7/jars/hadoop-auth-2.7.3.jar) to method sun.security.krb5.Config.getInstance()
WARNING: Please consider reporting this to the maintainers of org.apache.hadoop.security.authentication.util.KerberosUtil
WARNING: Use --illegal-access=warn to enable warnings of further illegal reflective access operations
WARNING: All illegal access operations will be denied in a future release
2018-07-31 22:14:48 WARN  NativeCodeLoader:62 - Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /__ / .__/\_,_/_/ /_/\_\   version 2.3.1
      /_/

Using Python version 3.6.0 (default, Dec 23 2016 12:22:00)
SparkSession available as 'spark'.
>>> 

# and some of the examples
src: https://spark.apache.org/docs/latest/#running-the-examples-and-shell



# ok, figure out why no working
# compare against hadoop-less install
$ tar -xvzf ~/Downloads/spark-2.3.1-bin-without-hadoop.tgz -C ~/devtools/
