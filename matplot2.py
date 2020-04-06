#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import sys
from PyQt5.QtWidgets import (QWidget,QComboBox,QLineEdit,QLabel,QGroupBox\
        ,QPushButton,QHBoxLayout,QVBoxLayout,QApplication,QCheckBox\
        ,QFileDialog)
import os 
import os.path 
import math 
import matplotlib
matplotlib.rcParams['ps.useafm'] = True
matplotlib.rcParams['pdf.use14corefonts'] = True
matplotlib.rcParams['text.usetex'] = True
from matplotlib.backends.backend_qt5agg \
        import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt 

cd =  os.path.abspath(os.path.dirname(__file__))
currentdir = cd 
#cd = "/home/hajime/graph_plot/"

os.chdir(cd)
os.getcwd()
colors = ['#1f77b4','#ff7f0e','#2ca02c','#d62728','#9467bd' ,'#8c564b','#e377c2','#7f7f7f','#bcbd22','#17becf']

class MyWidget(QWidget):




    def __init__(self):
        super(MyWidget,self).__init__()
        grid = QHBoxLayout()
        self.groupBox = QGroupBox('matplot ver.2.1.2')

        #for log ----------------------------------------------------------
        self.log =  ['import matplotlib']
        self.log += ['matplotlib.rcParams[\'ps.useafm\'] = True']
        self.log += ['matplotlib.rcParams[\'pdf.use14corefonts\'] = True']
        self.log += ['matplotlib.rcParams[\'text.usetex\'] = True']
        self.log += ['import matplotlib.pyplot as plt']
        self.log += ['plt.rcParams[\"font.size\"] = 20']
        self.log += ['color = [\'#1f77b4\',\'#ff7f0e\',\'#2ca02c\',\'#d62728\',\'#9467bd\' ,\'#8c564b\',\'#e377c2\',\'#7f7f7f\',\'#bcbd22\',\'#17becf\']']
        self.log += ['plt.figure(figsize=(8,6))']
        self.log += ['############### end setting ####################']
        # -----------------------------------------------------------------
        

        #-------------------------------------------------
        inputdata = QLabel('Input Data')
        self.openbutton = QPushButton("file")
        self.openbutton.clicked.connect(self.open_FileDialog)
        self.ledit = QLineEdit("")
        self.logbutton = QPushButton("log")
        self.logbutton.clicked.connect(self.log_FileDialog)

        layout1 = QHBoxLayout()
        layout1.addWidget(inputdata)

        self.layout2 = QHBoxLayout()
        self.layout2.addWidget(self.openbutton)
        self.layout2.addWidget(self.logbutton)
        self.layout2.addWidget(self.ledit)

        layout3 = QHBoxLayout()
        x1 = QLabel('x')
        y1 = QLabel('y')
        lw = QLabel('lw')
        self.xEdit = QLineEdit("0")
        self.yEdit = QLineEdit("1")
        self.lwEdit = QLineEdit("2")

        layout3.addWidget(x1)
        layout3.addWidget(self.xEdit)
        layout3.addWidget(y1)
        layout3.addWidget(self.yEdit)
        layout3.addWidget(lw)
        layout3.addWidget(self.lwEdit)
        
        layout4 = QHBoxLayout()
        label = QLabel('label')
        lc = QLabel('lc')
        lt = QLabel('lt')
        self.labelEdit = QLineEdit("")
        self.lccombo = QComboBox()
        self.lccombo.addItems(['defalt','Blue','Orange','Green','Red', 'Purple', 'Brown', 'Pink', 'Grey', 'Yellow', 'Cyan'])
        self.ltcombo = QComboBox()
        self.ltcombo.addItems(['-','--','-.',':'])
        layout4.addWidget(label)
        layout4.addWidget(self.labelEdit)
        layout4.addWidget(lc)
        layout4.addWidget(self.lccombo)
        layout4.addWidget(lt)
        layout4.addWidget(self.ltcombo)

        layout5 = QHBoxLayout()
        scale = QLabel('Scale')
        layout5.addWidget(scale)

        layout6 = QHBoxLayout()
        self.xradio = QCheckBox('xlog')
        self.yradio = QCheckBox('ylog')
        layout6.addWidget(self.xradio)
        layout6.addWidget(self.yradio)

        layout7 = QHBoxLayout()
        self.liradio = QCheckBox('Limit Scale on')
        layout7.addWidget(self.liradio)

        layout8 = QHBoxLayout()
        xmax = QLabel('xmax')
        xmin = QLabel('xmin')
        self.xmaxEdit = QLineEdit()
        self.xminEdit = QLineEdit()
        layout8.addWidget(xmin)
        layout8.addWidget(self.xminEdit)
        layout8.addWidget(xmax)
        layout8.addWidget(self.xmaxEdit)


        layout82 = QHBoxLayout()
        ymax = QLabel('ymax')
        ymin = QLabel('ymin')
        self.ymaxEdit = QLineEdit()
        self.yminEdit = QLineEdit()
        layout82.addWidget(ymin)
        layout82.addWidget(self.yminEdit)
        layout82.addWidget(ymax)
        layout82.addWidget(self.ymaxEdit)



        layout9 = QHBoxLayout()
        self.labelradio = QCheckBox('Label on')
        layout9.addWidget(self.labelradio)

        layout10 = QHBoxLayout()
        xlabel = QLabel('x')
        ylabel = QLabel('y')
        size_label = QLabel('size')
        self.xlabelEdit = QLineEdit()
        self.ylabelEdit = QLineEdit()
        self.size_labelEdit = QLineEdit("18")
        layout10.addWidget(xlabel)
        layout10.addWidget(self.xlabelEdit)
        layout10.addWidget(ylabel)
        layout10.addWidget(self.ylabelEdit)
        layout10.addWidget(size_label)
        layout10.addWidget(self.size_labelEdit)

        layout11 = QHBoxLayout()
        self.legendradio = QCheckBox('Legend on')
        layout11.addWidget(self.legendradio)

        layout12 = QHBoxLayout()
        loc = QLabel('loc')
        size = QLabel('size')
        self.loclegend = QComboBox()
        self.loclegend.addItems(['upper right','upper left','lower right','lower left'])
        self.size_legend = QLineEdit('18')
        layout12.addWidget(loc)
        layout12.addWidget(self.loclegend)
        layout12.addWidget(size)
        layout12.addWidget(self.size_legend)

        layout13 = QHBoxLayout()
        save_f = QLabel('save filename')
        self.saveEdit = QLineEdit("plot.pdf")
        layout13.addWidget(save_f)
        layout13.addWidget(self.saveEdit)

        plot = QLabel('Plot')
        layout333 = QHBoxLayout()
        layout333.addWidget(plot)
        layout34 = QHBoxLayout()
        self.okButton = QPushButton('Plot!')
        self.okButton3 = QPushButton('Save')
        self.okButton2 = QPushButton('Clear')
        layout34.addWidget(self.okButton)
        layout34.addWidget(self.okButton3)
        layout34.addWidget(self.okButton2)
        

        self.okButton3.clicked.connect(self.Save_files)



        #set orivbox
        self.orivbox = QVBoxLayout()
        self.orivbox.addLayout(layout1)
        self.orivbox.addLayout(self.layout2)
        self.orivbox.addLayout(layout3)
        self.orivbox.addLayout(layout4)
        self.orivbox.addLayout(layout5)
        self.orivbox.addLayout(layout6)
        self.orivbox.addLayout(layout7)
        self.orivbox.addLayout(layout8)
        self.orivbox.addLayout(layout82)
        self.orivbox.addLayout(layout9)
        self.orivbox.addLayout(layout10)
        self.orivbox.addLayout(layout11)
        self.orivbox.addLayout(layout12)
        self.orivbox.addLayout(layout13)
        self.orivbox.addLayout(layout333)
        self.orivbox.addLayout(layout34)


        #set Layout
        self.groupBox.setLayout(self.orivbox)
        grid.addWidget(self.groupBox)


        #figure
        self.figure = plt.figure(figsize=(8,6))
        plt.rcParams["font.size"] = 20
        self.canvas = FigureCanvas(self.figure)
        grid.addWidget(self.canvas)
        
        #log 

        self.setLayout(grid)


        self.setSignals()
        self.setSignals2()

    def setSignals(self):
        self.okButton.clicked.connect(self.plotValue)

    def setSignals2(self):
        self.okButton2.clicked.connect(self.clear)

    def clear(self):
        #for log 
        plt.clf()
        self.canvas.draw()
        #for log ----------------------------------------------------------
        self.log =  ['import matplotlib']
        self.log += ['matplotlib.rcParams[\'ps.useafm\'] = True']
        self.log += ['matplotlib.rcParams[\'pdf.use14corefonts\'] = True']
        self.log += ['matplotlib.rcParams[\'text.usetex\'] = True']
        self.log += ['import matplotlib.pyplot as plt']
        self.log += ['plt.rcParams[\"font.size\"] = 20']
        self.log += ['color = [\'#1f77b4\',\'#ff7f0e\',\'#2ca02c\',\'#d62728\',\'#9467bd\' ,\'#8c564b\',\'#e377c2\',\'#7f7f7f\',\'#bcbd22\',\'#17becf\']']
        self.log += ['plt.figure(figsize=(8,6))']
        self.log += ['############### end setting ####################']
        # -----------------------------------------------------------------


    def open_FileDialog(self):
        filerecord = currentdir + '/open_file.txt'
        for l in open(filerecord).readlines():
            data = l[:-1].split()
            filename1 = str(data[0])
            
        filename = QFileDialog.getOpenFileName(self, 'Open file', filename1)
        filename = str(filename[0])
        self.ledit.setText(filename)

        split_file = filename.split('/')
        if len(split_file) > 1:
            f = open(filerecord,"w")
            for n in range(len(split_file)-1):
                f.write(str(split_file[n]))
                f.write("/")
            f.close()

    def log_FileDialog(self):
        filename = QFileDialog.getOpenFileName(self, 'log file', currentdir + '/Log')
        filename = str(filename[0])
        self.ledit.setText(filename)


    def Save_files(self):
        foldername = QFileDialog.getExistingDirectory(self, 'Open Directory', os.path.expanduser('~'))
        #print foldername
        filename = self.saveEdit.text()
        #print filename
        save = str(foldername) + "/" + str(filename)
        plt.savefig(save)

        #-------------------------------------------------------
        self.log += ['plt.savefig(\''+str(save)+'\')']
        self.log += ['plt.close()']
        log = self.log
        dir_name = currentdir + '/Log/'
        split_file = filename.split('.')
        save_name = dir_name
        for n in range(len(split_file)-1):
            save_name += split_file[n]
       
        save_name += '_' + str(datetime.date.today())
        save_name += '.py'
        f = open(save_name,"w")
        for n in range(len(log)):
            f.write(str(log[n]))
            f.write('\n')
        f.close()

        #for log ----------------------------------------------------------
        self.log =  ['import matplotlib']
        self.log += ['matplotlib.rcParams[\'ps.useafm\'] = True']
        self.log += ['matplotlib.rcParams[\'pdf.use14corefonts\'] = True']
        self.log += ['matplotlib.rcParams[\'text.usetex\'] = True']
        self.log += ['import matplotlib.pyplot as plt']
        self.log += ['plt.rcParams[\"font.size\"] = 20']
        self.log += ['color = [\'#1f77b4\',\'#ff7f0e\',\'#2ca02c\',\'#d62728\',\'#9467bd\' ,\'#8c564b\',\'#e377c2\',\'#7f7f7f\',\'#bcbd22\',\'#17becf\']']
        self.log += ['plt.figure(figsize=(8,6))']
        self.log += ['############### end setting ####################']
        # -----------------------------------------------------------------

    def jiko_exec(self):
        exec(self.jiko)



    def plotValue(self):
        

        #find color-------------------
        def find_lc(moji):
            if moji == 0:
                moji2 = "no"
            elif moji == 1:
                moji2 = colors[0]
            elif moji == 2:
                moji2 = colors[1]
            elif moji == 3:
                moji2 = colors[2]
            elif moji == 4:
                moji2 = colors[3]
            elif moji == 5:
                moji2 = colors[4]
            elif moji == 6:
                moji2 = colors[5]
            elif moji == 7:
                moji2 = colors[6]
            elif moji == 8:
                moji2 = colors[7]
            elif moji == 9:
                moji2 = colors[8]
            elif moji == 10:
                moji2 = colors[9]
            else: 
                moji2 = "w"

            return moji2
        #-----------------------------

        def find_lt(moji):
            if moji == 0:
                moji2 = '-'
            elif moji ==1:
                moji2 = "--"
            elif moji == 2:
                moji2 = '-.'
            else:
                moji2 = ':'
            return moji2

        #-----------------------------

        def find_legend(moji):
            if moji == 0:
                moji2 = 'upper right'
            elif moji == 1:
                moji2 = 'upper left'
            elif moji == 2:
                moji2 = 'lower right'
            elif moji == 3:
                moji2 = 'lower left'
            
            return moji2

        def back_slash(moji):

            if moji.find('..') > -1:
                moji2 = moji.split('..')

                moji3 = moji2[0]
                for n in range(1,len(moji2)):
                    moji3 = moji3 + '\\' + moji2[n] 


            else:
                moji3 = moji
            return moji3


        #plot!i-------------------------------------------------
        fontsize = self.size_labelEdit.text()
        xmin     = self.xminEdit.text()
        xmax     = self.xmaxEdit.text()
        ymin     = self.yminEdit.text()
        ymax     = self.ymaxEdit.text()
        label_size= self.size_labelEdit.text()
        xlabel = str(self.xlabelEdit.text())
        ylabel = str(self.ylabelEdit.text())

        # back_slash ---------------
        xlabel = back_slash(xlabel)
        ylabel = back_slash(ylabel)
        # --------------------------


        filename = self.ledit.text()
        xnum = int(self.xEdit.text())
        ynum = int(self.yEdit.text())
        labell = str(self.labelEdit.text())
        lw = int(self.lwEdit.text())
        lc1 = self.lccombo.currentIndex()
        lt1 = self.ltcombo.currentIndex()
        
        lc = find_lc(lc1)
        lt = find_lt(lt1)

        if os.path.isfile(filename):
               
            
            # back_slash
            labell = back_slash(labell)

            # py or dat?
            splitfile = filename.split(".")

            # ------------------------------------------------------
            if splitfile[len(splitfile)-1] == "py":
                read_py = []
                for l in open(filename).readlines():
                    read_py += [str(l)]

                for n in range(len(read_py)):
                    if read_py[n].find('#') > -1:
                        n_start = n 
                        break
                jiko = ""
                for n in range(len(read_py)):
                    if n > n_start:
                        if read_py[n].find('savefig') > -1:
                            break
                        jiko1 = read_py[n]
                        jiko2 = jiko1.rstrip('\\n')
                        jiko += jiko2
                        self.log += [jiko2]
                        self.jiko = jiko

                self.jiko_exec()

                #xlim ---------------------------------------
                len_read = len(read_py)
                for n in range(len(read_py)):
                    num = len_read-1-n
                    #-----------------
                    moji1 = 'plt.xlim('
                    moji2= ')\n'
                    #-----------------
                    if read_py[num].find(moji1) > -1:
                        moji   = read_py[num].lstrip(moji1)
                        mojiji = moji.rstrip(moji2)
                        moji3  = mojiji.split(',')
                        xmin = str(moji3[0])
                        xmax = str(moji3[1])
                        self.xminEdit.setText(xmin)
                        self.xmaxEdit.setText(xmax)
                        self.liradio.setChecked(True)
                        break
            # ------------------------------------------------------

                #ylim ---------------------------------------
                len_read = len(read_py)
                for n in range(len(read_py)):
                    num = len_read-1-n
                    #-----------------
                    moji1 = 'plt.ylim('
                    moji2= ')\n'
                    #-----------------
                    if read_py[num].find(moji1) > -1:
                        moji   = read_py[num].lstrip(moji1)
                        mojiji = moji.rstrip(moji2)
                        moji3  = mojiji.split(',')
                        ymin = str(moji3[0])
                        ymax = str(moji3[1])
                        self.yminEdit.setText(ymin)
                        self.ymaxEdit.setText(ymax)
                        self.liradio.setChecked(True)
                        break
            # ------------------------------------------------------

                #xlabel ---------------------------------------
                len_read = len(read_py)
                for n in range(len(read_py)):
                    num = len_read-1-n
                    #-----------------
                    moji1 = 'plt.xlabel(\''
                    moji2= '\')\n'
                    #-----------------
                    if read_py[num].find(moji1) > -1:
                        moji   = read_py[num].lstrip(moji1)
                        mojiji = moji.rstrip(moji2)
                        moji3  = mojiji.split(',')
                        xlabel   = str(moji3[0])

                        #---------------------------------------
                        if xlabel.find('\\\\') > -1:
                            xlabel_d = xlabel.split('\\\\')
                            xlabel = ''
                            for n in range(len(xlabel_d)):
                                xlabel += xlabel_d[n]
                                if n < len(xlabel_d)-1:
                                    xlabel += '\\'
                        #---------------------------------------



                        xlabel = xlabel.rstrip('\'')
                        fontsize = moji3[1].lstrip('fontsize=')
                        self.xlabelEdit.setText(xlabel)
                        self.size_labelEdit.setText(fontsize)
                        self.labelradio.setChecked(True)
                        break
            # ------------------------------------------------------
                #ylabel ---------------------------------------
                len_read = len(read_py)
                for n in range(len(read_py)):
                    num = len_read-1-n
                    #-----------------
                    moji1 = 'plt.ylabel(\''
                    moji2= '\')\n'
                    #-----------------
                    if read_py[num].find(moji1) > -1:
                        moji   = read_py[num].lstrip(moji1)
                        mojiji = moji.rstrip(moji2)
                        moji3  = mojiji.split(',')
                        ylabel   = str(moji3[0])


                        #---------------------------------------
                        if ylabel.find('\\\\') > -1:
                            ylabel_d = ylabel.split('\\\\')
                            ylabel = ''
                            for n in range(len(ylabel_d)):
                                ylabel += ylabel_d[n]
                                if n < len(ylabel_d)-1:
                                    ylabel += '\\'
                        #---------------------------------------

                        ylabel = ylabel.rstrip('\'')



                        self.ylabelEdit.setText(ylabel)
                        self.labelradio.setChecked(True)
                        break
            # ------------------------------------------------------

                #xlog ---------------------------------------
                len_read = len(read_py)
                for n in range(len(read_py)):
                    num = len_read-1-n
                    #-----------------
                    moji1 = 'plt.xscale(\"log\")'
                    #-----------------
                    if read_py[num].find(moji1) > -1:
                        self.xradio.setChecked(True)
                        break
            # ------------------------------------------------------
                #ylog ---------------------------------------
                len_read = len(read_py)
                for n in range(len(read_py)):
                    num = len_read-1-n
                    #-----------------
                    moji1 = 'plt.yscale(\"log\")'
                    #-----------------
                    if read_py[num].find(moji1) > -1:
                        self.yradio.setChecked(True)
                        break
            # ------------------------------------------------------
                #legend ---------------------------------------
                len_read = len(read_py)
                for n in range(len(read_py)):
                    num = len_read-1-n
                    #-----------------
                    moji1 = 'plt.legend'
                    #-----------------
                    if read_py[num].find(moji1) > -1:
                        self.legendradio.setChecked(True)
                        break
            # ------------------------------------------------------

            # -------------------------------------------------------
            else:
                plot1 = []
                plot2 = []
                for l in open(filename).readlines():
                    data = l[:-1].split()
                    plot1 += [float(data[xnum])]
                    plot2 += [float(data[ynum])]

                self.log += ['plot1 = []']
                self.log += ['plot2 = []']
                self.log += ['for l in open(\'' + str(filename) + '\').readlines():']
                self.log += ['    data = l[:-1].split()']
                self.log += ['    plot1 += [float(data[' +str(xnum) + '])]']
                self.log += ['    plot2 += [float(data[' +str(ynum) + '])]']
                        
                plt.rcParams["font.size"] = fontsize
                #self.log += ['plt.rcParams[\"font.size\"] = '+ str(fontsize)]
                #xlog 
                if self.xradio.isChecked():
                    plt.xscale("log")
                    #self.log += ['plt.xscale(\"log\")']
                if self.yradio.isChecked():
                    plt.yscale("log")
                    #self.log += ['plt.yscale(\"log\")']
                #lim 
                if self.liradio.isChecked():
                    plt.xlim(float(xmin),float(xmax))
                    plt.ylim(float(ymin),float(ymax))
                    #self.log += ['plt.xlim(' + str(xmin) + ',' + str(xmax) + ')']
                    #self.log += ['plt.ylim(' + str(ymin) + ',' + str(ymax) + ')']
                

                #plot
                if lc in ["no"]:
                    if self.legendradio.isChecked():
                        plt.plot(plot1,plot2,linestyle = lt,lw = lw,label = labell)
                        #---------------------------------------
                        if labell.find('\\') > -1:
                            label_d = labell.split('\\')
                            labell = ''
                            for n in range(len(label_d)):
                                labell += label_d[n]
                                if n < len(label_d)-1:
                                    labell += '\\'
                                    labell += '\\'
                        #---------------------------------------
                        self.log += ['plt.plot(plot1,plot2,linestyle = \''\
                                + str(lt) + '\' ,lw = ' + str(lw) + ',label = \' '+ str(labell)+ '\')']
                    else:
                        plt.plot(plot1,plot2,linestyle = lt,lw = lw)
                        self.log += ['plt.plot(plot1,plot2,linestyle =\''\
                                + str(lt) + '\',lw = ' + str(lw) + ')']
                else:
                    if self.legendradio.isChecked():
                        plt.plot(plot1,plot2,linestyle = lt,lw = lw,color = lc ,label = labell)
                        #---------------------------------------
                        if labell.find('\\') > -1:
                            label_d = labell.split('\\')
                            labell = ''
                            for n in range(len(label_d)):
                                labell += label_d[n]
                                if n < len(label_d)-1:
                                    labell += '\\'
                                    labell += '\\'
                        #---------------------------------------
                        self.log += ['plt.plot(plot1,plot2,linestyle =\''\
                                + str(lt) + '\',lw = ' + str(lw) + ',color = \''+ str(lc) \
                                + '\',label = \''+ str(labell)+ '\')']
                    else:
                        plt.plot(plot1,plot2,linestyle = lt,lw = lw,color = lc )
                        self.log += ['plt.plot(plot1,plot2,linestyle =\''+ str(lt) + '\',lw = '\
                                + str(lw) + ',color = \''+ str(lc)+ '\')']

                if self.legendradio.isChecked():
                    legend_size = self.size_legend.text()
                    legend_loc = self.loclegend.currentIndex()
                    lege = find_legend(legend_loc)
                    plt.legend(loc = lege,prop={'size':legend_size})

                if self.labelradio.isChecked():
                    plt.xlabel(xlabel,fontsize=label_size)
                    plt.ylabel(ylabel,fontsize=label_size)
                    xlabel1 = xlabel    
                    ylabel1 = ylabel    
                    #---------------------------------------
                    if xlabel1.find('\\') > -1:
                        xlabel_d = xlabel1.split('\\')
                        xlabel1 = ''
                        for n in range(len(xlabel_d)):
                            xlabel1 += xlabel_d[n]
                            if n < len(xlabel_d)-1:
                                xlabel1 += '\\'
                                xlabel1 += '\\'
                    #---------------------------------------
                    #---------------------------------------
                    if ylabel1.find('\\') > -1:
                        ylabel_d = ylabel1.split('\\')
                        ylabel1 = ''
                        for n in range(len(ylabel_d)):
                            ylabel1 += ylabel_d[n]
                            if n < len(ylabel_d)-1:
                                ylabel1 += '\\'
                                ylabel1 += '\\'
                    #---------------------------------------
                


                        
            if self.labelradio.isChecked():
                self.log += ['plt.xlabel(\''+ str(xlabel1)+'\',fontsize='+str(label_size) + ')']
                self.log += ['plt.ylabel(\''+ str(ylabel1)+'\',fontsize='+str(label_size) + ')']
                        
            if self.xradio.isChecked():
                self.log += ['plt.xscale(\"log\")']
            if self.yradio.isChecked():
                self.log += ['plt.yscale(\"log\")']
            #lim 
            if self.liradio.isChecked():
                self.log += ['plt.xlim(' + str(xmin) + ',' + str(xmax) + ')']
                self.log += ['plt.ylim(' + str(ymin) + ',' + str(ymax) + ')']

            if self.legendradio.isChecked():
                self.log += ['plt.legend(loc =\''+str(lege)+ '\',prop={\'size\':'+ str(legend_size) +'})']

            plt.tight_layout()
            self.log += ['plt.tight_layout()']


            self.canvas.draw() 






            #----------------------------------------------------------









def main(args):
    app = QApplication(sys.argv)
    form = MyWidget()
    form.resize(1200,300)
    form.show()

    sys.exit(app.exec_())

if __name__== "__main__":
    main(sys.argv)
        

