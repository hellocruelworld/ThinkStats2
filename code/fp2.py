import multiprocessing
import random
import io
import mercantile
import urllib.request
import PIL.Image
from collections import deque
from imutils.video import VideoStream
import numpy as np
import argparse
import cv2
import imutils
import time


def _download_tile(tile: mercantile.Tile):
    """
    Helper function for downloading associated image
    """
    server = random.choice(['a', 'b', 'c'])
    url = 'http://{server}.tile.openstreetmap.org/{zoom}/{x}/{y}.png'.format(
    server=server,
    zoom=tile.z,
    x=tile.x,
    y=tile.y
    )
    response = urllib.request.urlopen(url)
    img = PIL.Image.open(io.BytesIO(response.read()))

    return img, tile

def get_image(west, south, east, north, zoom):
    """
    return glued tiles as PIL image
    :param west: west longitude in degrees
    :param south: south latitude in degrees
    :param east: east longitude in degrees
    :param north: north latitude in degrees
    :param zoom: wanted size
    :return: Image
    """
    tiles = list(mercantile.tiles(west, south, east, north, zoom))

    tile_size = 256
    min_x = min_y = max_x = max_y = None

    for tile in tiles:
        min_x = min(min_x, tile.x) if min_x is not None else tile.x
        min_y = min(min_y, tile.y) if min_y is not None else tile.y
        max_x = max(max_x, tile.x) if max_x is not None else tile.x
        max_y = max(max_y, tile.y) if max_y is not None else tile.y

        out_img = PIL.Image.new(
        'RGB',
        ((max_x - min_x + 1) * tile_size, (max_y - min_y + 1) * tile_size)
        )

        pool = multiprocessing.Pool(8)
        results = pool.map(_download_tile, tiles)
        pool.close()
        pool.join()

        for img, tile in results:
            left = tile.x - min_x
            top = tile.y - min_y
            bounds = (left * tile_size, top * tile_size, (left + 1) * tile_size, (top + 1) * tile_size)
            out_img.paste(img, bounds)

            return out_img

def makebinary():
    #the below need more accuracy
    greenLower = (40, 20, 6)
    greenUpper = (120, 255, 255)
    #original colour scheme (too light for OSM)
    #greenLower = (29, 86, 6)
    #greenUpper = (64, 255, 255)

    #reads into image in BGR
    image = cv2.imread('/Users/nicolawong/desktop/Finalproject/binaryimage/osm_image.png')
    blurred = cv2.GaussianBlur(image, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    gray = cv2.inRange(hsv, greenLower, greenUpper)
    #increased iterations to the below
    gray = cv2.erode(gray, None, iterations=6)
    gray = cv2.dilate(gray, None, iterations=6)

    cv2.imshow('Original image',image)
    cv2.imshow('Gray image', gray)

    x = 127
    y = 147
    bgrvalue = int(gray[x, y])
    if bgrvalue==255:
        print ("User is in a green environment!")
    else:
        print ("User is not in a green environment!")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    #currently doesnt take into account blues
    return


if __name__ == '__main__':
    #Not green:
    lat = 51.45544
    long = -2.60074

    #green:
    #lat = 51.45269
    #long = -2.60700

    #result is still off because of the way tiles are glued together.

    bb = 0.00001

    north = lat - bb
    west = long - bb
    south = lat + bb
    east = long + bb

    get_image(west, south, east, north, zoom=19).save('osm_image.png')
    makebinary()
    #currently doesnt take into account blues
