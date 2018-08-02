import xlrd

def guide(gamename):
    path = (r"path")
    games = xlrd.open_workbook(path)
    sheet = games.sheet_by_index(0)

    for row in range(sheet.nrows):
        for col in range(sheet.ncols):
            if sheet.cell_value(row, col) == gamename:
                return sheet.cell_value(row, col + 1)
