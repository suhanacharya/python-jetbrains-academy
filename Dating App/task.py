def select_dates(potentional_dates):
    names = ""
    for person in potentional_dates:
        if person.get("age") >= 30:
            if "art" in person.get("hobbies"):
                if person.get("city") == "Berlin":
                    names += person.get("name") + ", "

    return names.rstrip(", ")


# print(select_dates(potentional_dates))
