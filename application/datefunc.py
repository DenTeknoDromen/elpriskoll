from datetime import date, timedelta

latest = date.today() + timedelta(1)
earliest = date(2022, 11, 1)

# Verifierar att angivet datum fungerar
# Returnerar bool
def verify_date(form_date):
    try:
        input_date = date.fromisoformat(form_date)
    except Exception as e:
        return False
    if input_date > latest or input_date < earliest:
        return False
    
    return True

def get_currdate():
    return str(date.today())

print(type(get_currdate()))