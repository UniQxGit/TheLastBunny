# TheLastBunny

How to run

```
python3 last_bunny.py
```


Known Issues:
in pop_shapes: "RecursionError: maximum recursion depth exceeded while getting the str of an object"
	-rare case
	-possible solutions: -use 'sys.setrecursionlimit(value)'
						 -don't use recursion (use loops)
	-i think the grid is clickable during the dialogue part, i had an instance when i'd start with 1 gem