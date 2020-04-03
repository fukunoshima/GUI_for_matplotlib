import matplotlib
matplotlib.rcParams['ps.useafm'] = True
matplotlib.rcParams['pdf.use14corefonts'] = True
matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt
plt.figure(figsize=(8,6))
############### end setting ####################
plot1 = []
plot2 = []
for l in open('').readlines():
    data = l[:-1].split()
    plot1 += [float(data[2])]
    plot2 += [float(data[3])]
plt.rcParams["font.size"] = 18
plt.plot(plot1,plot2,linestyle ='-',lw = 2)
plt.tight_layout()
plt.savefig('')
plt.close()
