def num_islands(grid):
    if not grid:
        return 0

   
    rows, cols = len(grid), len(grid[0])
    
    
    def dfs(r, c):
       
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 'W':
            return
        
        grid[r][c] = 'W'
       
        dfs(r - 1, c)  
        dfs(r + 1, c)  
        dfs(r, c - 1)  
        dfs(r, c + 1)  

   
    island_count = 0
    
  
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'L':
               
                dfs(r, c)
               
                island_count += 1

    return island_count


def get_grid_input():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    grid = []
    print(f"Enter the grid ({rows} rows, {cols} columns) using 'L' for land and 'W' for water:")
    for i in range(rows):
        row = input(f"Row {i + 1}: ")
        grid.append(list(row.strip())) 

    return grid


archipelago_map = get_grid_input()


print("Number of islands:", num_islands(archipelago_map))
