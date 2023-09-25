<h2>Lambda Function to Invalidate CloudFront Distribution cache</h2>
<p>Wanted an easy way to update the CloudFront distribution without having to update it manually. After researching / tinkering, the easiest way seems to be with triggered actions to an S3 bucket from a Lambda function. This repository will contain code and permissions needed. Compliments any CI/CD updates to website through GitHub nicely.

Note: CodeCommit and CodePipeline can work as well. It was more steps to setup, but this is more practical within VS Code and GitHub </p>

Simple Flowchart of process:

![awscloudinval](https://github.com/ryangoddard1/s3-invalidate-cloudfront-distro/assets/84172786/86d4b47e-49ee-4357-aa4c-a7299476909b)

