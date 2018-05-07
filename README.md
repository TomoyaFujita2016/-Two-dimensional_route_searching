# Two-dimensional_route_searching
<img src="https://github.com/TomoyaFujita2016/2D_Route_searching/blob/master/model.JPG?raw=true" width=500px>
## Requirement
- python3
## Usage
1. Create a map file like following.
```
1,2,2,2,1,3
1,3,1,3,2,2
3,2,2,1,3,2
1,1,3,1,2,0
2,3,1,1,2,2
```

2. Execute script!
```
$ python3 explore.py [map file path]
```

3. The example of execution
```
$ python explore.py map_multi.csv 
==========Analyzing this map===========
  1   2   2   2   1   3 
  1   3   1   3   2   2 
  3   2   2   1   3   2 
  1   1   3   1   2   0 
  2   3   1   1   2   2 
=======================================
Minimum value: 12
  #   #   2   2   1   3 
  1   3   #   3   2   2 
  3   2   2   #   #   2 
  1   1   3   1   2   # 
  2   3   1   1   2   # 
or
  #   #   2   2   1   3 
  1   3   #   3   2   2 
  3   2   2   #   3   2 
  1   1   3   #   #   # 
  2   3   1   1   2   # 
```

4. Appendices & Attention
- You can use "map_multi.csv" and "map_single.csv" as a test.
- The all row & column of size in a file should be same.
- Creating map file is a piece of cake.
```
python3 mapGenerator.py [save path] [row] [col] [minValue] [maxValue]
```
