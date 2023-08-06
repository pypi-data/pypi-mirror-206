import datetime

def GetMonthDate(mymonth):
  mth = mymonth.split(" ")
  yr = mth[1]
  month_name = str(mth[0])
  month_num = datetime.datetime.strptime(month_name, '%B').month
  mn = str(month_num).zfill(2)
  full_date = str(yr) + "-" + mn + "-01 " + "00:00:00"
  return full_date

def SetFinancialMonth(month_date):
    month = month_date.split("-")
    m_num = int(month[1])
    if m_num <= 3:
        f_month = m_num + 9
    else:
        f_month = m_num - 3
    return f_month
# TODO: allow starting month to be set dynamically

def SetFinancialYear(month_date,mode):

    # mode 1 creates date as 202122
    # mode 2 creates date as 2021-22
    # mode 3 creates date as 2122

    month = month_date.split("-")
    m_num = int(month[1])
    
    if m_num > 3:
        y = (int(month[0]) - 2000)+1 #to calc fy
        if mode == 1:
            fy = str(month[0]) + str(y)
        elif mode == 2:
            fy = str(month[0]) + '-' + str(y)
        elif mode == 3:
            fy = str(int(month[0]))[-2:] + str(y)[-2:]
    else:
        y = (int(month[0]) - 2000)-1 #to calc fy
        if mode == 1:
            fy = str(int(month[0])-1) + str(month[0])[-2:]
        elif mode == 2:
            fy = str(int(month[0])-1) + '-' + str(month[0])[-2:] #used for the edict file
        elif mode == 3:
            fy = str(int(month[0])-1)[-2:] + str(month[0])[-2:]
    return fy

def GetMonthNameByFMShort(mn):
    mn_dict ={
        "01": "Apr",
        "02": "May",
        "03": "Jun",
        "04": "Jul",
        "05": "Aug",
        "06": "Sep",
        "07": "Oct",
        "08": "Nov",
        "09": "Dec",
        "10": "Jan",
        "11": "Feb",
        "12": "Mar"
    }

    return mn_dict[mn]