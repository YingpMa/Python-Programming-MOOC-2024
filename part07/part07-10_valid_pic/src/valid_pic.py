# Write your solution here
def is_it_valid(pic: str):
    from datetime import datetime, date
    day = int(pic[0:2])
    month = int(pic[2:4])
    string = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    if len(pic) != 11:
        return False
    if pic[6] == "+":
        year = 1800 + int(pic[4:6])
    elif pic[6] == "-":
        year = 1900 + int(pic[4:6])
    elif pic[6] == "A":
        year = 2000 + int(pic[4:6])
    else:
        return False
    
    try:
        date(year, month, day)
        pass
    except ValueError:
        return False
    
    numebr = int(pic[0:6] + pic[7:10])
    m = numebr % 31
    if string[m] == pic[-1]:
        return True 
    else:
        return False

if __name__ == "__main__":
    print(is_it_valid("030103A493DD"))
    