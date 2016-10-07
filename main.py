# -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
import psycopg2, sys, os, csv, resources, qgis.utils 
from PyQt4.QtCore import QSettings
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
import qgis.utils
from interface import *

class CarregaEstilos:   
    def __init__(self, iface):
        self.iface = iface
    
    def initGui(self):
        self.action1 = QAction(QIcon(":/plugins/carregaEstilos/style.png"), u"carrega estilo", self.iface.mainWindow())
        self.iface.addToolBarIcon(self.action1)
        QObject.connect(self.action1, SIGNAL("triggered()"), self.conectar)        
    
    def unload(self):
        self.iface.removeToolBarIcon(self.action1)
        try:
            self.MainWindow.close()
        except:
            pass
    
    def conectar(self):
        if QgsMapLayerRegistry.instance().mapLayers() != {}:
            self.dialogo()
            self.s = QSettings()
            self.s.beginGroup("PostgreSQL/connections")
            self.addCon()
        else:
            QMessageBox.warning(self.iface.mainWindow(),u"ERRO", u"<font color=red>Não há camadas carregadas:</font><br><font color=blue>Tente carrega camadas antes de carregar os estilos!</font>")	
        
    def addCon(self):	
        connects=[]
        for x in self.s.allKeys():
            if  x[-9:] == "/username":
                connects.append(x[:-9])
        self.menu.comboBox_2.addItems(connects)	
        
    def dialogo(self):
        self.MainWindow = QtGui.QDialog(self.iface.mainWindow())
        self.menu = Ui_Dialog(self.MainWindow)
        self.menu.pushButton.clicked.connect(self.carregar)
        self.MainWindow.show()
    
    def carregar(self):	    
        if (self.menu.comboBox_2.currentIndex() != 0) and (self.menu.comboBox_3.currentIndex() != 0):
            self.teste=None
            self.styles={}
            try:
                db=self.menu.comboBox_2.currentText().replace(" ","")
                self.menu.comboBox_2.setCurrentIndex(0) 
                s = QSettings()
                s.beginGroup("PostgreSQL/connections")
                a=db+"/host"
                b=db+"/port"
                c=db+"/database"
                d=db+'/username'
                e=db+'/password' 
                conn_string = "host="+s.value(a)+" dbname="+s.value(c)+" user="+s.value(d)+" password="+s.value(e)+" port="+s.value(b)
                conn = psycopg2.connect(conn_string)
                cursor = conn.cursor()
                cursor.execute("select id, stylename from layer_styles;")
                for valores in cursor.fetchall():
                    self.styles[valores[1]] = valores[0]
            except:
                QMessageBox.warning(self.iface.mainWindow(),u"ERRO", u"Conecte-se a um 'BANCO DE DADOS' e salve seu 'USUÁRIO' e sua 'SENHA' e coloque a 'MÁQUINA' que está seu banco de dados")
                self.teste = "erro"
            if not self.teste == "erro":
                tipos = { 1: 'revisao_', 2:'aquisicao_',3: 'reambulacao_', 4: 'vetorizacao_'}
                tipo = tipos[self.menu.comboBox_3.currentIndex()]					
                self.carregarEstilos(tipo)
        else:
            self.menu.comboBox_3.setCurrentIndex(0)
            self.menu.comboBox_2.setCurrentIndex(0)					
            QMessageBox.warning(self.iface.mainWindow(),u"ERRO", u"<font color=red>Todos os campos precisão está definidos para efetuar a operação</font>")

    def carregarEstilos(self, tipo):
        self.menu.comboBox_3.setCurrentIndex(0)
        layers = QgsMapLayerRegistry.instance().mapLayers()
        grupo={}
        for x in range(len(layers)):
            grupo[layers.keys()[x][:-17]]=layers.get(layers.keys()[x])
        for camada in grupo.keys():
            self.iface.setActiveLayer(grupo.get(camada))
            estilo_camada = tipo+self.iface.activeLayer().name()
            if estilo_camada in self.styles.keys():
                x= self.iface.activeLayer().getStyleFromDatabase(str(self.styles.get(estilo_camada)), "Estilo não encontrado")
        self.iface.mapCanvas().refreshAllLayers()
        self.MainWindow.close()
    




























