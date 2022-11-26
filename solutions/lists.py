l = []

def processCMDs(cmds):
    for cmd in cmds:
        commands = cmd.split(' ')
        command = commands[0]
        assert command in ["print", "sort", "pop", "reverse", "insert", "remove", "append"]
        if command == "print":
            print(l)
        elif command == "sort":
            l.sort()
        elif command == "pop":
            l.pop(len(l) - 1)
        elif command == "reverse":
            l.reverse()
        else:
            assert len(commands) > 1
            if command == "insert":
                assert len(commands) > 2
                i = int(commands[1])
                e = int(commands[2])
                l.insert(i, e)
            else:
                e = int(commands[1])
                if command == "remove":
                    l.remove(e)
                elif command == "append":
                    l.append(e)

if __name__ == '__main__':
    
    cmds = []
    N = int(input())
    for _ in range(N):
        cmds.append(input())
    
    processCMDs(cmds)