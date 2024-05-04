import tty, sys, termios, time

tty_attr = termios.tcgetattr(sys.stdin)
tty.setcbreak(sys.stdin)
times = sys.stdin.read(1)
try:
    int_times = int(times)
    print( "{0}".format(int_times))
    for x in range(int_times):
        sys.stdout.write("\7")
        time.sleep(1)
except ValueError:
    print("You did not input a number")
finally:
    termios.tcsetattr(sys.stdin, termios.TCSAFLUSH, tty_attr)
    sys.stdout.flush()