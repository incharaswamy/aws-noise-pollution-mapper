# aws-noise-pollution-mapper
Serverless noise monitoring system using AWS

# Neighbourhood Noise Pollution Mapper

## Why I built this

Noise complaints are common — construction, traffic, loud music — but reporting them is often inconvenient.
I wanted to build a simple system where anyone can upload an audio clip and report noise without needing an app.

This project explores how cloud systems can automate that process end-to-end.

---

## What this project does

* Upload an audio file
* Automatically process the upload
* Store the complaint
* Send an alert when noise reports increase

All of this runs without managing servers, using AWS services.

---

## Worki

Upload → S3 → Lambda → DynamoDB → SNS → Email Alert

### Flow:

1. Audio file is uploaded to Amazon S3
2. S3 triggers an AWS Lambda function
3. Lambda processes the file and creates a report
4. The report is stored in DynamoDB
5. If reports exceed a threshold, SNS sends an email alert

---

## Tech used

* AWS Lambda
* Amazon S3
* Amazon DynamoDB
* Amazon SNS
* Python

---

## What makes this interesting

* Fully serverless architecture
* Event-driven design
* Practical real-world use case
* Built with AWS Free Tier in mind

---

## Current limitation

The system currently uses placeholder text instead of real speech recognition because Amazon Transcribe is not yet enabled on the account.

---

## Future improvements

* Integrate speech-to-text using AWS Transcribe
* Add location-based complaint tracking
* Build a dashboard or map view
* Implement time-based filtering (for example, last 24 hours only)

---

## What I learned

* Designing event-driven systems
* Integrating multiple AWS services
* Debugging real cloud issues (permissions, regions, triggers)
* Building scalable backend systems

---

## About this project

This started as a simple idea and evolved into a complete serverless pipeline.
It is designed to be simple, scalable, and practical.

---

## Demo

Upload → Stored → Alert triggered

---

## Author

Inchara Swamy
