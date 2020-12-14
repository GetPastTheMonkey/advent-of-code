from utils import get_input_lines

memory = dict()
mask = ["0"] * 36

for line in get_input_lines(__file__):
    x, y = line.split(" = ")
    if x == "mask":
        mask = list(y)
    else:
        val = int(y)
        base_addr = list("{0:036b}".format(int(x[4:-1])))
        final_addr = [base_addr]

        for idx, m in enumerate(mask):
            if m == "1":
                new_f_a_list = []
                for f_a in final_addr:
                    new_f_a = f_a.copy()
                    new_f_a[idx] = "1"
                    new_f_a_list.append(new_f_a)
                final_addr = new_f_a_list
            elif m == "X":
                new_f_a_list = []
                for f_a in final_addr:
                    new_f_a = f_a.copy()
                    new_f_a[idx] = "0"
                    new_f_a_list.append(new_f_a)

                    new_f_a = f_a.copy()
                    new_f_a[idx] = "1"
                    new_f_a_list.append(new_f_a)
                final_addr = new_f_a_list

        for f_a in final_addr:
            memory["".join(f_a)] = val

print(sum(memory.values()))
