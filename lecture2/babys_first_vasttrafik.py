## To be filled in class

## "Hur mycket behöver jag resa så att det är värt att köpa dygnsbiljett/månadskort"?

# Studentpriser
enkel = 28
dygn = 90
tredygn = 180
månad = 645


### Beräkningar
värt_med_dygn = int(dygn / enkel) + 1
print("Värt att köpa dygnsbiljett om man reser minst", värt_med_dygn,"gånger under ett dygn")

print("Eftersom:", (värt_med_dygn - 1) * enkel, "kostar mindre än", dygn)
print("Eftersom:", värt_med_dygn * enkel, "kostar mer än", dygn)


#####

värt_med_tredygn = int(tredygn / enkel) + 1
print("Värt att köpa tredygnsbiljett om man reser minst", värt_med_tredygn, "gånger under tre dygn")


