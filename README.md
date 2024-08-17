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
* Create an ECS Container
  * Go to the ECS console.
  * Click on Clusters and then Create Cluster.
  * Choose Fargate. Name cluster `PloomberCluster`
