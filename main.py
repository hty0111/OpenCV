#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: HTY
# @Date: 2/8/22
# @Brief: OpenCV note

import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def show(src, name="window", time=0):
    cv2.imshow(name, src)
    cv2.waitKey(time)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    img = cv2.imread("img.png")  # read an image in BGR format
    # cv2.imshow("window name", img)  # show an image
    # cv2.waitKey(0)  # wait time (mm), 0 means any key
    # cv2.imwrite("file path", img)   # save picture
    b, g, r = cv2.split(img)
    img = cv2.merge((b, g, r))
    img = cv2.resize(img, (100, 100))
    ret, dst = cv2.threshold(src=r, thresh=127, maxval=255, type=cv2.THRESH_TOZERO)
    show(r, "r")
    show(dst, "r threshold")
