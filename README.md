# FIFA-2022-Analysis-Using-Hadoop-Framework-Big-Data-Project

## Babu Banarasi Das University

**Subject:** Big Data Fundmental<br>
**Submitted To:** Mr. Vikash (IBM) <br>
**Submitted By:**  
- Krishna Verma (1240258236)  
- Devansh Gupta (1240258159)  
- Divyanshu Sharma (1240258172)  
- Dipali Singh (1240258167)  

**Section:** BCADS-23  

---

## Project Overview

This project implements a complete **Big Data pipeline** using the Hadoop ecosystem to analyze FIFA 22 player data. The pipeline calculates the **average overall rating by nationality** across 16,000+ players, using Hadoop MapReduce for distributed processing and Hive for analytical querying.

---

## Architecture

```
Raw Dataset (CSV) → HDFS → MapReduce Processing → Processed Data → Hive Analysis → Insights
```

---

## Dataset

**File:** `FIFA22_official_data.csv`  
**Source:** FIFA 22 Official Player Data  
**Size:** 16,710 players (official FIFA 22 dataset)  

**Columns Used:**
| Column | Description |
|--------|-------------|
| ID | Unique player ID |
| Name | Player name |
| Nationality | Player's country |
| Position | Playing position (ST, CM, GK, etc.) |
| Overall | Overall rating (0–99) |
| Potential | Potential rating |
| Age | Player age |
| Club | Current club |
| Value | Market value |
| Wage | Weekly wage |

---

## Tools & Technologies

| Tool | Purpose |
|------|---------|
| Hadoop HDFS | Distributed file storage |
| MapReduce (Python) | Distributed data processing |
| Hive | SQL-like data analysis |
| Linux Terminal | Command execution |
| Python | Mapper and Reducer scripts |
| Cloudera QuickStart VM | Hadoop environment |

---

## Files in Repository

```
├── mapper.py                  # MapReduce Mapper - extracts nationality & overall rating
├── reducer.py                 # MapReduce Reducer - calculates average rating per nationality
├── FIFA22_official_data.csv   # Official FIFA 22 dataset (16,710 players)
├── Project-Report.pdf         # Full project report
└── README.md                  # This file
```

---

## How to Run

### Step 1: Upload dataset to HDFS
```bash
hdfs dfs -mkdir /user/cloudera/krishna
hdfs dfs -mkdir /user/cloudera/krishna/fifa
hdfs dfs -put FIFA22_official_data.csv /user/cloudera/krishna/fifa
```

### Step 2: Make scripts executable
```bash
chmod +x mapper.py reducer.py
```

### Step 3: Local test
```bash
cat FIFA22_official_data.csv | python mapper.py | sort | python reducer.py
```

### Step 4: Run Hadoop Streaming Job
```bash
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar -files mapper.py,reducer.py -input /user/cloudera/krishna/fifa/FIFA22_official_data.csv -output /user/cloudera/krishna/fifa/output -mapper "python mapper.py" -reducer "python reducer.py"
```

### Step 5: View output
```bash
hdfs dfs -cat /user/cloudera/krishna/fifa/output/part-00000
```

### Step 6: Hive Analysis
```sql
-- Create table
CREATE TABLE fifa_avg (
  nationality STRING,
  avg_overall FLOAT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t';

-- Load data
LOAD DATA INPATH '/user/cloudera/krishna/fifa/output' INTO TABLE fifa_avg;

-- View all results
SELECT * FROM fifa_avg;

-- Top nationalities by average overall rating
SELECT * FROM fifa_avg ORDER BY av_overall DESC;

-- Top 5 nationalities
SELECT * FROM fifa_avg ORDER BY av_overall DESC LIMIT 5;
```

---

## Sample Output

| Nationality | Avg Overall |
|-------------|------------|
| Argentina | 93.00 |
| Poland | 92.00 |
| Brazil | 91.00 |
| Belgium | 90.50 |
| Egypt | 90.00 |

---

## Use of Generative AI

Generative AI was used to assist in code generation, debugging MapReduce scripts, writing Hive queries, and understanding Big Data concepts. All AI-generated code was manually tested and verified before execution.

---

## Conclusion

A complete Big Data pipeline was successfully implemented using the Hadoop ecosystem. The FIFA 22 dataset was stored in HDFS, processed via MapReduce to compute average overall ratings by nationality, and analyzed using Hive to extract top-performing nations. The project demonstrates distributed data processing on a real-world sports dataset.
