def get_soc_sec_tax(gross_pay):
    # Social Security tax (6.2%)
    return gross_pay * 0.062

def get_medicare_tax(gross_pay):
    # Medicare tax (1.45%)
    return gross_pay * 0.0145

def get_federal_tax(gross_pay, withholding_code):
    if withholding_code == 0:
        return gross_pay * 0.23
    elif withholding_code == 1:
        return gross_pay * 0.21
    elif withholding_code == 2:
        return gross_pay * 0.195
    elif withholding_code == 3:
        return gross_pay * 0.185
    elif withholding_code >= 4:
        

        return gross_pay * (0.18 - (0.005 * (withholding_code - 4)))
    else:
        return 0
    

    # Person 1
gross_pay1 = 750
withholding_code1 = 0
soc_sec_tax1 = get_soc_sec_tax(gross_pay1)
medicare_tax1 = get_medicare_tax(gross_pay1)
federal_tax1 = get_federal_tax(gross_pay1, withholding_code1)


#person2
gross_pay2 = 1550
withholding_code2 = 0
soc_sec_tax2 = get_soc_sec_tax(gross_pay2)
medicare_tax2 = get_medicare_tax(gross_pay2)
federal_tax2 = get_federal_tax(gross_pay2, withholding_code2) 

#person 3
gross_pay3 = 1100
withholding_code3 = 5
soc_sec_tax3 = get_soc_sec_tax(gross_pay3)
medicare_tax3 = get_medicare_tax(gross_pay3)
federal_tax3 = get_federal_tax(gross_pay3, withholding_code3)

print(f"Person 1: Gross Pay = ${gross_pay1}, SS Tax = ${soc_sec_tax1:.2f}, Medicare Tax = ${medicare_tax1:.2f}, Federal Tax = ${federal_tax1:.2f}")
print(f"Person 2: Gross Pay = ${gross_pay2}, SS Tax = ${soc_sec_tax2:.2f}, Medicare Tax = ${medicare_tax2:.2f}, Federal Tax = ${federal_tax2:.2f}")
print(f"Person 3: Gross Pay = ${gross_pay3}, SS Tax = ${soc_sec_tax3:.2f}, Medicare Tax = ${medicare_tax3:.2f}, Federal Tax = ${federal_tax3:.2f}")
