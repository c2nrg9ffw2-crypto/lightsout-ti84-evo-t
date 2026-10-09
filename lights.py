# Lights Out for the TI-84 Evo
# Turn all the lights off. Pressing a light flips it and the 4 lights
# next to it (up, down, left, right).
# Keys: arrows = move, enter = press, clear = quit
import random
from ti_draw import clear, set_color, draw_text
from ti_draw import fill_rect as ti_fill_rect
try:
    from ti_draw import get_screen_dim
    SW, SH = get_screen_dim()
except:
    SW, SH = 319, 209

# Keep every box inside the screen and never stop the game over one box.
# The Evo draws boxes 1 pixel too small, so we ask for 1 pixel more.
def fill_rect(x, y, w, h):
    if x < 0:
        w, x = w + x, 0
    if y < 0:
        h, y = h + y, 0
    w, h = min(w, SW - x), min(h, SH - y)
    if w > 0 and h > 0:
        try:
            ti_fill_rect(x, y, w + 1, h + 1)
        except:
            pass
# Draw in a hidden buffer and show the finished picture at once: no flicker
try:
    from ti_draw import use_buffer, paint_buffer
    use_buffer()
except:
    paint_buffer = None
try:
    from ti_system import get_key as read_key
except:
    from ti_system import getKey as read_key
# On the Evo get_key wants one number. Find out once at the start.
try:
    read_key()
    key = read_key
except TypeError:
    def key():
        return read_key(0)
try:
    from ti_system import store_list, recall_list
except:
    store_list = recall_list = None
try:
    from time import sleep
except:
    from ti_system import sleep
try:
    import gc
except:
    gc = None

LEFT = (2, 24)
RIGHT = (1, 26)
UP = (3, 25)
DOWN = (4, 34)
OK = (5, 105)                 # enter
SECOND = (21, 22)             # 2nd, mode
QUIT = (9, 45)                # clear
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (150, 150, 150)
YELLOW = (255, 220, 0)

def paint():
    if paint_buffer:
        paint_buffer()

def write(x, y, s):                    # text that can never stop the game
    try:
        draw_text(x, y, s)
    except:
        pass

def wait_for(keys):
    paint()
    while True:
        k = key()
        if k in keys:
            return k
        sleep(0.05)

# Numbers saved in a calculator list, so they stay after quitting
def load(name, n):
    try:
        l = [int(v) for v in recall_list(name)]
    except:
        l = []
    return (l + [0] * n)[:n]

def save(name, l):
    try:
        store_list(name, l)
    except:
        pass

# Text panel on the right side: rows 30 px high, the whole row is wiped first
def text(row, s, col=WHITE):
    set_color(*BLACK)
    fill_rect(TX, row * 30, SW - TX, 29)
    set_color(*col)
    write(TX, row * 30 + 22, s)

def box_frame(x, y, w, h, t, col):     # a frame t pixels thick
    set_color(*col)
    fill_rect(x, y, w, t)
    fill_rect(x, y + h - t, w, t)
    fill_rect(x, y, t, h)
    fill_rect(x + w - t, y, t, h)

def title_screen(name, col, line):
    clear()
    set_color(*BLACK)
    fill_rect(0, 0, SW, SH)
    set_color(*col)
    write(SW // 2 - 80, 25, name)
    set_color(*WHITE)
    write(SW // 2 - 80, 55, line)

# A menu on the start screen. Returns the chosen number, or -1 for clear.
def menu(options, choice, hint):
    x = SW // 2 - 80
    set_color(*BLACK)
    fill_rect(0, 64, SW, SH - 64)
    set_color(*WHITE)
    write(x, 202, hint)
    while True:
        for i in range(len(options)):
            set_color(*BLACK)
            fill_rect(x - 20, 64 + i * 28, 230, 27)
            set_color(*(YELLOW if i == choice else GREY))
            write(x, 90 + i * 28, ("> " if i == choice else "  ") + options[i])
        k = wait_for(UP + DOWN + OK + QUIT)
        if k in QUIT:
            return -1
        if k in OK:
            return choice
        if k in UP:
            choice = (choice - 1) % len(options)
        if k in DOWN:
            choice = (choice + 1) % len(options)

N = 5
C = 38                        # square size
X0 = 6
Y0 = (SH - N * C) // 2
TX = X0 + N * C + 10          # text panel (black, so text is fine)
ON = YELLOW
OFF = (50, 50, 50)
CURSOR = (0, 200, 255)
LEVELS = [("Easy", 4), ("Medium", 8), ("Hard", 14)]   # random presses

lights = [0] * (N * N)

def cell(i, cursor=False):
    r, c = divmod(i, N)
    x, y = X0 + c * C, Y0 + r * C
    set_color(*(ON if lights[i] else OFF))
    fill_rect(x, y, C - 2, C - 2)
    if cursor:
        box_frame(x, y, C - 2, C - 2, 4, CURSOR)

def press(i):                  # flip this light and its neighbours
    r, c = divmod(i, N)
    out = [i]
    if r > 0:
        out.append(i - N)
    if r < N - 1:
        out.append(i + N)
    if c > 0:
        out.append(i - 1)
    if c < N - 1:
        out.append(i + 1)
    for j in out:
        lights[j] = 1 - lights[j]
    return out

def start_screen(stats):
    title_screen("LIGHTS OUT", ON,
                 "Solved " + str(stats[0]) + " / " + str(stats[1]) + " / " + str(stats[2]))
    return menu([n for n, k in LEVELS], 0, "UP/DOWN + ENTER")

def game(level):               # returns True when solved, False for quit
    for i in range(N * N):
        lights[i] = 0
    # start from all off and press random squares: then it can always be solved
    while sum(lights) == 0:
        for k in range(LEVELS[level][1]):
            press(random.randrange(N * N))
    clear()
    set_color(*BLACK)
    fill_rect(0, 0, SW, SH)
    cur = 12
    for i in range(N * N):
        cell(i, i == cur)
    text(0, "LIGHTS OUT")
    text(1, LEVELS[level][0])
    text(3, "Moves 0")
    text(5, "ENTER:press")
    text(6, "CLEAR:quit")
    moves = 0
    while True:
        paint()
        k = key()
        if not k:
            sleep(0.03)
            continue
        if k in QUIT:
            return False
        old = cur
        r, c = divmod(cur, N)
        if k in LEFT:
            c = (c - 1) % N
        elif k in RIGHT:
            c = (c + 1) % N
        elif k in UP:
            r = (r - 1) % N
        elif k in DOWN:
            r = (r + 1) % N
        elif k in OK:
            for j in press(cur):
                cell(j, j == cur)
            moves += 1
            text(3, "Moves " + str(moves))
            if sum(lights) == 0:
                return True
        cur = r * N + c
        if cur != old:
            cell(old)
            cell(cur, True)

# --- start ---
stats = load("LIGHT", 3)       # solved puzzles per level
level = start_screen(stats)
while level >= 0:
    if not game(level):
        break
    stats[level] += 1
    save("LIGHT", stats)
    text(2, "SOLVED!", ON)
    text(5, "ENTER:again")
    if wait_for(OK + QUIT) in QUIT:
        break
paint()
