import signal,os
import psutil
from enum import Enum

class Signal:

    def __init__(self,pid: str, sig: str):
        try:
            self.sig = self.s2s(sig)
        except Exception as e:
            print(e)
            
    def send(self,pid: str, sig: str):
        os.kill(int(pid), self.sig)
    def s2s(self,sig:str):
        match sig:
            case "SIGHUP":
                return signal.SIGHUP
            case "SIGINT":
                return signal.SIGINT
            case "SIGQUIT":
                return signal.SIGQUIT
            case "SIGILL":
                return signal.SIGILL
            case "SIGSEGV":
                return signal.SIGSEGV
            case "SIGPIPE":
                return signal.SIGPIPE
            case "SIGALRM":
                return signal.SIGALRM
            case "SIGTERM":
                return signal.SIGTERM
            case "SIGUSR1":
                return signal.SIGUSR1
            case "SIGUSR2":
                return signal.SIGUSR2
            case "SIGCHLD":
                return signal.SIGCHLD
            case "SIGCONT":
                return signal.SIGCONT
            case "SIGSTOP":
                return signal.SIGSTOP
            case "SIGTTIN":
                return signal.SIGTTIN
            case "SIGTTOU":
                return signal.SIGTTOU
            case default:
                raise(Exception("Unknown signal"))

help = """
    this is simple signal sender\n
    
    show help: show help
    show signal: show signal
    show process: show process
    send signal: send signal
    q: quit
    """

signals = """
    SIGHUP: 1 - hangup
    SIGINT: 2 - interrupt
    SIGQUIT: 3 - quit
    SIGILL: 4 - illegal instruction
    SIGABRT: 6 - abort
    SIGFPE: 8 - floating point exception
    SIGKILL: 9 - kill
    SIGSEGV: 11 - segmentation fault
    SIGPIPE: 13 - broken pipe
    SIGALRM: 14 - alarm
    SIGTERM: 15 - termination
    SIGUSR1: 10,30,16 - user defined signal 1
    SIGUSR2: 12,17,31 - user defined signal 2
    SIGCHLD: 17,18,20 - child status has changed
    SIGCONT: 18,19,25 - continue
    SIGSTOP: 17,19,23 - stop
    SIGTTIN: 17,19,21 - background read from tty
    SIGTTOU: 17,19,22 - background write to tty
"""

print(help)
while True:
    
    
    cmd = input("> ")

    match cmd:
        case "show help":
            print(help)
        case "show process":
            print("process list:")
            for proc in psutil.process_iter():
                try:
                # Get process name & pid from process object.
                    processName = proc.name()
                    processID = proc.pid
                    print(processName , ' ::: ', processID)
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    pass
        case "show signal":
            print("signal list:")
            print(signals)
        case "send signal":
            pid = input("pid: ")
            sig = input("signal: ")
            s = Signal(pid, sig)
            s.send(pid, sig)
        case "q":
            break
        case default:
            print("unknown command")
    
    
    