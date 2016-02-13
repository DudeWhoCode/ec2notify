# ec2notify
A simple daemon that monitors all the AWS ec2 running instances using boto3, filters it by the team/group who created it
and sends an email as a reminder to the respective team members end of every day to shutdown idle instances.

# prerequisites
Before using this script you need the following.

1. An active AWS_KEY and AWS_SECRET with proper permissions
2. ec2 instances need to be tagged. [click to know what are tags and
how to create them](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html)

# Getting started
1. Create a Virtual envorinment, activate it and do,
    `pip install -r requirements.txt`
2. Open ec2notify.cfg and edit the following fields
    * __tags__ : 
        If you have referred the above mentioned aws link, now you know what are the key and value in a tag. In this 
        dictionary tags, its key is the aws Key and the value is the aws Value, in our case : 
        For example, you have 6 instances (m1, m2, m3, m4, m5 , m6) running and there are three tech teams (backend, frontend, 
        data) in your company. you would have assigned the following tags for the machines m1 -> team:data, m2 -> team:data, 
        m3 -> team:backend, m4 -> team:backend, m5 -> team:frontend, m6 -> team:frontend. In this case the tags field should be 
        `tags={'team' : ['data', 'backend', 'frontend']}`
    * __username__ : 
        The username of the sender email, for example `notify@company.com`
    * __username__ : 
        The password for sender email [`notify@company.com`]
    * __recipients__ : 
        recipients is a dictionary where the key is the "team name" and value is always a list of email ids of that 
        team members. 
        Note : The key should be same as the values given in __tags__ field above.!!
        In our case : 
        `recipients={'data' : ['user@example.com', 'user1@example.com', 'user2@example.com'], 'backend' : ['user@example.com', 'user1@example.com', 'user2@example.com'], 'frontend' : ['user@example.com']}`
    * __aws_key, aws_secret__ : 
        boto3 uses this key and secret if ~/aws/config file is not found (Not yet implemented)
3. Now after settting all fields in the ec2notify.cfg, just run ec2notify.py file :
    `python ec2notify.py`
4. To run this remider script end of every day or every week, use [crontab](http://www.computerhope.com/unix/ucrontab.htm).
    * `crontab -e`
    * At the end of the file, enter 
        `30 18 * * * python /path/to/project/ec2notify.py
    * If you are running it under virtual environment, you need to activate it first and give absolute path to python and script
    `30 18 * * * cd /path/to/project && /path/to/project/env/bin/python/path/to/project/ec2notify.py`
    * Enter either one of them based on your need and close it. Now ec2notify will run at 6:30 pm everyday.

# The final reminder email
![alt text](http://i.imgur.com/uvzlMIS.png)