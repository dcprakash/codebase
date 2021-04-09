# isolated pixel means no same pixel in entire row or column

from __future__ import print_function


def Check_Isolated_Pixel():
    def get_row_count(grid, rows):
        rc = []
        for i in range(rows):
            # print (sum(grid[i]))
            rc.append(sum(grid[i]))
        return rc

    def get_col_count(grid, rows, cols):
        cc = []
        for j in range(cols):
            sum = 0
            for i in range(rows):
                sum += grid[i][j]
            cc.append(sum)
                # print ((grid[i][j]))
        return cc

    def check_pixels(grid, rc, cc):
        i_pixels = []
        for i in range(len(grid)):
            # if not 1, then either there is no 1 or 
            # more than 1 ones and it cannot be an isolated 1 in that row
            if rc[i] != 1:
                continue
            for j in range(len(grid[0])):
                if cc[j] != 1:
                    continue
                if grid[i][j] != 1:
                    continue
                i_pixels.append([i,j])
        # for i, iv in enumerate(rc):
        #     if iv != 1:
        #         continue
        #     for j, jv in enumerate(cc):
        #         if jv != 1:
        #             continue
        #         i_pixels.append(grid[i][j])
        return i_pixels


    # grid = [[1, 0, 0, 0],
    #         [0, 1, 0, ],
    #         [0, 0, 1, 1]]

    # grid = [[1, 0, 0, 0],
    #         [0, 1, 0, 0],
    #         [0, 0, 1, 1]]

    # grid = [[1, 0, 0, 0],
    #         [0, 0, 0, 1],
    #         [0, 1, 1, 0]]
    # grid = [[1, 0, 0, 0],
    #         [0, 1, 0, 0],
    #         [0, 0, 1, 1]]
    
    grid = [[1, 0, 0, 1],
            [0, 1, 0, 0],
            [0, 0, 1, 1]]

    rows = len(grid)
    cols = len(grid[0])
    row_count = get_row_count(grid, rows)
    print ("Row count {}".format(row_count))
    col_count = get_col_count(grid, rows, cols)
    print("Col count {}".format(col_count))
    isolated_pixels = check_pixels(grid, row_count, col_count)
    print ("Isolated Pixels {}" .format(isolated_pixels))


if __name__ == "__main__":
    Check_Isolated_Pixel()

