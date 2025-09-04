student_status = input("Är du student eller vuxen? ")
if 'student' in student_status.lower(): # Mer om .lower() nästa vecka
    enkel = 28
    dygn = 90
    tredygn = 180
    månad = 645
else:
    enkel = 37
    dygn = 120
    tredygn = 240
    månad = 860

### Beräkningar
värt_med_dygn = int(dygn / enkel) + 1
print("Värt att köpa dygnsbiljett om man reser minst", värt_med_dygn,"gånger under ett dygn")

print("Eftersom:", (värt_med_dygn - 1) * enkel, "kostar mindre än", dygn)
print("Eftersom:", värt_med_dygn * enkel, "kostar mer än", dygn)

print("------------------")

värt_med_tredygn = int(tredygn / enkel) + 1
print("Värt att köpa tredygnsbiljett om man reser minst", värt_med_tredygn, "gånger under tre dygn")
print("Eftersom:", (värt_med_tredygn - 1) * enkel, "kostar mindre än", tredygn)
print("Eftersom:", värt_med_tredygn * enkel, "kostar mer än", tredygn)