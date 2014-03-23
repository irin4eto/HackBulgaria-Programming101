def what_is_my_sign(day, month):
    signs = { (3, range(21, 32)): "Aries", (4, range(1, 21)): "Aries",
              (4, range(21, 31)): "Taurus", (5, range(1, 21)): "Taurus",
              (5, range(21, 32)): "Gemini", (6, range(1, 21)): "Gemini",
              (6, range(21, 31)): "Cancer", (7, range(1, 21)): "Cancer",
              (7, range(22, 32)): "Leo", (8, range(1, 23)): "Leo",
              (8, range(23, 32)): "Virgo", (9, range(1, 23)): "Virgo",
              (9, range(23, 31)): "Libra", (10, range(1, 23)): "Libra",
              (10, range(23, 32)): "Scorpio", (11, range(1, 22)): "Scorpio",
              (11, range(22, 31)): "Sagittarius", (12, range(1, 22)): "Sagittarius",
              (12, range(22, 32)): "Capricorn", (1, range(1, 20)): "Capricorn",
              (1, range(20, 32)): "Aquarius", (2, range(1, 19)): "Aquarius",
              (2, range(19, 30)): "Pisces", (3, range(1, 21)): "Pisces" }

    for key in signs.keys():
        if month == key[0] and day in key[1]:
            return signs[key]
