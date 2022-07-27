#This script is used to
#find details
#of a phone number

#Code Goes Here!
#importing dependencies
import phonenumbers
from phonenumbers import timezone,geocoder,carrier

number=input("Enter your Mobile Number with Country Code :")
#Enter your mobile number as input
phone=phonenumbers.parse(number)
time=timezone.time_zones_for_number(phone)
carr=carrier.name_for_number(phone,"en")
regeo=geocoder.description_for_number(phone,"en")

print("Your Country code and Phone Number is : ",phone)
print("Your TimeZone is :",time)
print("Your Carrier is : ",carr)
print("Your Country is : ",regeo)