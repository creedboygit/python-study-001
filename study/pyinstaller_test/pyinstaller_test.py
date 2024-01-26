import openpyxl

wb = openpyxl.Workbook()

ws = wb.active

ws.title = "pyinstaller 테스트"

wb.save("pyinstaller 테스트.xlsx")
