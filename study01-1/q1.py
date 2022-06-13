while True:
    try:
        timeToSleep = int(input("일주일 목표 수면 시간을 입력하세요. (0 이상 168이하의 정수를 입력하세요.) : "))
    except ValueError:
        print("숫자를 입력해주세요.")
        continue
    else:
        if not 0 <= timeToSleep <= 168:
            print("잘못 입력하셨습니다. 0이상, 168이하의 정수를 입력하세요.")
            continue
        else:
            break

while True:
    try:
        numOfSleep = int(input("평일에 잠을 잔 횟수를 입력하세요. (0 이상 10이하의 정수를 입력하세요.) : "))
    except ValueError:
        print("숫자를 입력해주세요.")
        continue
    else:
        if not 0 <= numOfSleep <= 10:
            print("잘못 입력하셨습니다. 0이상, 10이하의 정수를 입력하세요.")
            continue
        else:
            break

week = ["월", "화", "수", "목", "금"]
sleeplist = []
sleeptime = []
wakelist = []
waketime = []
sleephour = 0

if numOfSleep != 0:
    print("--------------------------------------------------------------------------")
    print("시작합니다. 월요일부터 시작하는 요일로 가장 빠른 날짜부터 순서대로 입력해주세요.")
    print("--------------------------------------------------------------------------")

for i in range(numOfSleep):
    while True:
        sl = input(f"{i+1}번째 잠든 요일을 입력하세요. (월, 화, 수, 목, 금) : ")
        if not sl in week:
            print("----에러----")
            print("요일을 잘못 입력하셨습니다.")
            continue
        else:
            if i > 0:
                if week.index(sl) < week.index(sleeplist[i - 1]):
                    print("----에러----")
                    print("이전 잠든 요일보다 과거를 입력하였습니다. 다시 입력해주세요.")
                    continue
                else:
                    sleeplist.append(sl)
                    break
            else:
                sleeplist.append(sl)
                break

    while True:
        try:
            st = int(input(f"{sleeplist[i]}요일 몇시에 잠에 들었나요? (0이상 23이하의 정수로 입력하세요.) : "))
        except ValueError:
            print("----에러----")
            print("숫자를 입력해주세요.")
            continue
        else:
            if 0 <= st <= 23:
                if i > 0:
                    if sl == wakelist[i - 1]:
                        if st < waketime[i - 1]:
                            print("----에러----")
                            print("잠든시간이 직전의 일어난 시간보다 과거일 수 없습니다.")
                            continue
                        else:
                            sleeptime.append(st)
                            break
                    else:
                        sleeptime.append(st)
                        break
                else:
                    sleeptime.append(st)
                    break
            else:
                print("----에러----")
                print("시간을 잘못 입력하셨습니다.")
                continue

    while True:
        wl = input(f"{i+1}번째 일어난 요일을 입력하세요. (월, 화, 수, 목, 금) : ")
        if not wl in week:
            print("----에러----")
            print("요일을 잘못 입력하셨습니다.")
            continue
        else:
            if week.index(wl) < week.index(sleeplist[i]):
                print("----에러----")
                print("일어난 요일이 잠 든 요일보다 과거일 수 없습니다.")
                continue
            else:
                wakelist.append(wl)
                break

    while True:
        try:
            wt = int(input(f"{wakelist[i]}요일 몇시에 일어났나요? (0이상 23이하의 정수로 입력하세요) : "))
        except ValueError:
            print("----에러----")
            print("숫자를 입력해주세요.")
            continue
        else:
            if wt < 0 or wt > 23:
                print("----에러----")
                print("시간을 잘못 입력하셨습니다.")
                continue
            else:
                if week.index(wl) == week.index(sl):
                    if wt <= st:
                        print("----에러----")
                        print("일어난 시각이 잠든 시각과 같거나 과거일 수 없습니다.")
                        continue
                    else:
                        waketime.append(wt)
                        break
                else:
                    waketime.append(wt)
                    break

    if sleeplist[i] == wakelist[i]:
        sleephour += waketime[i] - sleeptime[i]
    else:
        sleephour += 24 - sleeptime[i] + waketime[i]

if numOfSleep != 0:
    print("-------------입력------------")
for i in range(numOfSleep):
    print(
        f"{i+1}번째 잠 : {sleeplist[i]}요일 {sleeptime[i]}시에 자서 {wakelist[i]}요일 {waketime[i]}시에 일어남"
    )

print("-------------결과------------")
print("잔 시간 : ", sleephour)
print("목표 수면 시간 : ", timeToSleep)

if sleephour > timeToSleep:
    print("0, 잠 안자도 됨")
elif timeToSleep - sleephour > 48:
    print("-1, 주말 내내 자도 불충분")
else:
    print(f"{timeToSleep - sleephour}시간 더 자야함")
