# allxon-ota-example
Example files for an over the air (OTA) update using the Allxon service for NVIDIA Jetson. Example for JetsonHacks video on YouTube.

There are deliberate placed issues for the scripts presented here. These are addressed when going through the educational video.

One issue is that when jetson-stats is installed, it is setup for all users on the device. However, a particular user must register to be in the 'jtop' group to be able to use the jtop service.

If the Jetson is logged into a user, and you only have one user, then consider adding the following to ota_deplay.sh :

```
active_user=$(who | awk 'NR==1{print $1}')
sudo usermod -aG jtop $active_user
```
If you want to enable jtop for all of the users, then you should modify the script by looking up the users on the system, and then add them to the group.

For example (untested!):
```
for user in $(cut -d: -f1 /etc/passwd); do sudo usermod -aG jtop $user; done
```
You can also make sure that new users are added to the group automatically by modifying the file /etc/default/useradd

# Release

### Initial Release July, 2024
* Tested on JetPack 6
* This should also work on newer releases of JetPack 5 (untested)
