# TheLastBunny

Puzzle matching RPG turn based fantasy game!

The underworld has taken over all bunny kind, avenge your bunny brothers and sisters!

Style: 2D Turn-Based RPG Puzzle
Mechanic: During a battle, click on a shape with consecutive matching shapes in any direction (except diagonal) to collect all of that type. Collect various shapes to perform actions!
Aesthetics: Cute, bouncy aesthetics with dark storytelling


How to run
Please make sure that pygame and all its dependencies are installed before running. 
```
python3 last_bunny.py
```


Known Issues:
in pop_shapes: "RecursionError: maximum recursion depth exceeded while getting the str of an object"
	-rare case
	-possible solutions: -use 'sys.setrecursionlimit(value)'
						 -don't use recursion (use loops)
	-i think the grid is clickable during the dialogue part, i had an instance when i'd start with 1 gem
