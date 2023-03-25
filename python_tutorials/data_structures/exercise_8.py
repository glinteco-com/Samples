def sort_names_by_age(lst):
    return [tup[0] for tup in sorted(lst, key=lambda tup: tup[1])]
