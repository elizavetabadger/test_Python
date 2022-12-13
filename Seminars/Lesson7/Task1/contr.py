import viem as vi
import operat as opp
import my_del as dl
import log

def main():
    string = vi.inp() # 1 + 2
    print(string)
    a, b, op = dl.opi(string)
    if op == "+":
        res = opp.summ(a, b)
    elif op == "-":
        res = opp.diff(a, b)
    elif op == "*":
        res = opp.mult(a, b)
    else:
        res = opp.div(a, b)
    log.log(a, b, op, res)
    vi.viem_data(res)