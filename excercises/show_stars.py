def show_stars(rows):
    if rows == 1:
        print("*")
        return
    show_stars(rows - 1)
    print("*" * rows)
    return


show_stars(12)


def show(rows):
    if rows != 0:
        row_num = show(rows - 1)
        print("*" * (row_num + 1))
    return rows


show(21)
