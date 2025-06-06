# Wifi Password Recovery
This project starts like a very simple idea, "OMG, i forgot my Wifi password, sorry guys, i can't help you with that"
in this case, a friend of mine start the conversation asking me if it was possible to hack
a wifi password, i know it's possible but is ilegal, insted of that, maybe we can recover
a password already saved on my PC, it's easier and also legal.
## Functioning
This code starts using a basic command of the cmd power shell to recover the wifi passwords
of the history of profiles connections, that is:
```
netsh wlan show profiles
```
So, the only way to automatize this command using python was using it in a function, to
obtain the information of the profiles, folllowing to another function that use the 
parameters to get the key of a specific profile. To run this project and to create a json
file with the passwords, you need to write this command.
```
python WifiProfiles.py
```