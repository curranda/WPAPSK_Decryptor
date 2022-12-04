# WPAPSK_Decryptor (Cracker)
 Python Script used to decrypt WPA PSK keys using the a word list, SSID, and the encrypted PSK

Generator for WPA PSK keys: https://www.wireshark.org/tools/wpa-psk.html 

Source script used to reverse has the same generation results as Wireshark's site: https://github.com/julianofischer/python-wpa-psk-rawkey-gen 

Run using the following switches:
python3 decryptPSK.py Wordlist SSID EncryptedPSK VerboseSwitch

Example 1 (With Verbose Switch):
python3 decryptPSK.py rockyou.txt WPAPSKSecret d8853d38b81926b5bc46895a0012cd22ceb89051b48d004493150b3f0d2d860f Verbose

Expected Output from Example 1:
![image](https://user-images.githubusercontent.com/46076535/205490456-0b56db35-84c5-4969-8de9-092020faf714.png)
...
![image](https://user-images.githubusercontent.com/46076535/205490498-4e579de9-8800-4dd2-b5c2-8aee3a9898f3.png)

Example 2 (Without Verbose Switch, this should be faster since no output is needed to display)
![image](https://user-images.githubusercontent.com/46076535/205490545-3a07bd9b-e285-4d39-838f-9ae5dbf2ccb1.png)
