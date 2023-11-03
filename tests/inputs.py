from datetime import date, timedelta

class Inputs:
    def __init__(self):
        # Skapar datum för testning
        future = date.today() + timedelta(2)
        past = date(2022,11,1)

        # Skapar en lång sträng för testning
        toolong = "tralala"
        for x in range(10000):
            toolong += "la"

        # Lista med inputs som INTE ska funka
        wronginputs = ["23-24-62", "1995-11-25", 
                    "2022-10-31", "Wrong input", 
                    "-2023-10-31", "2023-31-10", 
                    "2023-10-31T14:30:43", "23-10-31", 
                    str(future), toolong, 
                    "<h1>HTML Injection testing</h1>", 
                    "<script></script>"
                    ]

        # Lista med med datum som ska funka
        correctinputs = []
        while past != future:
            print(str(past))
            correctinputs.append(str(past))
            past += timedelta(1)

        #Lista med alla korrekta prisklasser
        pricegroups = ["SE1", "SE2", "SE3", "SE4"]
        pricegroups_2 = ["SE1", "SE2", "SE3", "SE4", "No "]
        self.inputs = {"correctinputs": correctinputs, 
                       "wronginputs": wronginputs,
                       "pricegroups": pricegroups, 
                       "pricegroups_2": pricegroups_2}