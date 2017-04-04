# -*- coding: utf-8 -*-

print("Dobrodošli v igri Ugani skrito število!")
print("Pravila so enostavna: Uganite, katero število imam v mislih in si prislužite bogato nagrado!")

vnos = raw_input("Vnesite število: ")

while vnos != "7":
    print("Števila niste uganili! Poskusite znova!")
    vnos = raw_input("Vnesite število: ")
if vnos == "7":
    print("Čestitamo! Uganili ste število in si prislužili liziko!")




