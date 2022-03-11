# temp script ti setup an EC2 instance as a microk8s node
# allows for k8s centric development and makes migration
# to full cluster easier.

# https://microk8s.io/

ssh -i "ec2-single-node-k8s.pem" ubuntu@ec2-13-57-245-221.us-west-1.compute.amazonaws.com
