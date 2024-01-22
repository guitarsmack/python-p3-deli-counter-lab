def line(line):
    if len(line) > 0:
        names = ''
        for customer in line:
            names += f' {line.index(customer)+1}. {customer}'
        print(f'The line is currently:{names}')
    else:
        print("The line is currently empty.")

def take_a_number(line,name):
    line.append(name)
    print(f'Welcome, {name}. You are number {str(len(line))} in line.')


def now_serving(line):
    if len(line) > 0:
        print(f"Currently serving {line.pop(0)}.")
    else:
        print("There is nobody waiting to be served!")