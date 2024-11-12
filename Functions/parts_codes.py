def get_supplier_code(part_code):
    return part_code.split(':')[0]

def get_product_num(part_code):
    return part_code.split(':')[1].split('-')[0]

def get_size(part_code):
    return part_code.split('-')[1]

#Exampled part codes
part_codes = [
    "ACME:123-L",
    "DI:12345-M",
    "ACE:1-12"]

#Display results
for code in part_codes:
    supplier = get_supplier_code(code)
    product_num = get_product_num(code)
    size = get_size(code)


print(f"Part Code: {code}")
print(f"Supplier: {supplier}")
print(f"Producr Number: {product_num}")
print(f"Size: {size}")
print()