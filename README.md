Docker Lambda AWS Project
Overview
This project demonstrates how to create and deploy an AWS Lambda function using Docker and the AWS CDK. The Lambda function is written in Python and is containerized into a Docker image for deployment.

Prerequisites
AWS CLI installed and configured
Docker installed
AWS CDK installed
Node.js and npm installed
Project Setup
Create a CDK Project

First, create a new directory for your CDK project and initialize it:

```
mkdir docker-lambda-aws
cd docker-lambda-aws
cdk init app --language typescript
```
Create Docker Image Folder

Within the project directory, create a folder to store your Docker image and the application files:

```
mkdir image
cd image
mkdir src
```
Add Lambda Handler

Inside the src folder, create a file named main.py. This file will contain your Lambda function handler code.

Create Dockerfile

In the image directory, create a Dockerfile to containerize your Lambda function. This file defines the Docker image configuration.

Build Docker Image

Navigate to the directory where the Dockerfile is located and build the Docker image:

```
docker build -t docker-image:test .
Run Docker Container
```
After building the Docker image, run the Docker container and see if it is running:

```
docker run -p 9000:8080 docker-image:test
```

Open a new terminal and test the running Docker container using the following command. If port 9001 is in use, you can use an alternative port such as 9002 or 9003:

``` 
Invoke-WebRequest -Uri "http://localhost:9001/2015-03-31/functions/function/invocations" -Method POST -Body '{}' -ContentType "application/json"
```
Configure AWS Lambda Function
Update CDK Stack

Open docker-lambda-aws/lib/docker-lambda-aws-stack.ts and configure the file to create the Docker image and upload it to AWS Lambda.

Configure AWS CLI

In the terminal, configure the AWS CLI:

```
aws configure
```
Enter your AWS Access ID and Secret Key. You may leave the region blank or set it to us-east-1.

Verify AWS CLI Configuration

Verify your AWS CLI configuration with:

```
aws sts get-caller-identity
```
You should receive your AWS login information.

Bootstrap CDK

Navigate back to the project directory and bootstrap the CDK environment:

```
cd ..
cdk bootstrap --region us-east-1
```
Bootstrap the environment only once per account per region. This sets up resources needed for managing Lambda functions.

Deploy CDK Stack

Deploy the CDK stack with:

```
cdk deploy
```
Upon successful deployment, a URL will be provided. You can also find the Lambda function URL in the AWS Console under Lambda.

Troubleshooting
Incorrect Architecture: For Windows, it is recommended to use lambda.Architecture.X86_64. However, lambda.Architecture.ARM_64 has been used successfully in this tutorial even on a Windows machine.

Performance Note: Lambda functions can be slower on cold starts compared to native Python Lambdas. Howev
