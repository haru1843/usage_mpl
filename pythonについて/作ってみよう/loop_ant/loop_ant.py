import numpy as np
import cv2


class Ant:

    def __init__(self, h, w):
        self.d_list = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        self.d_index = np.random.choice(range(0, len(self.d_list)))
        self.pos = {"h": h, "w": w}

    def move(self):
        self.pos["h"] += self.d_list[self.d_index][0]
        self.pos["w"] += self.d_list[self.d_index][1]

    def check_tile(self, color):
        if color == "black":
            self.d_index = (self.d_index-1) % len(self.d_list)

        if color == "white":
            self.d_index = (self.d_index+1) % len(self.d_list)


def main():
    height = 200
    width = 200
    white_val = 200
    black_val = 0
    thresh = (white_val + black_val) // 2
    imageArray = np.zeros((height, width, 3), np.uint8)

    ant1 = Ant(h=height//2 - 7, w=width//2 + 7)
    ant2 = Ant(h=height//2 - 7, w=width//2 - 7)
    ant3 = Ant(h=height//2 + 10, w=width//2)

    ant_list = [ant1, ant2, ant3]

    try_num = 0
    while try_num < 50000:
        try_num += 1

        for i, ant in enumerate(ant_list):
            # 足元の確認
            now_color = imageArray[ant.pos["h"], ant.pos["w"]]
            color = ""

            if now_color[i] > thresh:
                color = "white"
                imageArray[ant.pos["h"], ant.pos["w"]][i] = black_val
            else:
                color = "black"
                imageArray[ant.pos["h"], ant.pos["w"]][i] = white_val

            ant.check_tile(color)
            ant.move()

        cv2.putText(imageArray, str(try_num),
                    (int(0.95*height), int(0.95*width)),
                    cv2.FONT_HERSHEY_SIMPLEX, 10, (0, 255, 255))

        cv2.imshow("ant", cv2.resize(imageArray, (height*4, width*4)))
        if cv2.waitKey(1) != -1:
            break


if __name__ == '__main__':
    main()
