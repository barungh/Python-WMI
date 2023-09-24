import wmi

conn = wmi.WMI()

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
            ("{:.2f}".format(int(cs.TotalPhysicalMemory)/1024/1024/1024)),
            cs.UserName,
            cs.Workgroup
            ]

def os_info():
    n = conn.Win32_OperatingSystem()
    os_name = n[0].Caption
    version = n[0].BuildNumber
    host = n[0].CSName
    free_mem = n[0].FreePhysicalMemory
    free_mem = "{:.2f}".format((int(free_mem))/1024/1024)
    os_arc = n[0].OSArchitecture
    userName = n[0].RegisteredUser
    system_drive = n[0].SystemDrive

    return [os_name, version, host, free_mem, os_arc, userName, system_drive]

def b_board():
    m = conn.Win32_Baseboard()[0].Manufacturer
    p = conn.Win32_Baseboard()[0].Product
    s = conn.Win32_Baseboard()[0].SerialNumber
    return [m,p,s]

def net_info():
    n = conn.Win32_NetworkAdapterConfiguration()
    for i in n:
        if i.IPEnabled:
            d = i.Description
            ip = i.IPAddress[0]
            mac = i.MACAddress
            return [d, ip, mac]

def hdd_info():
    disk_info = {}

    for i in conn.Win32_LogicalDisk():
        caption = i.Caption
        Did = i.DeviceID
        free = i.FreeSpace
        name = i.Name
        size = i.Size
        vName = i.VolumeName
        freePercent = "{:.2f}%".format((int(free) / int(size))*100)
        disk_info[Did] = [caption, Did, free, name, size, vName, freePercent]

    return disk_info

def sys_drive_check():
    sys_drive = os_info()[-1]
    for key, value in hdd_info().items():
        if (key == sys_drive):

            return value[-1]
