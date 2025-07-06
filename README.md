# ScriptKiddy

> A hacker-themed esolang (esoteric programming language) made by real cybersecurity actions.  
> Every command simulates a real-world cyber concept like `ddos`, `payload`, `keylogger`, and more — with logic that *makes sense to a script kiddie*.

---

## Why ScriptKid?

This esolang is my playful contribute to cybersecurity.  
It interprets commands as if they were real hacking tools — simulating the behavior you'd expect from cyber attacks and exploits.

Every Command in this esoland simulates a real concept in real Cybersecurity, like ddos, keylogger, nmap, and more.

Still Confused? here is some examples of what I mean:
ddos in real depends mainly on sudden overwhelming, so in this esolang, it increaes the current value suddenly by 10
nmap in real is mainly used for enumeration and mapping, so in this esoland, it mapps for command in specific lines

---

## How It Works

- There's a single variable: `value`.
- Most commands manipulate `value` or memory.
- All commands are typed interactively in the terminal.
- Some commands take arguments (like `store`, `load`, etc.).
- Run it using Python 3:  
  ```bash
  python3 scriptkid.py 

_

  ##  Command Reference

| Command           | Description                                                                 |
|-------------------|-----------------------------------------------------------------------------|
| `ping`            | Increases `value` by 1 (basic connectivity check)                           |
| `ddos`            | Increases `value` by 10 (simulate overwhelming a system)                    |
| `dec`             | Decreases `value` by 1                                                      |
| `zero`            | Sets `value` to 0                                                           |
| `payload`         | Squares the value (`value = value^2`)                                       |
| `decrypt`         | Halves the value (integer division by 2)                                    |
| `virus`           | Randomizes `value` between 0 and 100                                        |
| `rm -rf /`        | Wipes the system: clears `value` and all memory                             |
| `sql_inject`      | Prints the current `value`                                                  |
| `keylogger`       | Prompts user to enter a number and sets `value` to it                       |
| `scanports`       | Randomly increases `value` by 1–10                                          |
| `store <name>`    | Stores the current value under the given name                               |
| `load <name>`     | Loads a stored value into `value`                                           |
| `swap <name>`     | Swaps current value with the one in memory                                  |
| `clear <name>`    | Deletes a stored variable from memory                                       |
| `print "<text>"`  | Prints custom text to the terminal                                          |
| `log`             | Shows the current value and memory state                                    |
| `exit`            | Exits the ScriptKid console                                                 |
| `crash`           | Simulates a full crash and exits                                            |
| `firewall`        | Skips the next command (simulate a block)                                   |
| `backdoor`        | Jumps back to the last `store` command                                      |
| `bruteforce`      | Repeats the last command (again and again)                                  |
| `nmap <line>`     | Jumps to and executes the Nth command from the history                      |
| `ifzero <line>`   | If `value == 0`, jumps to and runs Nth command                              |
| `loop <num>`      | Repeats the previous command N times                                        |


## Sample Session

> ping

> ddos

> sql_inject

> Output: 11

> virus

> Virus injected → value is now 47

> store secret

> zero

> load secret

> Loaded 'secret' = 47

> payload

> sql_inject

> Output: 2209


## Insallation:
Make sure you have installed python

```
git clone https://github.com/yourusername/scriptkid
```
```
cd scriptkid 
```
``` 
python3 scriptkid.py
```

