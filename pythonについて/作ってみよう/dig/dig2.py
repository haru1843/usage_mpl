import random


def deg(maze_mat, now_w, now_h):
    if maze_mat[now_h][now_w] == "□":
        return

    maze_mat[now_h][now_w] = "□"

    direct_list = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    while len(direct_list) > 0:
        direct = random.choice(direct_list)
        direct_list.remove(direct)

        # 横幅の制限
        if now_w + 2*direct[0] < 0 or now_w + 2*direct[0] >= len(maze_mat[0]):
            continue

        # 縦幅の制限
        if now_h + 2*direct[1] < 0 or now_h + 2*direct[1] >= len(maze_mat):
            continue

        # 進行先2マスの制限
        if maze_mat[now_h + 2*direct[1]][now_w + 2*direct[0]] == "□":
            continue

        # 制限をクリアした時の処理
        maze_mat[now_h + direct[1]][now_w + direct[0]] = "□"
        deg(maze_mat, now_w + 2*direct[0], now_h + 2*direct[1])


def main():
    width = 53
    height = 29
    maze_mat = [["■" for i in range(0, width)] for j in range(0, height)]

    now_w = random.choice(list(range(1, width, 2)))
    now_h = random.choice(list(range(1, height, 2)))

    deg(maze_mat, now_w, now_h)

    for maze_line in maze_mat:
        print(*maze_line, sep="")


if __name__ == '__main__':
    main()
