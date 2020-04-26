# Greenest Part

#### AIM: To calculate the areas in bangalore with area covered in greenery covered over 75%

### Preprocessing:

* Install opencv using the command:
    ```
    sudo apt install python3-opencv 
    ```
    Install numpy using the command: 
    ```
    pip3 install numpy 
    ```
* Login into <b><i>username</i></b> using your password.
  
* Clone this repository and copy it into a folder of your choice: 
    * In this case: ```ccbd_3```

    ![Image Not Loaded](./assets/2.png)

* Run the command below to produce  <i>data.txt</i>
    ```python3 cv_green.py```


### Steps to run Map-Reduce Job:

* Install Hadoop on Ubuntu using the guide [here](https://www.youtube.com/watch?v=ieeCyhQ2PPM)
  
* Once the installation is complete, you will have two users on your system, <b><i>username</i></b> and hadoopusr.  
  
* Login into <b><i>username</i></b> using your password.
  
* Open Terminal in the user: <b><i>username</i></b>

* Use  the following command to login to the hadoopusr and then ssh into localhost:
    ```
    su - hadoopusr
    ssh localhost
    ```
    ![Image Not Loaded](./assets/1.png)

* Enter password on prompt

* Run the following command to cd into the folder:
    ```cd /home/username/ccbd_3```

* To start all nodes:
    ```
    start-all.sh
    ```

* To check whether all nodes are running, use the ```jps``` command. The output should look similar to the image below.
    ![Image Not Loaded](./assets/3.png)

* To make a folder in file system on hadoop, use the command below:
    ```
    hadoop fs -mkdir /datamr
    ```
* To copy data.txt from local system to hadoop file system , use the command below:
    ```
    hadoop fs -put /home/username/ccbd_3/data.txt /datamr
    ```
    ![Image Not Loaded](./assets/4.png)
* To confirm whether its done or not, use the following command
    ```
    hadoop fs -ls /datamr
    ```
* The output of this command should look something like this.

* To run the task:
    ```
    hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.0.jar -file mapper.py -mapper mapper.py -file reducer.py -reducer reducer.py -input /datamr/* -output /datamr-output
    ```
    * You can use the following flag to define the number  of reduce tasks explicitly: 
        ```-D mapred.reduce.tasks=<number-of-tasks>```
    ![Image Not Loaded](./assets/5.png)
    ![Image Not Loaded](./assets/8.png)

* Use the following command to access the output:
    ```hadoop fs -text /datamr-output/part-*```
    ![Image Not Loaded](./assets/9.png)

* Visit ```localhost:50070/explorer.html/user/hadoopusr``` to view the job result, the result should look similar to the image below.
    ![Image Not Loaded](./assets/10.png)
* Click on ```data-output``` and then click on ```part-00000```
    ![Image Not Loaded](./assets/11.png)
* Press Download to fetch a copy of the result of the map-reduce job 

* Open the file to view the result.
    ![Image Not Loaded](./assets/12.png)

##### Note: File structure and port numbers may vary depending on the installation method.

##### Useful Commads: 

* Hadoop:
    * Start all nodes: ```start-all/sh```
    * Stop all nodes: ```stop-all.sh```
    * Format Namenode: ```hdfs namenode -format```
    * Java Virtual Machine Process Status Tool: ```jps```


* HDFS:
    * List all Directories and Files:
        ```hadoop dfs -ls /path/to/directory```
    * To make a folder in HDFS:
        ```hadoop fs -mkdir /path/to/folder```
    * To copy a folder from local system to HDFS:
        ```hadoop fs put /path/to/local/directory /path/to/hdfs/directory```
    * To delete a directory in HDFS:
        ```hadoop fs -rm -r /path/to/directory```
    * To view result of a Job:
        ```hadoop fs -text /path/to/output/part-*```

### Explaination: 
// TODO