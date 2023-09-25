<h2>Lambda Function to Invalidate CloudFront Distribution cache</h2>
<p>Wanted an easy way to upfront the CloudFront distribution without having to update it manually. After researching / tinkering, the easiest way seems to be with triggered actions to an S3 bucket from a Lambda function. This repository will contain code and permissions needed. 

Note: CodeCommit and CodePipeline can work as well. It was more steps to setup, but this is more practical within VS Code and GitHub </p>
