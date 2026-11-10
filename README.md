# 🌍 Greeting Wall

A super simple Python app that shows a random welcome message in a different language each time you run it. Built as a small project for practicing Git.

## Languages

- Kinyarwanda: _Muraho!_
- English: _Hello!_
- Swahili: _Jambo!_

## Requirements

- Python 3 (no extra packages needed)

## How to run

```bash
python greeting.py
```

Example output:

```
✨ *** GREETING WALL *** ✨

Welcome Message: Muraho! (Kinyarwanda)

Total languages represented: 3
```

Run it a few times to see different greetings.

## Adding a new greeting

1. Open `greeting.py` in any text editor.
2. Find the `greetings` list near the top of the file.
3. Add a new line inside the square brackets, using the format `"Greeting! (Language)"`.
4. Make sure the line ends with a comma.
5. Save the file and run it to check that your greeting appears and the language count goes up by one.

Example, adding French:

```python
greetings = [
    "Muraho! (Kinyarwanda)",
    "Hello! (English)",
    "Jambo! (Swahili)",
    "Bonjour! (French)",   # new greeting
]
```

> ⚠️ **Don't forget the comma.** If you leave it out, Python silently joins two greetings into one string, and the language count will be wrong. No error is shown, so it's easy to miss.

### Contributing your greeting with Git

```bash
git checkout -b add-shona-greeting
# edit greeting.py
git add greeting.py
git commit -m "Add shona greeting"
git push origin add-shona-greeting
```

Then open a pull request so others can review and merge your greeting.

## Git demo ideas

1. Commit the starting version.
2. Add a new language on a separate branch.
3. Merge the branch and view the history with `git log --oneline`.
