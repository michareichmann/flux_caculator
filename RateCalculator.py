#!/usr/bin/env python
__author__ = 'micha'

# ============================================
# IMPORTS
# ============================================
from Tkinter import *
from collections import OrderedDict


ew = 10

# ============================================
# CLASS DEFINITION
# ============================================
class Gui:
    def __init__(self):
        # gui
        self.root = Tk()
        self.entries = self.create_entries()
        self.labels = self.create_labels()
        self.names = self.create_names()
        self.var_results = self.create_var_results()
        self.results = self.create_results()
        self.close = Button(self.root, text='Close', command=self.root.destroy)
        self.clear = Button(self.root, text='Clear', command=self.clear)
        self.update = Button(self.root, text='Update', command=self.update_var_results)
        self.config_root()
        self.make_gui()

    def config_root(self):
        self.root.title('Flux Calculator')
        self.root.geometry('+800-400') #530x250

    def clear(self):
        no = ['area1', 'area2']
        for key, box in self.entries.iteritems():
            if key not in no:
                box.delete(0, 'end')

    def create_var_results(self):
        dic = OrderedDict()
        dic['flux coinc'] = StringVar()
        dic['flux calc'] = StringVar()
        return dic

    def update_var_results(self):
        for1 = float(self.entries['for1'].get())
        for2 = float(self.entries['for2'].get())
        forc = float(self.entries['coinc'].get())
        area1 = float(self.entries['area1'].get())
        area2 = float(self.entries['area2'].get())
        flux_coinc = 10. * forc / min(area1, area2)
        flux_calc = 5. * (for1 / area1 + for2 / area2)
        self.var_results['flux coinc'].set('{0:2.1f}'.format(flux_coinc))
        self.var_results['flux calc'].set('{0:2.1f}'.format(flux_calc))

    def create_names(self):
        dic = OrderedDict()
        dic['flux coinc'] = Label(self.root, text='Flux FORC:', width=14, anchor=W, font='font/Font 10 bold')
        dic['flux calc'] = Label(self.root, text='Flux Calculated:', anchor=W, width=14, font='font/Font 10 bold')
        return dic

    def create_results(self):
        dic = OrderedDict()
        dic['flux coinc'] = Entry(self.root, textvar=self.var_results['flux coinc'], font='font/Font 16 bold', width=8, justify=CENTER)
        dic['flux calc'] = Entry(self.root, textvar=self.var_results['flux calc'], font='font/Font 16 bold', width=8, justify=CENTER)
        return dic

    def create_entries(self):
        dic = OrderedDict()
        dic['coinc'] = Entry(self.root, width=ew, justify=CENTER)
        dic['for1'] = Entry(self.root, width=ew, justify=CENTER)
        dic['for2'] = Entry(self.root, width=ew, justify=CENTER)
        dic['area1'] = Entry(self.root, width=ew, justify=CENTER)
        dic['area2'] = Entry(self.root, width=ew, justify=CENTER)
        return dic

    def create_labels(self):
        dic = OrderedDict()
        dic['coinc'] = Label(self.root, text='FORC [Hz]')
        dic['for1'] = Label(self.root, text='FOR 1 [Hz]')
        dic['for2'] = Label(self.root, text='FOR 2 [Hz]')
        dic['area1'] = Label(self.root, text='area 1 [mm^2]')
        dic['area2'] = Label(self.root, text='area 2 [mm^2')
        return dic

    def make_gui(self):
        i = 0
        for label, entry in zip(self.labels.values(), self.entries.values()):
            label.grid(row=i)
            entry.grid(row=i, column=1)
            i += 1
        j = 0
        for label, msg in zip(self.names.values(), self.results.values()):
            label.grid(row=j, column=2, rowspan=2, pady=10, padx=12)
            msg.grid(row=j, column=3, rowspan=2, pady=10, padx=12)
            j += 2
        self.clear.grid(row=i + 1)
        self.close.grid(row=i + 1, column=1)
        self.update.grid(row=i + 1, column=2)

if __name__ == '__main__':
    t = Gui()
    t.root.mainloop()