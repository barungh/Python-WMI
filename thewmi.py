import wmi

# conn = wmi.WMI("192.168.0.108", user=r"tej", password="tej@108")
conn = wmi.WMI()

# for class_name in conn.classes:
    # if 'Process' in class_name:
    # print(class_name)

# print(wmi.WMI().Win32_Process.methods.keys())
# print(wmi.WMI().Win32_Process.properties.keys())


def comp_info():
    cs = conn.Win32_Computersystem()[0]
    return [
            cs.ChassisSKUNumber,
            cs.Domain,
            cs.Manufacturer,
            cs.Model,
            cs.Name,
            cs.OEMStringArray,
            cs.PartOfDomain,
            cs.PrimaryOwnerName,
            cs.SystemFamily,
            cs.SystemSKUNumber,
            cs.SystemType,
            cs.TotalPhysicalMemory,
            cs.UserName,
            cs.Workgroup
            ]


for i in (comp_info()):
    print(i)

# for i in conn.Win32_LogicalDisk():
#     print(i)

# l = conn.Win32_LogicalDisk()
#
# t = l[0]
#
# print(t.DeviceID)

# print(type(l))
#
# print(len(l))
#
# print(type(l[0]), type(l[1]))

# for i in conn.Win32_Baseboard():
#     print(i.properties)

# for n in conn.Win32_OperatingSystem():
#     print(n)
# n = conn.Win32_OperatingSystem()
# print(n[0])

# def os_info():
#     n = conn.Win32_OperatingSystem()
#     os_name = n[0].Caption
#     version = n[0].BuildNumber
#     host = n[0].CSName
#     free_mem = n[0].FreePhysicalMemory
#     free_mem = "{:.2f}".format((int(free_mem))/1024/1024)
#     os_arc = n[0].OSArchitecture
#     userName = n[0].RegisteredUser
#     system_drive = n[0].SystemDrive
#
#     return [os_name, version, host, free_mem, os_arc, userName, system_drive]
#
# for i in (os_info()):
#     print((i))


# def b_board():
#     m = conn.Win32_Baseboard()[0].Manufacturer
#     p = conn.Win32_Baseboard()[0].Product
#     s = conn.Win32_Baseboard()[0].SerialNumber
#     return [m,p,s]
#
# print(b_board())

# bb = conn.Win32_Baseboard()
# print(bb[0].Product)

# n = conn.Win32_NetworkAdapterConfiguration()

# print("Description", "\t\t\t", "Status")
# for i in n:
#     if i.IPEnabled:
#         d = i.Description
#         ip = i.IPAddress[0]
#         mac = i.MACAddress
#         print(d, ip, mac)
#         print(type(d), type(ip), type(mac))

        # print(i.Description, "\n", i.IPAddress[0], "\n", i.MACAddress, "\n")
        # print(i.Description, "\t\t\t", i.IPEnabled)
