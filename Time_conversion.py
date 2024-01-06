def view_selection():
    print("Enter--")
    print("1: To convert time from 12-hour notation to 24-hour notation.")
    print("2: To convert time from 24-hour notation to 12-hour notation.")
    print("99: To quit the program.")

def readUserValues():
    hr = int(input("Enter hours: "))
    min = int(input("Enter minutes: "))
    sec = int(input("Enter seconds: "))
    return hr, min, sec

def adjustTo24(hr, min, sec, span):
    if span == "PM" and hr != 12:
        hr += 12
    elif span == "AM" and hr == 12:
        hr = 0
    return hr, min, sec

def adjustTo12(hr, min, sec):
    span = "AM"
    if hr >= 12:
        span = "PM"
        if hr > 12:
            hr -= 12
    elif hr == 0:
        hr = 12
    return hr, min, sec, span

def showOutcome(hr, min, sec, span=None):
    if span:
        print(f"The time is: {hr:02d}:{min:02d}:{sec:02d} {span}")
        print()
    else:
        print(f"The time is: {hr:02d}:{min:02d}:{sec:02d}")
        print()

def main():
    while True:
        view_selection()
        userSelection = int(input())
        if userSelection == 99:
           break
        print()
        hr, min, sec = readUserValues()
        if userSelection == 1:
            span = input("Enter AM/PM: ")
            hr, min, sec = adjustTo24(hr, min, sec, span)
            print()
            showOutcome(hr, min, sec)
        elif userSelection == 2:
            hr, min, sec, span = adjustTo12(hr, min, sec)
            print()
            showOutcome(hr, min, sec, span)

main()