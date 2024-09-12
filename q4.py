#If the given string S1= “Maha Bharat”, generate the following strings by manipulating S1.
#“mAHA bHARAT”
#“Bharat”
#“BharatBharatBharat”
#“Mera Bharat”
#“Mera Bharat Mahan”

s="Maha Bharat"
print(s[0].lower()+s[1:].upper())
print(s[5:])
print(s[5:]*3)
print(s.replace("Maha","Mera"))
print(s.replace("Maha","Mera")+" Mahaan")
