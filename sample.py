def clean_customer(raw):
    fields = raw.split(';')
    if len(fields) != 4:
        return None
    
    name_raw, email_raw, phone_raw, city_raw = fields
    
    # A. Clean and Validate Name & City
    name = name_raw.strip()
    name_words = name.split()
    if not name_words:
        return None
    for word in name_words:
        if not word.isalpha():
            return None
    cleaned_name = ' '.join([w.capitalize() for w in name_words])
    
    city = city_raw.strip()
    if not city:
        return None
    city_words = city.split()
    for word in city_words:
        if not word.isalpha():
            return None
    cleaned_city = ' '.join([w.capitalize() for w in city_words])
    
    # B. Clean and Validate Email
    email = email_raw.strip().lower()
    if email.count('@') != 1:
        return None
    parts = email.split('@')
    if not parts[0] or not parts[1]:
        return None
    domain = parts[1]
    if '.' not in domain:
        return None
    if domain.startswith('.') or domain.endswith('.'):
        return None
        
    # C. Clean and Validate Phone Number
    phone = phone_raw.strip().replace(' ', '').replace('-', '')
    if phone.startswith('+91'):
        phone = phone[3:]
    if len(phone) == 12 and phone.startswith('91'):
        phone = phone[2:]
        
    if len(phone) != 10 or not phone.isdigit():
        return None
    if phone[0] not in ('6', '7', '8', '9'):
        return None
        
    return {
        'name': cleaned_name,
        'email': email,
        'phone': phone,
        'city': cleaned_city
    }


# --- Processing Loop & Test ---
lines = [ 
    ' asha VERMA ; ASHA.V@Example.COM ; +91 98765-43210 ;pune ', 
    'ravi kumar;ravi@@corp.in;9123456780;Mumbai', 
    'meera;meera@mail;9123456780;Delhi', 
    'john doe; john@x.org ;12345; Goa', 
    'Neha Rao;neha.rao@firm.co.in;919876501234;nashik', 
    'amit;amit@site.com;9876543210' 
] 

rejected_count = 0

for line in lines:
    result = clean_customer(line)
    if result:
        print(result)
    else:
        rejected_count += 1

print(f"Rejected: {rejected_count}")