# -*- coding: latin1 -*-

from main import CarregaEstilos 


def name():
  return "Carrega estilos"
def description():
  return "Carrega camadas personalizadas para feições"
def version():
  return "Version 0.1"

def classFactory(iface):
  from main import CarregaEstilos
  return CarregaEstilos(iface)

def qgisMinimumVersion():
  return "2.0"
def author():
  return "Jossan"
def email():
  return "me@hotmail.com"
def icon():
  return "style.png"

## any other initialisation needed
