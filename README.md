Back in the days when SonicWall is not supporting upload
of multiple ip addresses at once; you have to create hosts
one by one.

Imagine creating 200+ host using GUI.

This code tries to simplify the task by spitting out prepared 
syntax with your 200+ IP addresses. All you need to do after 
providing those IP addresses is to copy and paste the 
generated configuration.

You need to have a CLI access to your firewall in order to
get the benefit of this script.

Requirements: Python 2.7, Kali Linux

ipadd.txt: Edit and input all host IP address


//Coded in 2015
https://github.com/ledzep84
