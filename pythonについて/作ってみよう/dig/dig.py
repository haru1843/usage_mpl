# 深さ優先で計算していった方がいい感じのできそう
# 深さ優先 -> 再帰関数
import random


def main():
    width = 15
    height = 15
    maze_mat = [["■" for i in range(0, width)] for j in range(0, height)]

    next_w_list = [random.choice(list(range(1, width, 2)))]
    next_h_list = [random.choice(list(range(1, height, 2)))]
    while len(next_w_list) > 0:
        now_w = next_w_list.pop()
        now_h = next_h_list.pop()

        direct_list = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        while len(direct_list) > 0:
            direct = random.choice(direct_list)
            direct_list.remove(direct)

            # 横幅の制限
            if now_w + 2*direct[0] < 0 or now_w + 2*direct[0] >= width:
                continue

            # 縦幅の制限
            if now_h + 2*direct[1] < 0 or now_h + 2*direct[1] >= height:
                continue

            # 進行先2マスの制限
            if maze_mat[now_w + 2*direct[0]][now_h + 2*direct[1]] == "□":
                continue

            # 制限をクリアした時の処理
            maze_mat[now_w + direct[0]][now_h + direct[1]] = "□"
            maze_mat[now_w + 2 * direct[0]][now_h + 2*direct[1]] = "□"

            next_w_list.append(now_w + 2 * direct[0])
            next_h_list.append(now_h + 2 * direct[1])

    for maze_line in maze_mat:
        print(*maze_line, sep="")


if __name__ == '__main__':
    main()
