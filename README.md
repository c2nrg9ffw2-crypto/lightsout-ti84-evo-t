# Lights Out for the TI-84 Evo-T

The puzzle **Lights Out** for the **TI-84 Evo-T** graphing calculator, written in Python.

> **Made with AI:** this game and this README were created with the help of AI (Claude by Anthropic).
> Everything was tested on a real TI-84 Evo-T.

## What is Lights Out?

- The board has **5 × 5 lights**. Some are **on** (yellow), some are **off** (dark).
- Pressing a light **flips** it **and** the 4 lights next to it (up, down, left, right):
  on becomes off, off becomes on.
- **Goal:** turn **all** the lights off.

## Features

- 3 levels: **Easy**, **Medium** and **Hard**
- **Every puzzle can be solved**
- A new puzzle every game
- A move counter
- Solved puzzles per level stay saved after you quit

## What you need

- A **TI-84 Evo-T** calculator
- A USB cable to connect it to your computer
- **Google Chrome** or **Microsoft Edge** (Safari and Firefox do not work with the TI tool)
- The file [`lights.py`](lights.py) from this repo

## Setup

1. Download [`lights.py`](lights.py) to your computer.
2. Connect the calculator to your computer with the USB cable.
   Leave the calculator on the **home screen**.
3. Open **https://connectevo.ti.com** in **Chrome** or **Edge**.
4. Connect to your calculator in the page and allow access when the browser asks.
5. Drag `lights.py` onto the page to send it to the calculator.
6. **Choose RAM** to play right away.
   The Python app on the Evo-T only shows files that are in RAM.
   (Want to keep the game safe? See [Don't lose the game](#dont-lose-the-game).)

> **Already sent it to Archive?** On the **home screen** (not in the Python app) press **2nd → mem → Mem Management**,
> find **LIGHTS** and press **enter**. The `*` in front of the name disappears, which means
> it is now in RAM.

## Start the game

1. Open the **Python** app on the calculator.
2. Choose **LIGHTS** and run it.
3. Choose **Easy**, **Medium** or **Hard** with ▲ ▼ and press **enter**.

## Keys

| Key | What it does |
|---|---|
| ◀ ▶ ▲ ▼ | Move the blue frame |
| enter | Press that light |
| clear | Quit |

## Tip: "chasing the lights"

1. Look at the **top row**. For every light that is on, press the square **just below it**.
   That turns it off.
2. Do the same row by row, down to the bottom.
3. If some lights are left in the bottom row, try pressing one or two squares in the
   **top row** first, then chase the lights down again.

**The order of presses doesn't matter**, and pressing the same square twice does nothing.

## Levels

| Level | How the puzzle is made |
|---|---|
| Easy | 4 random presses from a dark board |
| Medium | 8 random presses |
| Hard | 14 random presses |

Because every puzzle is made by pressing squares on a dark board, it can always be solved.

## Don't lose the game

The Evo-T **deletes RAM** when it stays turned off for a while.
A normal turn-off is fine, but after some time the game is gone.

**Best way:**

1. Keep the game in **Archive**. Archive is never deleted.
2. Go to the **home screen**. If you are in the Python app, leave it with **2nd → quit**
   (quit is above the **mode** key). In the Python app, **2nd → mem** does nothing.
3. Press **2nd → mem** (mem is above the **+** key) and choose **2: Mem Management**.
4. Choose the list with Python programs (or **All**).
5. Find **LIGHTS** and press **enter**. The `*` disappears, which means the game is now in RAM.
6. Open the **Python** app and play.

Programs can't move files between Archive and RAM by themselves, so this step can't be automatic.
The solved list **LIGHT** is in RAM too, so it can be deleted the same way.

## Solved puzzles

The number of solved puzzles per level is saved in a calculator list called **LIGHT**
(Easy, Medium, Hard), so it stays after you quit. The start screen shows them.

- To reset them, delete the list **LIGHT** in **2nd → mem → Mem Management** (on the home screen).
- A calculator reset (RAM clear) also resets them.

## Good to know

- Keep `lights.py` on your computer too, so you can always send it again.
- Made for the TI-84 Evo-T. Other TI-84 models are not tested.
