# sshtanos
Using an ollama model that interacts autonomously with a Linux system over ssh.&nbsp;

## Environment

### 1. install SSH on the Linux system
Make sure SSH Server is installed and running on your Linux system. You can install OpenSSH Server with the following command:
```sh
sudo apt-get install openssh-server
```
### 2. Setting up SSH keys

Generate an SSH key on the machine you wish to connect from (if you haven't already done so):

```sh

ssh-keygen -t rsa -b 4096
```
Add the generated public key to the ~/.ssh/authorized_keys file of the user on the Linux server.


### 3. Python
Install the libraries paramiko (for SSH) and a library to interact with the language model (e.g. openai for GPT-3/4).&nbsp;

```
pip install paramiko openai
``` 	 
### 4. Use 

Run the script from your terminal:

 
```sh

python sshtanos.py

```
