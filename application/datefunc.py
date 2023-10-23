from datetime import date, timedelta

latest = date.today() + timedelta(1)
earliest = date(2022, 11, 1)

# def get_years():
#     years = []
#     year = earliest.year
#     while year <= latest.year:
#         years.append(year)
#         year += 1
#     return years


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
