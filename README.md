# CryptHue

## How to use it

Simply replace the following arguments by your bridge local IP address and hashed username :

b = Bridge("bride_ip_address_here", "hashed_valid_username_here").lights


Select the lamp by modifying the variable "lampe" at line 9


The variable "CMCid" is the ID of the crypto that you wish to follow. You can find the ID here :
https://api.coinmarketcap.com/v2/ticker/ 


The variable "loopTime" is the refresh time in seconds (5 minutes by default).


The variable "varia" is the min/max range of percentage variation. The default is 5%. Which means that you will get a full green at 5% and a full red at -5%. Everything in between will give an in between color.

## Dependancy
You will need the following package :
https://github.com/quentinsf/qhue 

Or install it from pip :
pip install qhue
