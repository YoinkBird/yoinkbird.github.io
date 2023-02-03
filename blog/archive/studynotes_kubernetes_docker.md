# Worklog - 2018-08-19: Explore PipelineAI and Kubernetes

Learn PipelineAI and Kubernetes

# PipelineAI

https://github.com/PipelineAI/pipeline/tree/master/docs/quickstart/kubernetes

## Install Pipeline AI CLI

https://github.com/PipelineAI/pipeline/blob/master/docs/quickstart/README.md#install-pipelinecli

$ pip install cli-pipeline==1.5.200 --default-timeout=120 --ignore-installed --no-cache --upgrade

$ pipeline version
['/home/thisuser/devtools/miniconda3/bin/pipeline', 'version']

CLI version: 1.5.200
API version: v1

Default build type: docker
Default build context path: . => /home/thisuser/workspace/mleng

Default train base image: docker.io/pipelineai/train-cpu:1.5.0
Default predict base image: docker.io/pipelineai/predict-cpu:1.5.0

cli_version:                1.5.200
api_version:                v1
build_type_default:         docker
build_context_path:         /home/thisuser/workspace/mleng
build_context_path_default: .
train_base_image_default:   docker.io/pipelineai/train-cpu:1.5.0
predict_base_image_default: docker.io/pipelineai/predict-cpu:1.5.0


# https://kubernetes.io/docs/getting-started-guides/ubuntu/
$ sudo snap install conjure-up --classic
$ conjure-up kubernetes


# WORKLOG
# kubernetes docker ohmy
having a difficult time deciding "which" kubernetes to install
https://www.sumologic.com/blog/devops/kubernetes-vs-docker/
minikube:
https://www.linux.com/learn/getting-started-kubernetes-easy-minikube

# whoah nelly
https://kubernetes.io/docs/tasks/tools/install-minikube/
* install hypervisor e.g. virtualbox
* install kubectl
* install minikube
see also: https://www.linux.com/learn/getting-started-kubernetes-easy-minikube

hypervisor:
need to installl virtualbox
BUT:
Note: Minikube also supports a --vm-driver=none option that runs the Kubernetes components on the host and not in a VM. Docker is required to use this driver but a hypervisor is not required.

kubectl:
TODO
# modified based on 'minikube'
curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl && chmod +x kubectl && sudo mv kubectl /usr/local/bin/

Configure kubectl
In order for kubectl to find and access a Kubernetes cluster, it needs a kubeconfig file, which is created automatically when you create a cluster using kube-up.sh or successfully deploy a Minikube cluster

=> wait until Minikube is deployed

minikube:
install:
https://github.com/kubernetes/minikube/releases
curl -Lo minikube https://storage.googleapis.com/minikube/releases/v0.28.2/minikube-linux-amd64 && chmod +x minikube && sudo mv minikube /usr/local/bin/

verify:
https://github.com/kubernetes/minikube/blob/v0.28.2/README.md#Quickstart

> minikube start
: VBoxManage not found. Make sure VirtualBox is installed and VBoxManage is in the path.

> minikube start
$ minikube start --vm-driver=none
========================================
kubectl could not be found on your path. kubectl is a requirement for using minikube
To install kubectl, please run the following:

curl -Lo kubectl https://storage.googleapis.com/kubernetes-release/release/v1.10.0/bin/linux/amd64/kubectl && chmod +x kubectl && sudo mv kubectl /usr/local/bin/

To disable this message, run the following:

minikube config set WantKubectlDownloadMsg false
========================================
Starting local Kubernetes v1.10.0 cluster...
Starting VM...
Getting VM IP address...
Moving files into cluster...
Downloading kubelet v1.10.0
Downloading kubeadm v1.10.0
Finished Downloading kubeadm v1.10.0
Finished Downloading kubelet v1.10.0
E0803 00:32:02.111449    8896 start.go:258] Error updating cluster:  downloading binaries: transferring kubeadm file: &{BaseAsset:{data:[] reader:0xc42000e0a8 Length:0 AssetName:/home/myuser/.minikube/cache/v1.10.0/kubeadm TargetDir:/usr/bin TargetName:kubeadm Permissions:0641}}: error creating file at /usr/bin/kubeadm: open /usr/bin/kubeadm: permission denied
================================================================================
An error has occurred. Would you like to opt in to sending anonymized crash
information to minikube to help prevent future errors?
To opt out of these messages, run the command:
        minikube config set WantReportErrorPrompt false
================================================================================
Please enter your response [Y/n]:

=> expects sudo, not sure

EXPERIMENT1
# try this: "Linux Continuous Integration without VM Support"

# start with sudo:
$ sudo minikube start --vm-driver=none
Starting local Kubernetes v1.10.0 cluster...
Starting VM...
Getting VM IP address...
Moving files into cluster...
Setting up certs...
Connecting to cluster...
Setting up kubeconfig...
Starting cluster components...
# long wait
Kubectl is now configured to use the cluster.
===================
WARNING: IT IS RECOMMENDED NOT TO RUN THE NONE DRIVER ON PERSONAL WORKSTATIONS
        The 'none' driver will run an insecure kubernetes apiserver as root that may leave the host vulnerable to CSRF attacks

When using the none driver, the kubectl config and credentials generated will be root owned and will appear in the root home directory.
You will need to move the files to the appropriate location and then set the correct permissions.  An example of this is below:

        sudo mv /root/.kube $HOME/.kube # this will write over any previous configuration
        sudo chown -R $USER $HOME/.kube
        sudo chgrp -R $USER $HOME/.kube

        sudo mv /root/.minikube $HOME/.minikube # this will write over any previous configuration
        sudo chown -R $USER $HOME/.minikube
        sudo chgrp -R $USER $HOME/.minikube

This can also be done automatically by setting the env var CHANGE_MINIKUBE_NONE_USER=true
Loading cached images from config file.

# NOTE: sudo required because ~/.kube/config should have been created as normal user
# next step in 

$ ls -ltd ~/.kube/config 
-rw------- 1 root root 432 Aug  3 00:46 /home/myuser/.kube/config

$ kubectl get po
error: Error loading config file "/home/myuser/.kube/config": open /home/myuser/.kube/config: permission denied

$ sudo kubectl get po
No resources found.

EXPERIMENT2 - minkube already running
# but: from "Quickstart"
$ sudo kubectl run hello-minikube --image=k8s.gcr.io/echoserver:1.4 --port=8080
deployment.apps/hello-minikube created

$ sudo kubectl expose deployment hello-minikube --type=NodePort
service/hello-minikube exposed

# already running
$ sudo kubectl get pod
NAME                             READY     STATUS    RESTARTS   AGE
hello-minikube-6c47c66d8-7t5x2   1/1       Running   0          3m


$ sudo minikube service hello-minikube --url
http://192.xxx.xxx.xxx:port

$ curl $( sudo minikube service hello-minikube --url)
CLIENT VALUES:
client_address=192.xxx.xxx.xxx
command=GET
real path=/
query=nil
request_version=1.1
request_uri=http://192.xxx.xxx.xxx:port/

SERVER VALUES:
server_version=nginx: 1.10.0 - lua: 10001

HEADERS RECEIVED:
accept=*/*
host=192.xxx.xxx.xxx:port
user-agent=curl/7.58.0
BODY:
-no body in request-


$ sudo kubectl delete service hello-minikube
service "hello-minikube" deleted

# fixing sudo
$ minikube stop
Stopping local Kubernetes cluster...
Error stopping machine:  Error loading host: minikube: Error loading host from store: open /home/myuser/.minikube/machines/minikube/config.json: permission denied
...

$ sudo chown myuser ~/.minikube/machines/minikube/config.json


$ minikube stop
Stopping local Kubernetes cluster...
Machine stopped.

=> therefore also chmodding the ~/.kube dir
$ sudo chown -R myuser ~/.kube/

=> time to fix all the things. Start from the "Linux Continuous Integration without VM Support"
$ sudo minikube stop 
Stopping local Kubernetes cluster...
Machine stopped.


