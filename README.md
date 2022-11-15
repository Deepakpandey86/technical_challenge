#  Deploy a three-tier architecture in AWS using Terraform


**Step 1:- Create a file for the VPC**

  
**Step 2:- Create a file for the Subnet**

* For this project, I will create total 6 subnets for the front-end tier and back-end tier with a mixture of public & private subnet
*  subnet.tf file 
  
**Step 3:- Create a file for the Internet Gateway**

*  igw.tf file 

**Step 4:- Create a file for the Route table**

*  route_table_public.tf 

**Step 5:- Create a file for EC2 instances**

*  ec2.tf file 


**Step 6:- Create a file for Security Group for the FrontEnd tier**

*  web_sg.tf file 

**Step 7:- Create a file for Security Group for the Database tier**

*  database_sg.tf file 
**Step 8:- Create a file Application Load Balancer**

*  alb.tf file 
**Step 9:- Create a file for the RDS instance**

*   rds.tf file 

**Step 10:- Create a file for outputs**

* Create outputs.tf file 

**Step 11:- Create a file for variable**

* Create vars.tf file and add the subnet_cidr to it



**Step 12:- Create a file for NAT Gateway**

* natg.tf for private networks

So, now our entire code is ready. We need to run the below steps to create infrastructure.

* terraform init is to initialize the working directory and downloading plugins of the provider
* terraform plan is to create the execution plan for our code
* terraform apply is to create the actual infrastructure. It will ask you to provide the Access Key and Secret Key in order to create the infrastructure. So, instead of hardcoding the Access Key and Secret Key, it is better to apply at the run time.


**Step 13:- Verify the resources**

* Terraform will create below resources

  * VPC
  * Application Load Balancer
  * Public & Private Subnets
  * EC2 instances
  * Internet Gateway
  * NAt Gateway
  * Route Table
  * Security Groups for Web & DB instances
  * Route Table

We can get the DNS of a load balancer and paste it into the browser to see load balancer to send the request to two instances.

 
