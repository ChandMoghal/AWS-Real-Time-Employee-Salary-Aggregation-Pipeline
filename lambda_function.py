import boto3
import csv
import json
from io import StringIO

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    try:
        source_bucket = event['Records'][0]['s3']['bucket']['name']
        file_key = event['Records'][0]['s3']['object']['key']

        response = s3.get_object(Bucket=source_bucket, Key=file_key)
        file_content = response['Body'].read().decode('utf-8')
        csv_reader = csv.DictReader(StringIO(file_content))

        salary_data = {}
        for row in csv_reader:
            country = row['Country']
            salary = float(row['Salary'])
            if country not in salary_data:
                salary_data[country] = {'total_salary': 0, 'count': 0}
            salary_data[country]['total_salary'] += salary
            salary_data[country]['count'] += 1

        results = {}
        for country, data in salary_data.items():
            avg = data['total_salary'] / data['count']
            results[country] = {
                'total_salary': data['total_salary'],
                'average_salary': round(avg, 2),
                'employee_count': data['count']
            }

        target_bucket = 'employee-summary-data-rajinikanth-2025'
        output_file = file_key.replace(".csv", "_summary.json")
        s3.put_object(
            Bucket=target_bucket,
            Key=output_file,
            Body=json.dumps(results, indent=4),
            ContentType='application/json'
        )

        print(f"Processed {file_key} successfully!")

    except Exception as e:
        print("Error:", e)
        raise e
