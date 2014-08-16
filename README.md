This repo is to hold all the pieces required aggregate the DynamoDB records for Alakazam, including tools to parse, decode, and sort the data from the archive file. The file should be aggregated using the datapipeline.json profile for AWS's Data Pipeline service (use the cli and the instructions [here](http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-crossregion-ddb-upload-cli.html)). 



I think the python libraries are dependent on `boto` (may need to make a config file? google it) and that's it for now (for the `collect.py` script) 


Clone this into an EC2 instance and do `sudo yum install python-pip` for pip on EC2. You'll also need to install the AWS CLI and do `aws config` to set your credentials. 
