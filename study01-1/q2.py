plotlist = []
while True:
    count = 0
    line = input("줄거리 한 줄을 1000자 이하로 입력해주세요. : ")
    if len(line) > 1000:
        print("문장의 길이는 1000이하여야 합니다.")
        continue
    if line == "0":
        break
    else:
        plotlist.append(line)
        count += 1
        continue

while True:
    WHO = input("WHO : ")
    if "WHO" in WHO or "WHERE" in WHO or "WHAT" in WHO:
        print("WHO 안에는 WHO, WHERE, WHAT이 들어갈 수 없습니다.")
        continue
    else:
        break

while True:
    WHERE = input("WHERE : ")
    if "WHERE" in WHERE or "WHAT" in WHERE:
        print("WHERE 안에는 WHERE, WHAT이 들어갈 수 없습니다.")
        continue
    else:
        break

WHAT = input("WHAT : ")

if "WHERE" in WHAT:
    WHAT.replace("WHERE", WHERE)
if "WHO" in WHAT:
    WHAT.replace("WHO", WHO)
if "WHO" in WHERE:
    WHERE.replace("WHO", WHO)

print(plotlist)
print("-----")
for plot in plotlist:
    print(
        plot.replace("WHAT", f"{WHAT}")
        .replace("WHERE", f"{WHERE}")
        .replace("WHO", f"{WHO}")
    )
