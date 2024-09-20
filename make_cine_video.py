import numpy as np
from basicfunctions import cine2nparrall, cine2nparr, avg_cine, save_movie_nparr
from pyphantom import Phantom, utils, cine
import matplotlib.pyplot as plt
import cv2 as cv
# basicfunctions import 에 save_movie_nparr 추가해주기


ph = Phantom() # cine 파일을 불러올 때 항상해줘야됨

fname = '//203.253.185.128/kk/03 exp/240905/case5.cine'
raw = cine2nparrall(fname)

save_movie_nparr(raw, 'case5.avi', 10) # 원본 cine파일 넣어준 뒤 -> 파일 이름 정해주고 -> 프레임 속도 지정