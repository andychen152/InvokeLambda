# InvokeLambda
Our goal is to invoke an AWS Lambda function from other cloud providers. Such functionality is essential in the real world with very little resources on how to set up the connections. We will test the connection across multiple clouds (ex. Azure and Google Cloud) and profile it, learning the pros and cons of each provider in this use case. 

# Week 5 Contribution:
* Created free-tier AWS account & setup basic credentials
* Completed this [tutorial](https://docs.aws.amazon.com/lambda/latest/dg/with-s3.html), allowing us to invoke Lambdas from S3
* Next steps: Adding the S3 library to a different FaaS platform and invoking AWS Lambdas via S3

# Week 6 Contribution:
* Completed this [tutorial](https://docs.microsoft.com/en-us/azure/azure-functions/), setting up Azure Functions
* Set up python script to put objects in S3
* Next steps: Link Azure Functions with S3 by deploying python script on Azure Functions

# Week 7 Contributions:
* Linked Azure Function with S3
* Next steps: Start profiling our procedure to trigger Lambda Function through Azure and brainstorm other ways to replicate the same Lambda Function trigger.


# Week 8 Contributions:
* Able to trigger different image sizes from Azure to AWS
* Brainstormed to profile against different ways to trigger Lambda (ex: API Gateway)
* Trigger Link: https://s3buckettrigger.azurewebsites.net/api/HttpTriggerJS1?code=jTMWtHeaFeJ0C5Ah7mqcdwkjW13D1UePrMx6pWycHQcB4uWlNQJwBw==
* Next steps: Finish figuring out 2-3 more ways to trigger Lambda through Azure Functions and fully connect them