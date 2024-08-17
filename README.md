## To run:
`docker build -t my-python-app .`
`docker run --rm my-python-app`


## To deploy to ECR
* Update IAM policy
  * Go to IAM>User. Select active role.
  * Add Permissions > Inline. Select JSON.
  * Add policy `{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Effect": "Allow",
			"Action": [
				"ecr:CreateRepository",
				"ecr:DescribeRepositories",
				"ecr:ListImages",
				"ecr:PutImage",
				"ecr:InitiateLayerUpload",
				"ecr:UploadLayerPart",
				"ecr:CompleteLayerUpload",
				"ecr:DeleteRepository",
				"ecr:DeleteRepositoryPolicy",
				"ecr:SetRepositoryPolicy",
				"ecr:BatchDeleteImage",
				"ecr:BatchCheckLayerAvailability",
				"ecr:GetAuthorizationToken",
				"ecr:ListImages",
				"ecr:DescribeRepositories",
				"ecr:CreateRepository",
				"ecr:PutImage",
				"ecr:InitiateLayerUpload",
				"ecr:UploadLayerPart",
				"ecr:CompleteLayerUpload",
				"ecr:DeleteRepository",
				"ecr:DeleteRepositoryPolicy",
				"ecr:SetRepositoryPolicy",
				"ecr:BatchDeleteImage",
				"ecr:BatchCheckLayerAvailability"
			],
			"Resource": "*"
		}
	]
}
`
* Deploy docker to ECR
  * Create ECR repo: `aws ecr create-repository --repository-name my-python-app`
  * Authenticate: `aws ecr get-login-password --region your-region | docker login --username AWS --password-stdin your-account-id.dkr.ecr.your-region.amazonaws.com`
  * Tag docker image: `docker tag my-python-app:latest your-account-id.dkr.ecr.your-region.amazonaws.com/my-python-app:latest`
  * Push docker image: `docker push your-account-id.dkr.ecr.your-region.amazonaws.com/my-python-app:latest`
* Create an IAM Role:
  * Go to the IAM console.
  * Create a new role with AWS service as the trusted entity and Batch as the use case.
  * Change the trust policy to:
    `{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "",
            "Effect": "Allow",
            "Principal": {
                "Service": "ecs-tasks.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}`
  * Attach the AmazonECSTaskExecutionRolePolicy policy to the role. This policy allows ECS tasks to pull images from ECR and write logs to CloudWatch.
  * Name the role (e.g., AWSBatchECSRole).
* Create a Job Definition:
  * Click Job Definitions in the left pane, then click Create.
  * Set a name for your job definition (e.g., `ploomber`).
  * Under Container properties:
    * Image: Enter your ECR image URL (e.g., 123456789012.dkr.ecr.us-east-1.amazonaws.com/my-app:latest).
    * Memory: Specify the memory in MiB required (e.g., 512).
    * Job Role: Select the IAM role you created earlier (e.g., AWSBatchECSRole).
    * Optionally, add environment variables or a command to override the default command in the Docker image.
  * Click Create to save the job definition.
* Create a Compute Environment (if not already done):
  * Go to Compute environments in the Batch console.
  * Click Create to set up a new environment. Choose either a managed or unmanaged environment based on your needs.
  * Configure the environment with the necessary instance types, maximum vCPUs, and other settings.
  * Set name to `ploomber`
  * Associate the compute environment with a job queue.
* Create a Job Queue:
  * Go to Job queues in the Batch console.
  * Click Create.
  * Set a name for the job queue (e.g., `ploomber_queue`).
  * Associate the job queue with the compute environment you created.
  * Click Create to save the job queue.
* Submit a Job:
  * Click Jobs in the left pane.
  * Set the job name (e.g., `ploomber_job`).
  * Select the job queue you created.
  * Choose the job definition you created (e.g., MyBatchJob).
  * Optionally, override the command or environment variables if needed.
  * Click Submit job.
* Job failing with error: `ResourceInitializationError: unable to pull secrets or registry auth: The task cannot pull registry auth from Amazon ECR: There is a connection issue between the task and Amazon ECR. Check your task network configuration. RequestError: send request failed caused by: Post "https://api.ecr.us-east-1.amazonaws.com/": dial tcp 44.213.79.86:443: i/o timeout`
