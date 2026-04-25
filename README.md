# 🧠 Deep Work Analytics: Big Data Project

## ❔ Problem Statement
Students often confuse total hours spent at a desk with actual productivity. This project analyzes the correlation between digital habits (doomscrolling), sleep duration, and mental fatigue to determine their impact on deep work capacity. The objective is to identify how high social media consumption and poor sleep lead to severe mental fatigue.

## 📜 Dataset Description
A synthetic dataset of 5,000 records containing student productivity and digital health metrics. 
Columns include: 
~ UserID, 
~ Academic_Major, 
~ Deep_Work_Hours, 
~ Doomscrolling_Hours, 
~ Sleep_Duration, 
~ Reported_Stress_Level, and 
~ Mental_Fatigue_Score.

## ⚙ Steps to Run
1. Start Cloudera VM and open the terminal.
2. Create an input directory in HDFS: `hdfs dfs -mkdir /input`
3. Upload the dataset: `hdfs dfs -put dataset.csv /input/`
4. Execute the MapReduce job using Hadoop Streaming:
   `hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar -file Mapper.py -mapper "python Mapper.py" -file Reducer.py -reducer "python Reducer.py" -input /input/dataset.csv -output /output`
5. View output: `hdfs dfs -cat /output/part-00000`
6. Open Hive (`hive`) and create the table:
   `CREATE TABLE fatigue_analytics (Mental_Fatigue_Score STRING, Avg_Doomscrolling_Hours FLOAT) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t';`
7. Load data: `LOAD DATA INPATH '/output/part-00000' INTO TABLE fatigue_analytics;`
8. Query results: `SELECT * FROM fatigue_analytics ORDER BY Avg_Doomscrolling_Hours DESC;`

## 📄 Sample Output
Mental_Fatigue_Score    Avg_Doomscrolling_Hours
Severe                  4.74
Moderate                3.93
Low                     3.0

## 💻 Technologies Used
* Cloudera Distribution
* Hadoop Distributed File System (HDFS)
* MapReduce (Hadoop Streaming with Python)
* Apache Hive
* Generative AI (Code Generation & Debugging)
