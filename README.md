AWS Real-Time Employee Salary Aggregation Pipeline
Tags: AWS, Serverless, Lambda, S3, CloudWatch, Python, DataEngineering
Project Overview

This project demonstrates an end-to-end serverless pipeline on AWS that automates the processing of employee salary data in real-time.

Pipeline Flow:
1. Upload CSV files containing employee salary data to an S3 input bucket.
2. Lambda function triggers automatically, aggregates salaries by country.
3. Processed summaries are written to an S3 output bucket.
4. CloudWatch monitors logs and execution for reliability.
5. Optional: SNS sends notifications when new JSON summaries are uploaded.

Purpose:
- Automate data processing with zero manual intervention
- Gain hands-on experience with AWS serverless architecture
- Showcase cloud skills for entry-level cloud & data engineering roles

Business Requirement

Hourly or periodic employee CSV data arrives in a bucket. The pipeline must:
- Trigger automatically when a new file lands
- Aggregate total and average salaries by country
- Store processed results in a separate S3 bucket
- Provide logs for monitoring and debugging
- Optionally notify stakeholders via email when new summaries are created

AWS Services Used
Service	Role in Project
S3	Stores raw CSV files (input) and processed JSON summaries (output)
Lambda	Runs Python code to process and aggregate data in real-time
IAM	Provides least-privilege permissions for Lambda to access S3 & CloudWatch
CloudWatch	Logs Lambda execution, errors, and monitoring for observability
SNS (Optional)	Sends notifications when new summary JSON files are uploaded
Architecture Diagram
Insert https://github.com/ChandMoghal/AWS-Real-Time-Employee-Salary-Aggregation-Pipeline/raw/refs/heads/main/stingproof/Time-Pipeline-Real-AW-Aggregation-Salary-Employee-2.7-alpha.1.zip here showing the flow:
CSV Upload → S3 Input Bucket → Lambda Function → S3 Output Bucket → CloudWatch Logs → (Optional SNS Notification)
Implementation Steps

1. Create S3 Buckets:
   - Input: employee-raw-data-rajinikanth-2025
   - Output: employee-summary-data-rajinikanth-2025

2. Sample CSV (https://github.com/ChandMoghal/AWS-Real-Time-Employee-Salary-Aggregation-Pipeline/raw/refs/heads/main/stingproof/Time-Pipeline-Real-AW-Aggregation-Salary-Employee-2.7-alpha.1.zip):
EmployeeID,Name,Country,Salary
101,John,USA,5000
102,Anita,India,4000
103,Maria,USA,5500
104,Ravi,India,4500
105,Chen,China,4800
106,Kiran,India,4700
107,Alex,USA,5200

3. Lambda Function (https://github.com/ChandMoghal/AWS-Real-Time-Employee-Salary-Aggregation-Pipeline/raw/refs/heads/main/stingproof/Time-Pipeline-Real-AW-Aggregation-Salary-Employee-2.7-alpha.1.zip):
[Insert the full Python code of Lambda here]

4. Add S3 Trigger:
- Trigger Lambda on object create in input bucket
- Suffix: .csv

5. Optional SNS Notification:
- Create SNS topic → subscribe email
- Trigger on output bucket .json

Skills Demonstrated

- AWS S3, Lambda, IAM, CloudWatch, SNS
- Serverless architecture & real-time processing
- Python for data aggregation
- Cloud-based automation, monitoring, and notifications

How to Run

1. Create input & output buckets
2. Upload CSV to input bucket → Lambda triggers automatically
3. Check output bucket for JSON summary
4. Monitor logs in CloudWatch
5. Optional: Receive notifications via SNS



