# Strings and Text

# Example 1
MyName = "My name is {}"
print(MyName.format("Achmad Noorafzam"))
print(f"My name is {'Achmad Noorafzam'} <-- Guna f-string") # Guna f-string

# Example 2
umur = 2025 - 1989
template1 = "{} berumur {} tahun"
Nama = "Bobby"
print(template1.format(Nama, umur))
print(f"{Nama} berumur {umur} tahun <-- Guna f-string") # Guna f-string

# Example 3
template2 = "{1} adalah anak kepada {0}."
print(template2.format("Ali", "Abu")) # f-string tidak mengenal posisi pernomboran

# Real world application example
# Sales Report

product = "Laptop"
quantity = 5
price = 4500

report = "Anda telah membeli {} sebanyak {} dengan harga RM{}."
print(report.format(product, quantity, price * quantity))
print(f"Anda telah membeli {product} sebanyak {quantity} dengan harga RM{price * quantity} <-- Guna f-string")

# Notification Example

nama_pelanggan = "Achmad Noorafzam"
tarikh_penghantaran = "17 Jun 2025"
nombor_invoice = "INV1234"

mesej = """
Hello {}! tempahan (#{}) telah dihantar pada {}.
Terima kasih kerana telah menggunakan perkhidmatan kami.
"""

print(mesej.format(nama_pelanggan, nombor_invoice, tarikh_penghantaran))
# TODO: Sila buat versi f-string

# Command Line (CLI) Progress Bar

progress = 0.5 # nilai 1 adalah 100%
print("Progress: [{:<20}] {:.1%}".format("="*int(progress*20), progress))
print(f"Progress: [{'=' * int(progress * 20):<20}] {progress:.1%} <-- Guna f-string") #Guna f-string

# Dynamic HTML generation
tag = "div"
content = "Selamat datang"
attributes = {'class': 'header', 'id': 'welcome-msg'}

html = "<{tag} {attrs}>{content}</{tag}>".format(
    tag=tag,
    attrs=" ".join(f'{key}="{value}"' for key,value in attributes.items()),
    content=content
)
print(html)
