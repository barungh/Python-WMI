from openpyxl import Workbook
from thewmi import comp_info, os_info, b_board, net_info, sys_drive_check

n = input("Input excel file name to save data : ")
filename = f'{n}.xlsx'


def output_excel():
    wb = Workbook()
    sheet = wb.active
    sheet.title = "sys_info"

    def sa(title, value):
        sheet.append([title, value])

    oi = os_info()
    sa("Operating System", oi[0])
    sa("Version", oi[1])
    sa("Hostname", oi[2])
    sa("OS Architecture", oi[4])
    sa("Logged User", oi[5])

    ci = comp_info()
    sa("Part of domain ?", ci[6])
    sa("System Architecture", ci[10])
    sa("Total Physical Memory", f'{ci[11]} GB')

    bbi = b_board()
    sa("Serial Number", bbi[-1])
    sa("Make", bbi[0])
    sa("Model", bbi[1])

    ninfo = net_info()
    sa("IP Address", ninfo[1])
    sa("MAC", ninfo[2])

    sa("OS Drive free ", sys_drive_check())

    wb.save(filename)
    print("Excel file generated successfully")
    return

output_excel()



def output():
    oi = os_info()

    os = oi[0]
    version = oi[1]
    hostname = oi[2]
    os_arch = oi[4]
    reg_user = oi[5]

    ci = comp_info()
    part_of_domain = ci[6]
    sys_arch = ci[10]
    total_mem = ci[11]

    bbi = b_board()
    sn = bbi[-1]
    make = bbi[0]
    model = bbi[1]

    ninfo = net_info()

    ip = ninfo[1]
    mac = ninfo[2]

    sys_drive_status = sys_drive_check()

    return [sn, make, model, hostname, os, version, os_arch, sys_arch, reg_user, ip, mac, sys_drive_status, part_of_domain, total_mem]

# for i in output():
#     print(i)

