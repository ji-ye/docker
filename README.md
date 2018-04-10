
## Deploying a PySpark machine learning model on EC2 with Docker

that includes training a logistic regression model with PySpark, building a docker image, and running it on AWS EC2 machine.

## Deployment on AWS EC2
Open port 3838 with a security group under EC2 settings.

* SSH into the EC2 Node
```bash
ssh -i keyname.pem [ec2-user@instance-DNS]
```

* Install docker
```bash
sudo yum update -y
sudo yum install -y docker
sudo yum install -y git
```

* Start docker and give permissions to the ec2-user
```bash
sudo service docker start
sudo usermod -a -G docker ec2-user
```

* Repeat the "SSH into the EC2 node" step to restart the user account with the updated permissions.

* Git Clone the Repository.
```bash
git clone https://github.com/ji-ye/docker.git
```

* Build the Docker Image
```bash
cd docker
docker-compose up
```

* Visit [instance-DNS]:3838 to see the web application


## Deployment Locally
In terminal, go to ml directory:
```bash
python predict.py
```
Then, go to input directory:
```bash
python form.py
```
Then open up localhost:3838 to see the web application.
