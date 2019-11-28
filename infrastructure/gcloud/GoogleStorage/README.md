Dataproc provisioning script
===

You need to have the credentials file from the google account in this folder called as ```credentials.json```

Copy ```terraform.tfvars.dist``` to ```terraform.tfvars``` and modify as you like

Running
```
terraform init
terraform plan -out=run.plan
terraform apply "run.plan"
terraform destroy
```