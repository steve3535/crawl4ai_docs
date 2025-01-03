# Connecting

Source: https://docs.lxp.lu/first-steps/connecting/

# Connecting

This page contains information on how to configure your connection for accessing MeluXina.

> **Note**

> Note

Note

MeluXina is only available if you have a valid and active user account.

Before you can use MeluXina you require an active project, see Gaining access.

There are two main access mechanisms for connecting to MeluXina services:

Through login nodes by ssh connection to login.lxp.lu

By using custom services via the Cloud module, e.g. JupyterLab, S3.

- Through login nodes by ssh connection to login.lxp.lu

- By using custom services via the Cloud module, e.g. JupyterLab, S3.

## SSH Connection

SSH, also known as Secure Shell, is a network protocol that allows users to connect remotely to another machine. For the SSH connections to MeluXina, you will be authenticated using a public and private key scheme. The public key will be used to generate a challenge that can only be answered with the private key. It is important that you do not share your private key in any case. You just need to provide your public key.

Below are described the steps needed to generate your public-private keys and upload your public key to our servicedesk to have access to MeluXina.

### Get your service desk password

Once your access to MeluXina is approved, you will receive a Welcome Email with a temporary access token and a link where you will be asked to reset your password using the token sent by email.

This password will be used to log in to the servicedesk portal to later upload your public ssh key in the next steps, but not connect directly to MeluXina.

> **Note**

> Note

Note

If you forget your password or the token expires, you can always reset it again in servicedesk.lxp.lu/reset/.

### Generating an SSH key pair

To connect to MeluXina you need to generate an Ed25519 SSH key pair. The private key shall be protected by a passphrase with the following minimal complexity: a minimum of 12 characters, including upper and lower case characters, numbers and special characters.

Depending on the operating system you are using, you can use different SSH clients. In case you are using Windows, we highly recommend to use MobaXterm.

Linux/macOSWindows (Command Prompt)Windows(MobaXterm)

Open a terminal and create an SSH key with the following command:

ssh-keygen -o -a 100 -t ed25519 -f ~/.ssh/id_ed25519_mlux -C "Key4meluXina"

The newly generated private key will be located at ~/.ssh/id_ed25519_mlux and a public key at ~/.ssh/id_ed25519_mlux.pub.

Then run the following command to add your newly generated Ed25519 key to SSH agent:

ssh-add ~/.ssh/id_ed25519_mlux

Or, to add all of the available keys under the default .ssh directory, use the following command:

ssh-add

From your Windows desktop, type 'Windows+R' and enter "cmd". Once the Command prompt is open, type in the following command :

ssh-keygen -o -a 100 -t ed25519 -f %userprofile%/id_ed25519_mlux -C "Key4meluXina"

You'll then be requested to enter a passphrase for your ssh key-pair : This passphrase is personal and should not be communicated. We will not be able to retrieve it for you in case of loss.

The newly generated private key will be located at %userprofile%/id_ed25519_mlux and a public key at %userprofile%/id_ed25519_mlux.pub

Warning

Your ssh key-pair generated on MobaXterm will be saved in the '.ppk' format and will not be usable on platform such as Linux or WSL but on tools like  MobaXterm, Putty, WinSCP...

Download and install MobaXterm from the official website

Start MobaXterm and Click in Tools > MobaKeyGen (SSH key generator)

At the bottom of the window select Ed25519 (1) as the type of key and click Generate (2)

Fill the field Key passphrase (1) to set up a password for the private key and click the Save private key (2) button to store the key in your local device / computer. Then, copy the public key and paste it into a file located in the same folder than your private key (3).

Caution : If you forget your passphrase, we will not be able to retrieve it for you and your SSH Key-pair will become obsolete. This means that in this case, you'll have to generate a new ssh key-pair.

Linux/macOSWindows (Command Prompt)Windows(MobaXterm)

Open a terminal and create an SSH key with the following command:

ssh-keygen -o -a 100 -t ed25519 -f ~/.ssh/id_ed25519_mlux -C "Key4meluXina"

The newly generated private key will be located at ~/.ssh/id_ed25519_mlux and a public key at ~/.ssh/id_ed25519_mlux.pub.

Then run the following command to add your newly generated Ed25519 key to SSH agent:

ssh-add ~/.ssh/id_ed25519_mlux

Or, to add all of the available keys under the default .ssh directory, use the following command:

ssh-add

From your Windows desktop, type 'Windows+R' and enter "cmd". Once the Command prompt is open, type in the following command :

ssh-keygen -o -a 100 -t ed25519 -f %userprofile%/id_ed25519_mlux -C "Key4meluXina"

You'll then be requested to enter a passphrase for your ssh key-pair : This passphrase is personal and should not be communicated. We will not be able to retrieve it for you in case of loss.

The newly generated private key will be located at %userprofile%/id_ed25519_mlux and a public key at %userprofile%/id_ed25519_mlux.pub

Warning

Your ssh key-pair generated on MobaXterm will be saved in the '.ppk' format and will not be usable on platform such as Linux or WSL but on tools like  MobaXterm, Putty, WinSCP...

Download and install MobaXterm from the official website

Start MobaXterm and Click in Tools > MobaKeyGen (SSH key generator)

At the bottom of the window select Ed25519 (1) as the type of key and click Generate (2)

Fill the field Key passphrase (1) to set up a password for the private key and click the Save private key (2) button to store the key in your local device / computer. Then, copy the public key and paste it into a file located in the same folder than your private key (3).

Caution : If you forget your passphrase, we will not be able to retrieve it for you and your SSH Key-pair will become obsolete. This means that in this case, you'll have to generate a new ssh key-pair.

Open a terminal and create an SSH key with the following command:

ssh-keygen -o -a 100 -t ed25519 -f ~/.ssh/id_ed25519_mlux -C "Key4meluXina"

The newly generated private key will be located at ~/.ssh/id_ed25519_mlux and a public key at ~/.ssh/id_ed25519_mlux.pub.

Then run the following command to add your newly generated Ed25519 key to SSH agent:

ssh-add ~/.ssh/id_ed25519_mlux

Or, to add all of the available keys under the default .ssh directory, use the following command:

ssh-add

Open a terminal and create an SSH key with the following command:

ssh-keygen -o -a 100 -t ed25519 -f ~/.ssh/id_ed25519_mlux -C "Key4meluXina"

The newly generated private key will be located at ~/.ssh/id_ed25519_mlux and a public key at ~/.ssh/id_ed25519_mlux.pub.

ssh-keygen -o -a 100 -t ed25519 -f ~/.ssh/id_ed25519_mlux -C "Key4meluXina"

```

ssh-keygen -o -a 100 -t ed25519 -f ~/.ssh/id_ed25519_mlux -C "Key4meluXina"

```

```

ssh-keygen -o -a 100 -t ed25519 -f ~/.ssh/id_ed25519_mlux -C "Key4meluXina"

```

```

~/.ssh/id_ed25519_mlux

```

```

~/.ssh/id_ed25519_mlux.pub

```

Then run the following command to add your newly generated Ed25519 key to SSH agent:

ssh-add ~/.ssh/id_ed25519_mlux

```

ssh-add ~/.ssh/id_ed25519_mlux

```

```

ssh-add ~/.ssh/id_ed25519_mlux

```

Or, to add all of the available keys under the default .ssh directory, use the following command:

```

.ssh

```

ssh-add

```

ssh-add

```

```

ssh-add

```

From your Windows desktop, type 'Windows+R' and enter "cmd". Once the Command prompt is open, type in the following command :

ssh-keygen -o -a 100 -t ed25519 -f %userprofile%/id_ed25519_mlux -C "Key4meluXina"

You'll then be requested to enter a passphrase for your ssh key-pair : This passphrase is personal and should not be communicated. We will not be able to retrieve it for you in case of loss.

The newly generated private key will be located at %userprofile%/id_ed25519_mlux and a public key at %userprofile%/id_ed25519_mlux.pub

From your Windows desktop, type 'Windows+R' and enter "cmd". Once the Command prompt is open, type in the following command :

ssh-keygen -o -a 100 -t ed25519 -f %userprofile%/id_ed25519_mlux -C "Key4meluXina"

You'll then be requested to enter a passphrase for your ssh key-pair : This passphrase is personal and should not be communicated. We will not be able to retrieve it for you in case of loss.

ssh-keygen -o -a 100 -t ed25519 -f %userprofile%/id_ed25519_mlux -C "Key4meluXina"

```

ssh-keygen -o -a 100 -t ed25519 -f %userprofile%/id_ed25519_mlux -C "Key4meluXina"

```

```

ssh-keygen -o -a 100 -t ed25519 -f %userprofile%/id_ed25519_mlux -C "Key4meluXina"

```

The newly generated private key will be located at %userprofile%/id_ed25519_mlux and a public key at %userprofile%/id_ed25519_mlux.pub

```

%userprofile%/id_ed25519_mlux

```

```

%userprofile%/id_ed25519_mlux.pub

```

Warning

Your ssh key-pair generated on MobaXterm will be saved in the '.ppk' format and will not be usable on platform such as Linux or WSL but on tools like  MobaXterm, Putty, WinSCP...

Download and install MobaXterm from the official website

Start MobaXterm and Click in Tools > MobaKeyGen (SSH key generator)

At the bottom of the window select Ed25519 (1) as the type of key and click Generate (2)

Fill the field Key passphrase (1) to set up a password for the private key and click the Save private key (2) button to store the key in your local device / computer. Then, copy the public key and paste it into a file located in the same folder than your private key (3).

Caution : If you forget your passphrase, we will not be able to retrieve it for you and your SSH Key-pair will become obsolete. This means that in this case, you'll have to generate a new ssh key-pair.

> **Warning**

> Warning

Warning

Your ssh key-pair generated on MobaXterm will be saved in the '.ppk' format and will not be usable on platform such as Linux or WSL but on tools like  MobaXterm, Putty, WinSCP...

Download and install MobaXterm from the official website

Start MobaXterm and Click in Tools > MobaKeyGen (SSH key generator)

At the bottom of the window select Ed25519 (1) as the type of key and click Generate (2)

Fill the field Key passphrase (1) to set up a password for the private key and click the Save private key (2) button to store the key in your local device / computer. Then, copy the public key and paste it into a file located in the same folder than your private key (3).

Caution : If you forget your passphrase, we will not be able to retrieve it for you and your SSH Key-pair will become obsolete. This means that in this case, you'll have to generate a new ssh key-pair.

- Download and install MobaXterm from the official website

- Start MobaXterm and Click in Tools > MobaKeyGen (SSH key generator)

```

Tools > MobaKeyGen (SSH key generator)

```

- At the bottom of the window select Ed25519 (1) as the type of key and click Generate (2)

```

Ed25519

```

```

Generate

```

- Fill the field Key passphrase (1) to set up a password for the private key and click the Save private key (2) button to store the key in your local device / computer. Then, copy the public key and paste it into a file located in the same folder than your private key (3).

Fill the field Key passphrase (1) to set up a password for the private key and click the Save private key (2) button to store the key in your local device / computer. Then, copy the public key and paste it into a file located in the same folder than your private key (3).

```

Key passphrase

```

```

Save private key

```

- Caution : If you forget your passphrase, we will not be able to retrieve it for you and your SSH Key-pair will become obsolete. This means that in this case, you'll have to generate a new ssh key-pair.

Caution : If you forget your passphrase, we will not be able to retrieve it for you and your SSH Key-pair will become obsolete. This means that in this case, you'll have to generate a new ssh key-pair.

### Upload your public SSH key

After saving your ssh key-pair into your local device, you'll kindly need to raise a request to MeluXina Support Team, in order to add your public key into your MeuXina user account.

To add your public key to your MeluXina user account, please login in the servicedesk portal with your user ID and password (See Get your service desk password) and click Add a new SSH key to an Account.

```

Add a new SSH key to an Account

```

In the Description field, kindly paste your public ED25519 key in '.txt' format.

The public Ed25519 key that must be uploaded must be looking like the following:

```

Description

```

ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJNjjHKvwvim+bJjCG7HIVYB7ftpxw+bdrU/6O/86Jtb Key4meluXina

```

ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJNjjHKvwvim+bJjCG7HIVYB7ftpxw+bdrU/6O/86Jtb Key4meluXina

```

```

ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJNjjHKvwvim+bJjCG7HIVYB7ftpxw+bdrU/6O/86Jtb Key4meluXina

```

> **Warning**

> Warning

Warning

There are different types of public-key cryptosystems. On MeluXina we are using Ed25519 keys, please do not upload RSA keys or others.

Always remember to keep your private key private! Only upload your public key, never share your private key.

### Connect to MeluXina

Linux/macOSWindows(Command Prompt)Windows(MobaXterm)

MeluXina login nodes allow connection by SSH on port 8822, thus you may access them with:

ssh '<your-user-ID>'@login.lxp.lu -p 8822 -i ~/.ssh/id_ed25519_mlux

To simplify the login procedure you can define a shorthand alias for the connection parameters (user, host, port).

You may add the following declaration to the SSH user configuration file on your system (~/.ssh/config,  create it if it does not already exist):

Host meluxina

Hostname login.lxp.lu

User '<your-user-ID>'

Port 8822

IdentityFile '<absolute-path-to-your-ssh-private-key>'

IdentitiesOnly yes

ForwardAgent no

You will then be able to connect to MeluXina simply with:

ssh meluxina

X11 forwarding is allowed and necessary to display editor windows (gvim, emacs, nedit, etc.) or similar on your desktop. To enable X11 forwarding, log in with the ssh -X option enabled

ssh -X meluxina

Note on errors while connecting

"Permission denied" error: please ensure that your ssh key is unlocked (using ssh-add ~/.ssh/id_ed25519). If you run ssh-add -L, your key should be listed.

"Too many authentication failures" error: you may have too many keys (more than 6). You can check this with ssh-add -L|wc -l. If so you need to specify the ssh key to use for connecting to MeluXina using the ssh command-line option -i ~/.ssh/id_ed25519", or by specifying the ssh key to use in your ~/.ssh/config file with the IdentityFile ~/.ssh/id_ed25519 option.

"Failed setting locale from environment variables" error:, try running ssh with a known locale setting, e.g. LC_ALL="en_US.UTF-8" ssh yourlogin@login.lxp.lu -p 8822

"Could not open connection to your authentication agent" error: You need to have an ssh agent running. On some Linux desktop environments like Gnome or KDE this is provided. If you get this error on Linux or WSL, try to start an ssh-agent manually as follows: eval "$(ssh-agent -s)"

MeluXina login nodes allow connection by SSH on port 8822, thus you may access them with:

ssh '<your-user-ID>'@login.lxp.lu -p 8822 -i %userprofile%/id_ed25519_mlux

To simplify the login procedure you can define a shorthand alias for the connection parameters (user, host, port).

You may add the following declaration to the SSH user configuration file on your system (%userprofile%/config,  create it if it does not already exist):

Host meluxina

Hostname login.lxp.lu

User '<your-user-ID>'

Port 8822

IdentityFile '<absolute-path-to-your-ssh-private-key>'

IdentitiesOnly yes

ForwardAgent no

You will then be able to connect to MeluXina simply with:

ssh meluxina

Open MobaXterm, click in Session (1) and  choose SSH the type of session (2)

Fill the name of the Remote Host as login.lxp.lu (3) and your username to access to MeluXina(4)

Specify the port 8822 (5)

Click in Advanced SSH settings(6), Use private key(7) and select your private key (8) generated in the step Generating an SSH key pair

Click OK and you will connect to MeluXina

Linux/macOSWindows(Command Prompt)Windows(MobaXterm)

MeluXina login nodes allow connection by SSH on port 8822, thus you may access them with:

ssh '<your-user-ID>'@login.lxp.lu -p 8822 -i ~/.ssh/id_ed25519_mlux

To simplify the login procedure you can define a shorthand alias for the connection parameters (user, host, port).

You may add the following declaration to the SSH user configuration file on your system (~/.ssh/config,  create it if it does not already exist):

Host meluxina

Hostname login.lxp.lu

User '<your-user-ID>'

Port 8822

IdentityFile '<absolute-path-to-your-ssh-private-key>'

IdentitiesOnly yes

ForwardAgent no

You will then be able to connect to MeluXina simply with:

ssh meluxina

X11 forwarding is allowed and necessary to display editor windows (gvim, emacs, nedit, etc.) or similar on your desktop. To enable X11 forwarding, log in with the ssh -X option enabled

ssh -X meluxina

Note on errors while connecting

"Permission denied" error: please ensure that your ssh key is unlocked (using ssh-add ~/.ssh/id_ed25519). If you run ssh-add -L, your key should be listed.

"Too many authentication failures" error: you may have too many keys (more than 6). You can check this with ssh-add -L|wc -l. If so you need to specify the ssh key to use for connecting to MeluXina using the ssh command-line option -i ~/.ssh/id_ed25519", or by specifying the ssh key to use in your ~/.ssh/config file with the IdentityFile ~/.ssh/id_ed25519 option.

"Failed setting locale from environment variables" error:, try running ssh with a known locale setting, e.g. LC_ALL="en_US.UTF-8" ssh yourlogin@login.lxp.lu -p 8822

"Could not open connection to your authentication agent" error: You need to have an ssh agent running. On some Linux desktop environments like Gnome or KDE this is provided. If you get this error on Linux or WSL, try to start an ssh-agent manually as follows: eval "$(ssh-agent -s)"

MeluXina login nodes allow connection by SSH on port 8822, thus you may access them with:

ssh '<your-user-ID>'@login.lxp.lu -p 8822 -i %userprofile%/id_ed25519_mlux

To simplify the login procedure you can define a shorthand alias for the connection parameters (user, host, port).

You may add the following declaration to the SSH user configuration file on your system (%userprofile%/config,  create it if it does not already exist):

Host meluxina

Hostname login.lxp.lu

User '<your-user-ID>'

Port 8822

IdentityFile '<absolute-path-to-your-ssh-private-key>'

IdentitiesOnly yes

ForwardAgent no

You will then be able to connect to MeluXina simply with:

ssh meluxina

Open MobaXterm, click in Session (1) and  choose SSH the type of session (2)

Fill the name of the Remote Host as login.lxp.lu (3) and your username to access to MeluXina(4)

Specify the port 8822 (5)

Click in Advanced SSH settings(6), Use private key(7) and select your private key (8) generated in the step Generating an SSH key pair

Click OK and you will connect to MeluXina

MeluXina login nodes allow connection by SSH on port 8822, thus you may access them with:

ssh '<your-user-ID>'@login.lxp.lu -p 8822 -i ~/.ssh/id_ed25519_mlux

To simplify the login procedure you can define a shorthand alias for the connection parameters (user, host, port).

You may add the following declaration to the SSH user configuration file on your system (~/.ssh/config,  create it if it does not already exist):

Host meluxina

Hostname login.lxp.lu

User '<your-user-ID>'

Port 8822

IdentityFile '<absolute-path-to-your-ssh-private-key>'

IdentitiesOnly yes

ForwardAgent no

You will then be able to connect to MeluXina simply with:

ssh meluxina

X11 forwarding is allowed and necessary to display editor windows (gvim, emacs, nedit, etc.) or similar on your desktop. To enable X11 forwarding, log in with the ssh -X option enabled

ssh -X meluxina

Note on errors while connecting

"Permission denied" error: please ensure that your ssh key is unlocked (using ssh-add ~/.ssh/id_ed25519). If you run ssh-add -L, your key should be listed.

"Too many authentication failures" error: you may have too many keys (more than 6). You can check this with ssh-add -L|wc -l. If so you need to specify the ssh key to use for connecting to MeluXina using the ssh command-line option -i ~/.ssh/id_ed25519", or by specifying the ssh key to use in your ~/.ssh/config file with the IdentityFile ~/.ssh/id_ed25519 option.

"Failed setting locale from environment variables" error:, try running ssh with a known locale setting, e.g. LC_ALL="en_US.UTF-8" ssh yourlogin@login.lxp.lu -p 8822

"Could not open connection to your authentication agent" error: You need to have an ssh agent running. On some Linux desktop environments like Gnome or KDE this is provided. If you get this error on Linux or WSL, try to start an ssh-agent manually as follows: eval "$(ssh-agent -s)"

MeluXina login nodes allow connection by SSH on port 8822, thus you may access them with:

ssh '<your-user-ID>'@login.lxp.lu -p 8822 -i ~/.ssh/id_ed25519_mlux

To simplify the login procedure you can define a shorthand alias for the connection parameters (user, host, port).

You may add the following declaration to the SSH user configuration file on your system (~/.ssh/config,  create it if it does not already exist):

ssh '<your-user-ID>'@login.lxp.lu -p 8822 -i ~/.ssh/id_ed25519_mlux

```

ssh '<your-user-ID>'@login.lxp.lu -p 8822 -i ~/.ssh/id_ed25519_mlux

```

```

ssh '<your-user-ID>'@login.lxp.lu -p 8822 -i ~/.ssh/id_ed25519_mlux

```

```

~/.ssh/config

```

Host meluxina

Hostname login.lxp.lu

User '<your-user-ID>'

Port 8822

IdentityFile '<absolute-path-to-your-ssh-private-key>'

IdentitiesOnly yes

ForwardAgent no

```

Host meluxina

Hostname login.lxp.lu

User '<your-user-ID>'

Port 8822

IdentityFile '<absolute-path-to-your-ssh-private-key>'

IdentitiesOnly yes

ForwardAgent no

```

```

Host meluxina

Hostname login.lxp.lu

User '<your-user-ID>'

Port 8822

IdentityFile '<absolute-path-to-your-ssh-private-key>'

IdentitiesOnly yes

ForwardAgent no

```

You will then be able to connect to MeluXina simply with:

ssh meluxina

```

ssh meluxina

```

```

ssh meluxina

```

X11 forwarding is allowed and necessary to display editor windows (gvim, emacs, nedit, etc.) or similar on your desktop. To enable X11 forwarding, log in with the ssh -X option enabled

```

ssh -X

```

ssh -X meluxina

```

ssh -X meluxina

```

```

ssh -X meluxina

```

> **Note on errors while connecting**

> Note on errors while connecting

Note on errors while connecting

"Permission denied" error: please ensure that your ssh key is unlocked (using ssh-add ~/.ssh/id_ed25519). If you run ssh-add -L, your key should be listed.

"Too many authentication failures" error: you may have too many keys (more than 6). You can check this with ssh-add -L|wc -l. If so you need to specify the ssh key to use for connecting to MeluXina using the ssh command-line option -i ~/.ssh/id_ed25519", or by specifying the ssh key to use in your ~/.ssh/config file with the IdentityFile ~/.ssh/id_ed25519 option.

"Failed setting locale from environment variables" error:, try running ssh with a known locale setting, e.g. LC_ALL="en_US.UTF-8" ssh yourlogin@login.lxp.lu -p 8822

"Could not open connection to your authentication agent" error: You need to have an ssh agent running. On some Linux desktop environments like Gnome or KDE this is provided. If you get this error on Linux or WSL, try to start an ssh-agent manually as follows: eval "$(ssh-agent -s)"

- "Permission denied" error: please ensure that your ssh key is unlocked (using ssh-add ~/.ssh/id_ed25519). If you run ssh-add -L, your key should be listed.

```

ssh-add ~/.ssh/id_ed25519

```

```

ssh-add -L

```

- "Too many authentication failures" error: you may have too many keys (more than 6). You can check this with ssh-add -L|wc -l. If so you need to specify the ssh key to use for connecting to MeluXina using the ssh command-line option -i ~/.ssh/id_ed25519", or by specifying the ssh key to use in your ~/.ssh/config file with the IdentityFile ~/.ssh/id_ed25519 option.

```

ssh-add -L|wc -l

```

```

-i ~/.ssh/id_ed25519"

```

```

~/.ssh/config

```

```

IdentityFile ~/.ssh/id_ed25519

```

- "Failed setting locale from environment variables" error:, try running ssh with a known locale setting, e.g. LC_ALL="en_US.UTF-8" ssh yourlogin@login.lxp.lu -p 8822

```

LC_ALL="en_US.UTF-8" ssh yourlogin@login.lxp.lu -p 8822

```

- "Could not open connection to your authentication agent" error: You need to have an ssh agent running. On some Linux desktop environments like Gnome or KDE this is provided. If you get this error on Linux or WSL, try to start an ssh-agent manually as follows: eval "$(ssh-agent -s)"

```

eval "$(ssh-agent -s)"

```

MeluXina login nodes allow connection by SSH on port 8822, thus you may access them with:

ssh '<your-user-ID>'@login.lxp.lu -p 8822 -i %userprofile%/id_ed25519_mlux

To simplify the login procedure you can define a shorthand alias for the connection parameters (user, host, port).

You may add the following declaration to the SSH user configuration file on your system (%userprofile%/config,  create it if it does not already exist):

Host meluxina

Hostname login.lxp.lu

User '<your-user-ID>'

Port 8822

IdentityFile '<absolute-path-to-your-ssh-private-key>'

IdentitiesOnly yes

ForwardAgent no

You will then be able to connect to MeluXina simply with:

ssh meluxina

MeluXina login nodes allow connection by SSH on port 8822, thus you may access them with:

ssh '<your-user-ID>'@login.lxp.lu -p 8822 -i %userprofile%/id_ed25519_mlux

To simplify the login procedure you can define a shorthand alias for the connection parameters (user, host, port).

You may add the following declaration to the SSH user configuration file on your system (%userprofile%/config,  create it if it does not already exist):

ssh '<your-user-ID>'@login.lxp.lu -p 8822 -i %userprofile%/id_ed25519_mlux

```

ssh '<your-user-ID>'@login.lxp.lu -p 8822 -i %userprofile%/id_ed25519_mlux

```

```

ssh '<your-user-ID>'@login.lxp.lu -p 8822 -i %userprofile%/id_ed25519_mlux

```

```

%userprofile%/config

```

Host meluxina

Hostname login.lxp.lu

User '<your-user-ID>'

Port 8822

IdentityFile '<absolute-path-to-your-ssh-private-key>'

IdentitiesOnly yes

ForwardAgent no

```

Host meluxina

Hostname login.lxp.lu

User '<your-user-ID>'

Port 8822

IdentityFile '<absolute-path-to-your-ssh-private-key>'

IdentitiesOnly yes

ForwardAgent no

```

```

Host meluxina

Hostname login.lxp.lu

User '<your-user-ID>'

Port 8822

IdentityFile '<absolute-path-to-your-ssh-private-key>'

IdentitiesOnly yes

ForwardAgent no

```

You will then be able to connect to MeluXina simply with:

ssh meluxina

```

ssh meluxina

```

```

ssh meluxina

```

Open MobaXterm, click in Session (1) and  choose SSH the type of session (2)

Fill the name of the Remote Host as login.lxp.lu (3) and your username to access to MeluXina(4)

Specify the port 8822 (5)

Click in Advanced SSH settings(6), Use private key(7) and select your private key (8) generated in the step Generating an SSH key pair

Click OK and you will connect to MeluXina

Open MobaXterm, click in Session (1) and  choose SSH the type of session (2)

Fill the name of the Remote Host as login.lxp.lu (3) and your username to access to MeluXina(4)

Specify the port 8822 (5)

Click in Advanced SSH settings(6), Use private key(7) and select your private key (8) generated in the step Generating an SSH key pair

Click OK and you will connect to MeluXina

- Open MobaXterm, click in Session (1) and  choose SSH the type of session (2)

```

Session

```

```

SSH

```

- Fill the name of the Remote Host as login.lxp.lu (3) and your username to access to MeluXina(4)

```

Remote Host

```

- Specify the port 8822 (5)

- Click in Advanced SSH settings(6), Use private key(7) and select your private key (8) generated in the step Generating an SSH key pair

```

Advanced SSH settings

```

```

Use private key

```

- Click OK and you will connect to MeluXina

> **SSH host keys verification**

> SSH host keys verification

SSH host keys verification

To verify your connection to the MeluXina Login Nodes, you can check the following ED25519 SSH host keys:

Fingerprint: SHA256:CiIRq/peOWCDY7r5iReXS1KLaO/BBwN7wcpcT4sqsiI

Public key: ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIMkbJzJorf7EayCNtSs5RDBsQv1Qt8zpYmFtWpdj0vqX

Upon successful connection you will see the welcome banner:

Welcome to the Luxembourg - EuroHPC supercomputer

████     ████          ██         ██     ██ ██

░██░██   ██░██         ░██        ░░██   ██ ░░

░██░░██ ██ ░██  █████  ░██ ██   ██ ░░██ ██   ██ ███████   ██████

░██ ░░███  ░██ ██░░░██ ░██░██  ░██  ░░███   ░██░░██░░░██ ░░░░░░██

░██  ░░█   ░██░███████ ░██░██  ░██   ██░██  ░██ ░██  ░██  ███████

░██   ░    ░██░██░░░░  ░██░██  ░██  ██ ░░██ ░██ ░██  ░██ ██░░░░██

░██        ░██░░██████ ███░░██████ ██   ░░██░██ ███  ░██░░████████

░░         ░░  ░░░░░░ ░░░  ░░░░░░ ░░     ░░ ░░ ░░░   ░░  ░░░░░░░░

.-----------------------------------------------------------------------------.

| You are on a MeluXina login node                                            |

|-----------------------------------------------------------------------------|

|                       System information: Compute                           |

|-----------------------------------------------------------------------------|

| Nodes | CPU                     | RAM    | Accelerator              | Disk  |

|-------|-------------------------|--------|--------------------------|-------|

| 573N  | 2x AMD 7H12: 128c @2.6G |  512GB | -                        | -     |

| 200N  | 2x AMD 7452:  64c @2.3G |  512GB | 4x NVIDIA A100-40        | 1.92T |

|  20N  | 2x AMD 7452:  64c @2.3G |  512GB | 2x Intel Stratix 10MX-16 | 1.92T |

|  20N  | 2x AMD 7H12: 128c @2.6G | 4096GB | -                        | 1.92T |

|-----------------------------------------------------------------------------|

|                       System information: Data                              |

|-----------------------------------------------------------------------------|

| Tier           | Capacity | Speed   | Type | Location on compute/login      |

|----------------|----------|---------|------|--------------------------------|

| Scratch        | 0.6PB    | 400GB/s | NVMe | /project/scratch               |

| Home/Project   | 12.5PB   | 180GB/s | HDD  | /home/users, /project/home     |

| Backup         | 7.5PB    | 30GB/s  | HDD  | -                              |

|-----------------------------------------------------------------------------|

|                       System information: Interconnect                      |

|-----------------------------------------------------------------------------|

| Fabric: Infiniband HDR, 200Gbps, DragonFly+ topology                        |

| Links : 1x on CPU nodes, 2x on GPU, FPGA & LargeMemory nodes                |

|-----------------------------------------------------------------------------|

|                       System information: Software                          |

|-----------------------------------------------------------------------------|

| Production software stack: 2023.1                                           |

|                                                                             |

| Modules system: LMod, use `module av` on nodes to discover the environment  |

|-----------------------------------------------------------------------------|

|                           Center information                                |

|-----------------------------------------------------------------------------|

| News & Events      : luxprovide.lu                                          |

| Documentation      : docs.lxp.lu                                            |

| System status      : weather.lxp.lu                                         |

| Support            : servicedesk.lxp.lu, servicedesk@lxp.lu                 |

|-----------------------------------------------------------------------------|

| LinkedIn & Twitter : @luxprovide #meluxina @EuroHPC_JU                      |

°_____________________________________________________________________________°

###############################################################################

#                   System events, in-progress and upcoming                   #

#-----------------------------------------------------------------------------#

#                                                                             #

#  * No events                                                                #

#                                                                             #

###############################################################################

```

Welcome to the Luxembourg - EuroHPC supercomputer

████     ████          ██         ██     ██ ██

░██░██   ██░██         ░██        ░░██   ██ ░░

░██░░██ ██ ░██  █████  ░██ ██   ██ ░░██ ██   ██ ███████   ██████

░██ ░░███  ░██ ██░░░██ ░██░██  ░██  ░░███   ░██░░██░░░██ ░░░░░░██

░██  ░░█   ░██░███████ ░██░██  ░██   ██░██  ░██ ░██  ░██  ███████

░██   ░    ░██░██░░░░  ░██░██  ░██  ██ ░░██ ░██ ░██  ░██ ██░░░░██

░██        ░██░░██████ ███░░██████ ██   ░░██░██ ███  ░██░░████████

░░         ░░  ░░░░░░ ░░░  ░░░░░░ ░░     ░░ ░░ ░░░   ░░  ░░░░░░░░

.-----------------------------------------------------------------------------.

| You are on a MeluXina login node                                            |

|-----------------------------------------------------------------------------|

|                       System information: Compute                           |

|-----------------------------------------------------------------------------|

| Nodes | CPU                     | RAM    | Accelerator              | Disk  |

|-------|-------------------------|--------|--------------------------|-------|

| 573N  | 2x AMD 7H12: 128c @2.6G |  512GB | -                        | -     |

| 200N  | 2x AMD 7452:  64c @2.3G |  512GB | 4x NVIDIA A100-40        | 1.92T |

|  20N  | 2x AMD 7452:  64c @2.3G |  512GB | 2x Intel Stratix 10MX-16 | 1.92T |

|  20N  | 2x AMD 7H12: 128c @2.6G | 4096GB | -                        | 1.92T |

|-----------------------------------------------------------------------------|

|                       System information: Data                              |

|-----------------------------------------------------------------------------|

| Tier           | Capacity | Speed   | Type | Location on compute/login      |

|----------------|----------|---------|------|--------------------------------|

| Scratch        | 0.6PB    | 400GB/s | NVMe | /project/scratch               |

| Home/Project   | 12.5PB   | 180GB/s | HDD  | /home/users, /project/home     |

| Backup         | 7.5PB    | 30GB/s  | HDD  | -                              |

|-----------------------------------------------------------------------------|

|                       System information: Interconnect                      |

|-----------------------------------------------------------------------------|

| Fabric: Infiniband HDR, 200Gbps, DragonFly+ topology                        |

| Links : 1x on CPU nodes, 2x on GPU, FPGA & LargeMemory nodes                |

|-----------------------------------------------------------------------------|

|                       System information: Software                          |

|-----------------------------------------------------------------------------|

| Production software stack: 2023.1                                           |

|                                                                             |

| Modules system: LMod, use `module av` on nodes to discover the environment  |

|-----------------------------------------------------------------------------|

|                           Center information                                |

|-----------------------------------------------------------------------------|

| News & Events      : luxprovide.lu                                          |

| Documentation      : docs.lxp.lu                                            |

| System status      : weather.lxp.lu                                         |

| Support            : servicedesk.lxp.lu, servicedesk@lxp.lu                 |

|-----------------------------------------------------------------------------|

| LinkedIn & Twitter : @luxprovide #meluxina @EuroHPC_JU                      |

°_____________________________________________________________________________°

###############################################################################

#                   System events, in-progress and upcoming                   #

#-----------------------------------------------------------------------------#

#                                                                             #

#  * No events                                                                #

#                                                                             #

###############################################################################

```

```

Welcome to the Luxembourg - EuroHPC supercomputer

████     ████          ██         ██     ██ ██

░██░██   ██░██         ░██        ░░██   ██ ░░

░██░░██ ██ ░██  █████  ░██ ██   ██ ░░██ ██   ██ ███████   ██████

░██ ░░███  ░██ ██░░░██ ░██░██  ░██  ░░███   ░██░░██░░░██ ░░░░░░██

░██  ░░█   ░██░███████ ░██░██  ░██   ██░██  ░██ ░██  ░██  ███████

░██   ░    ░██░██░░░░  ░██░██  ░██  ██ ░░██ ░██ ░██  ░██ ██░░░░██

░██        ░██░░██████ ███░░██████ ██   ░░██░██ ███  ░██░░████████

░░         ░░  ░░░░░░ ░░░  ░░░░░░ ░░     ░░ ░░ ░░░   ░░  ░░░░░░░░

.-----------------------------------------------------------------------------.

| You are on a MeluXina login node                                            |

|-----------------------------------------------------------------------------|

|                       System information: Compute                           |

|-----------------------------------------------------------------------------|

| Nodes | CPU                     | RAM    | Accelerator              | Disk  |

|-------|-------------------------|--------|--------------------------|-------|

| 573N  | 2x AMD 7H12: 128c @2.6G |  512GB | -                        | -     |

| 200N  | 2x AMD 7452:  64c @2.3G |  512GB | 4x NVIDIA A100-40        | 1.92T |

|  20N  | 2x AMD 7452:  64c @2.3G |  512GB | 2x Intel Stratix 10MX-16 | 1.92T |

|  20N  | 2x AMD 7H12: 128c @2.6G | 4096GB | -                        | 1.92T |

|-----------------------------------------------------------------------------|

|                       System information: Data                              |

|-----------------------------------------------------------------------------|

| Tier           | Capacity | Speed   | Type | Location on compute/login      |

|----------------|----------|---------|------|--------------------------------|

| Scratch        | 0.6PB    | 400GB/s | NVMe | /project/scratch               |

| Home/Project   | 12.5PB   | 180GB/s | HDD  | /home/users, /project/home     |

| Backup         | 7.5PB    | 30GB/s  | HDD  | -                              |

|-----------------------------------------------------------------------------|

|                       System information: Interconnect                      |

|-----------------------------------------------------------------------------|

| Fabric: Infiniband HDR, 200Gbps, DragonFly+ topology                        |

| Links : 1x on CPU nodes, 2x on GPU, FPGA & LargeMemory nodes                |

|-----------------------------------------------------------------------------|

|                       System information: Software                          |

|-----------------------------------------------------------------------------|

| Production software stack: 2023.1                                           |

|                                                                             |

| Modules system: LMod, use `module av` on nodes to discover the environment  |

|-----------------------------------------------------------------------------|

|                           Center information                                |

|-----------------------------------------------------------------------------|

| News & Events      : luxprovide.lu                                          |

| Documentation      : docs.lxp.lu                                            |

| System status      : weather.lxp.lu                                         |

| Support            : servicedesk.lxp.lu, servicedesk@lxp.lu                 |

|-----------------------------------------------------------------------------|

| LinkedIn & Twitter : @luxprovide #meluxina @EuroHPC_JU                      |

°_____________________________________________________________________________°

###############################################################################

#                   System events, in-progress and upcoming                   #

#-----------------------------------------------------------------------------#

#                                                                             #

#  * No events                                                                #

#                                                                             #

###############################################################################

```

> **Multiple**

> Multiple

Multiple

By accessing login.lxp.lu you will arrive to one of the 4 login nodes.

If you need to connect to a specific login node, you may jump from the landing login node (e.g. if you arrived at login02) to another by connecting to it specifically (e.g. ssh login01 -p 8822 when you are on login02).

```

ssh login01 -p 8822

```