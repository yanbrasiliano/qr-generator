""" 
File name: 						qr-generator.py             
Author:								Yan Brasiliano Silva Penalva                        
Email: 								yanpenabr@gmail.com
---------------------------------------------------------------------
Date created: 				20 MAR 2021                
Date last modified: 	20 MAR 2021
Python Version: 			Above 3.6
License: 							GNU License
Maintainer: 					Yan Brasiliano Silva Penalva  
Version: 							1.0
---------------------------------------------------------------------
Description
PT-BR: Este programa tem como função gerar -CODES das frases/links inseridos.
EN-US: This program has the function of generating QR CODES of the inserted phrases/links. 

"""


from pyqrcode import QRCode
import png
import pyqrcode

variable = input('Enter the phrase or link to generate the QR CODE:  ')

#convert QR CODE
qr_code = pyqrcode.create(variable)

#save the picture

qr_code.png(r'qr.png', scale = 10)