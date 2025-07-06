import random
import sys

# This esoland is made in a way of descriping my love for cyber security, and most of these commands are simulating the real. For example, ddos: is a real attack that depends on rapid overwhelming, so it is made as a command to increase the value rapidly by 10

# = Global State
value = 0
memory = {}
history = []
last_store_index = None

# = Command Functions

def ping(): # INCREASES the value by 1
    global value
    value += 1

def ddos(): # INCREASES the value by 10
    global value
    value += 10

def dec(): # DECRESES the value by 1
    global value
    value -= 1

def zero(): #SETS the value to 0
    global value
    value = 0

def payload(): # SQUARES the value
    global value
    value = value ** 2

def decrypt(): # DIVIDE the value by 2
    global value
    value = value // 2

def virus(): # RANDOMIZED the value between 0 and 100
    global value
    value = random.randint(0, 100)
    print(f"Virus injected → value is now {value}")

def rm_rf(): # CLEARS the value
    global value, memory
    value = 0
    memory.clear()
    print("System wiped")

def sql_inject(): # PRINTS the current value
    print(f"Output: {value}")

def keylogger(): # TAKES the value from the user
    global value
    try:
        user_input = input("Enter a number: ").strip()
        value = int(user_input)
        print(f"Value is now {value}")
    except ValueError:
        print("Invalid input. Value set to 0.")
        value = 0

def scanports(): # RANDOMIZED the value from 1 to 10
    global value
    ports = random.randint(1, 10)
    value += ports
    print(f"Found {ports} open ports. Value is now {value}")

def log(): # PRINTS the previous stores commands
    print(f"value = {value} | memory = {memory}")

def exit_program(): # for EXIT
    print("Exiting ScriptKid. Stay shady, kid.")
    sys.exit()

def crash(): # CRASHcrash
    print("SYSTEM CRASHED. Goodbye.")
    sys.exit()

def firewall(): # SKIPS the next command
    input("Firewall active. Press enter to skip next command...")

def store(arg): # STORES the current value in a virtual file
    global last_store_index
    memory[arg] = value
    last_store_index = len(history) - 1
    print(f"Stored {value} in '{arg}'")

def load(arg): # LOADS the stored specific value
    global value
    value = memory.get(arg, 0)
    print(f"Loaded '{arg}' = {value}")

def swap(arg): # SWAPS between stored values
    global value
    temp = value
    value = memory.get(arg, 0)
    memory[arg] = temp
    print(f"Swapped value with '{arg}'")

def clear(arg):
    if arg in memory:
        del memory[arg]
        print(f"Cleared memory '{arg}'")
    else:
        print(f"'{arg}' not found in memory")

def print_text(arg):
    print(arg.strip('"'))

def backdoor(): # MAKES the last store command
    if last_store_index is not None and 0 <= last_store_index < len(history):
        return history[last_store_index]
    return None

   # I am tired of explaning, I hope you get the rest.
def bruteforce():
    if len(history) >= 2:
        return history[-2]
    return None

def nmap(arg):
    try:
        target = int(arg)
        if 0 <= target < len(history):
            return history[target]
    except:
        pass
    return None

def ifzero(arg):
    global value
    if value == 0:
        return nmap(arg)
    return None

def loop(arg):
    try:
        count = int(arg)
        if len(history) > 1:
            last = history[-2]
            for _ in range(count - 1):
                run_command(last)
    except:
        print("Invalid loop count")


commands = {
    'ping': ping,
    'ddos': ddos,
    'dec': dec,
    'zero': zero,
    'payload': payload,
    'decrypt': decrypt,
    'virus': virus,
    'rm -rf /': rm_rf,
    'sql_inject': sql_inject,
    'keylogger': keylogger,
    'scanports': scanports,
    'log': log,
    'exit': exit_program,
    'crash': crash,
    'firewall': firewall,
    'backdoor': lambda: run_command(backdoor()),
    'bruteforce': lambda: run_command(bruteforce()),
}

# = Command Dispatcher
def run_command(line):
    if not line:
        return

    history.append(line)
    parts = line.strip().split(' ', 1)
    cmd = parts[0]
    arg = parts[1] if len(parts) > 1 else None


    if cmd in commands:
        commands[cmd]()
    elif cmd == 'store' and arg:
        store(arg)
    elif cmd == 'load' and arg:
        load(arg)
    elif cmd == 'swap' and arg:
        swap(arg)
    elif cmd == 'clear' and arg:
        clear(arg)
    elif cmd == 'print' and arg:
        print_text(arg)
    elif cmd == 'nmap' and arg:
        new_cmd = nmap(arg)
        if new_cmd: run_command(new_cmd)
    elif cmd == 'ifzero' and arg:
        new_cmd = ifzero(arg)
        if new_cmd: run_command(new_cmd)
    elif cmd == 'loop' and arg:
        loop(arg)
    else:
        print(f"oops, are you sure from what you wrote?: {cmd}")

# = REPL
def run_scriptkid():
    print("\nWelcome to ScriptKid Interactive Console")
    print("Type 'exit' to quit.\n")

    while True:
        try:
            line = input(" > ").strip()
            run_command(line)
        except KeyboardInterrupt:
            print("\nUse 'exit' to quit.")
        except Exception as e:
            print(f"I think you entered it wrong!: {e}")

if __name__ == "__main__":
    run_scriptkid()
