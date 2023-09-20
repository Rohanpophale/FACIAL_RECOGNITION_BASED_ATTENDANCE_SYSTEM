import py2exe
from distutils.core import setup
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot, QTimer, QDate, Qt
from PyQt5.QtWidgets import QDialog,QMessageBox
import cv2
import face_recognition
import numpy as np
import datetime
import os
import csv

setup(
    option={'py2exe':{'bundle_files':1,'compressed': True}},
    windows=[{'script': "mainwindow.py"}],
    zipfile=None,
)