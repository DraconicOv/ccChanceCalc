import matplotlib.pyplot as plt
import json
import re
#total 500k,8711931000 cc
#data from 100 summons
data = {"1000": 17849, "2000": 33339, "3000": 31154, "4000": 14777, "5000": 27978, "6000": 26183, "7000": 12252, "8000": 23157, "9000": 21631, "10000": 10104, "11000": 19326, "12000": 18367, "13000": 8774, "14000": 16109, "15000": 15113, "16000": 7098, "17000": 13545, "18000": 12577, "19000": 5957, "20000": 11325, "21000": 10755, "22000": 5039, "23000": 9437, "24000": 9024, "25000": 4268, "26000": 8005, "27000": 7388, "28000": 3474, "29000": 6685, "30000": 6183, "31000": 2900, "32000": 5505, "33000": 5285, "34000": 2441, "35000": 4615, "36000": 4319, "37000": 2122, "38000": 3820, "39000": 3573, "40000": 1654, "41000": 3164, "42000": 3001, "43000": 1489, "44000": 2762, "45000": 2465, "46000": 1233, "47000": 2311, "48000": 2167, "49000": 998, "50000": 1916, "51000": 1740, "52000": 865, "53000": 1522, "54000": 1482, "55000": 714, "56000": 1295, "57000": 1287, "58000": 588, "59000": 1021, "60000": 1046, "61000": 496, "62000": 938, "63000": 903, "64000": 405, "65000": 730, "66000": 754, "67000": 328, "68000": 683, "69000": 603, "70000": 259, "71000": 518, "72000": 522, "73000": 244, "74000": 446, "75000": 382, "76000": 203, "77000": 399, "78000": 348, "79000": 179, "80000": 327, "81000": 293, "82000": 133, "83000": 244, "84000": 252, "85000": 120, "86000": 209, "87000": 211, "88000": 85, "89000": 192, "90000": 171, "91000": 77, "92000": 144, "93000": 151, "94000": 68, "95000": 120, "96000": 126, "97000": 51, "98000": 109, "99000": 93, "100000": 40, "101000": 97, "102000": 90, "103000": 33, "104000": 82, "105000": 74, "106000": 29, "107000": 57, "108000": 70, "109000": 22, "110000": 51, "111000": 40, "112000": 25, "113000": 28, "114000": 40, "115000": 12, "116000": 29, "117000": 33, "118000": 17, "119000": 29, "120000": 40, "121000": 9, "122000": 23, "123000": 22, "124000": 12, "125000": 26, "126000": 17, "127000": 9, "128000": 18, "129000": 20, "130000": 6, "131000": 9, "132000": 27, "133000": 6, "134000": 10, "135000": 11, "136000": 4, "137000": 3, "138000": 7, "139000": 6, "140000": 12, "141000": 8, "142000": 3, "143000": 10, "144000": 9, "145000": 7, "146000": 5, "147000": 6, "148000": 3, "149000": 4, "150000": 4, "152000": 2, "153000": 5, "154000": 1, "155000": 1, "156000": 4, "157000": 2, "158000": 4, "159000": 4, "161000": 4, "162000": 2, "163000": 1, "164000": 1, "165000": 4, "167000": 2, "168000": 2, "169000": 1, "170000": 2, "171000": 1, "173000": 1, "175000": 1, "181000": 1, "182000": 1, "183000": 1, "185000": 1, "186000": 1, "189000": 1, "193000": 1, "194000": 1, "196000": 1, "204000": 1, "210000": 1, "242000": 1}
'''data = {}
with open('dict.json') as file:
     data = json.loads(file.read())
'''
xA,yA = zip(*data.items())
xA=list(xA)
yA=list(yA)

xA[:]=[int(x)/1000 for x in xA]
yA[:]=[(int(x)/500000)*100 for x in yA]
yAxis = yA

yA.append(0)
for i in range(len(yA)-1):
    yA[i] = yA[i]+yA[i-1]
yA.remove(0)

def get_cc_chance():
    cc = int(input("How many cc do you have?> "))
    chance = "That value didn't make sense to me, are you sure that you just put in a number?"
    if cc > xA[-1]*1000:
        chance = "Greater chance than I care to calculate, but prob more than " + str(yA[-1])
    else:
        for i in range(len(xA)-1):
            if cc-(xA[i]*1000) <= 999:
                chance = "About a " + str(int(yA[i])) + f"% chance. (Give or take .5%) \n"
                break
    print(chance)
    goAgain = input("\nCheck different cc value? (y/n)> ")
    if goAgain == "y" or goAgain =="Y":
        get_cc_chance()
    else:
        main()
        
def get_chance_cc():
    chance = float(input("What chance are you trying to find? > ").replace("%",""))
    cc = "That value didn't make sense to me, are you sure that you just put in a number? (Decimals ARE supported, but numbers over 100 aren't)"
    if chance >= 100:
        cc = "Value impossible"
    else:
        for i in range(len(yA)-1):
            if chance-(yA[i]) <= 0.5:
                cc = "About " + str(xA[i]) +"k cc, give or take. (off by up to 0.5%)"
                break
    print(cc)
    goAgain = input("\nCheck different chance cost? (y/n)> ")
    if goAgain == "y" or goAgain =="Y":
        get_chance_cc()
    else:
        main()

def main():
    which_function = input("Chance from cc (1), cc from chance (2), or just see graph (3)? > ")
    if which_function == "1":
        get_cc_chance()
    elif which_function == "2":
        get_chance_cc()
    elif which_function == "3":
        return
    else:
        print("Invalid input, try again. \n")
        main()
main()
seeGraph = input("See graph of chances? (y/n)> ")        
if seeGraph == "y" or seeGraph =="Y":
    plt.plot(xA,yAxis)
#plt.xticks([0,10,20,30,40,50,100,150,200,250])
    plt.title('Summons, total of 500k ultra pulls, cost ~8,711,931,000cc')
    plt.xlabel('Cost (in thousands)')
    plt.ylabel('People who got at that cost (in thousands)')
    plt.show()
