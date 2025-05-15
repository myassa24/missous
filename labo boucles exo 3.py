TAUX = 0.05

montantInvesti = float(input("Tapez le montant investi: "))

montantCumule= montantInvesti

for i in range(1,11):
    montantCumule+= montantCumule* TAUX

print("Le montant cumulé = ", round(montantCumule,2))
