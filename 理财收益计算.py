rate = float(input("年利率："))
principal = float(input("本金："))
period = int(input("理财周期："))
numbers = int(input("购买期数："))
summary = 0
n = 1

def calu():
    global n
    global summary
    global principal
    if n > numbers:
        return
    interest = principal * (rate * period / 365) /100
    print("第%d期收益:%f" % (n , interest))
    summary += interest
    principal += interest
    n += 1
    calu()

if __name__ == "__main__":

    calu()
    print("总收益：%f" % (summary))
    print("总额：%f" % (principal))
