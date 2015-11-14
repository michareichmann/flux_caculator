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
        self.other_labels = self.creat_other_labels()
        self.names = self.create_names()
        self.var_results = self.create_var_results()
        self.results = self.create_results()
        self.close = Button(self.root, text='Close', command=self.root.destroy)
        self.clear_but = Button(self.root, text='Clear Rates', command=self.clear, width=8)
        self.update = Button(self.root, text='Update', command=self.update_var_results, width=11)
        self.config_root()
        self.make_gui()

    def config_root(self):
        self.root.title('Flux Calculator')
        self.root.geometry('+800-400')  # 530x250

    def clear(self):
        no = ['area1', 'area2']
        for key, box in self.entries.iteritems():
            if key not in no:
                box.delete(0, 'end')

    @staticmethod
    def create_var_results():
        dic = OrderedDict()
        dic['flux coinc'] = StringVar()
        dic['flux calc'] = StringVar()
        return dic

    def creat_other_labels(self):
        dic = OrderedDict()
        dic['main'] = Label(self.root, text='Flux Calculator', font='font/Font 16 bold')
        dic['result'] = Label(self.root, text='Result', font='font/Font 10 bold')
        dic['rate'] = Label(self.root, text='Rates', font='font/Font 10 bold')
        dic['area'] = Label(self.root, text='Unmasked Area', font='font/Font 10 bold')
        return dic

    def update_var_results(self):
        try:
            for1 = float(self.entries['for1'].get())
            for2 = float(self.entries['for2'].get())
            forc = float(self.entries['coinc'].get())
            area1 = float(self.entries['area1'].get())
            area2 = float(self.entries['area2'].get())
            flux_coinc = 10. * forc / min(area1, area2)
            flux_calc = 5. * (for1 / area1 + for2 / area2)
            self.var_results['flux coinc'].set('{0:2.1f}'.format(flux_coinc))
            self.var_results['flux calc'].set('{0:2.1f}'.format(flux_calc))
        except ValueError:
            flux_coinc = 'ERROR'
            flux_calc = 'ERROR'
            self.var_results['flux coinc'].set(flux_coinc)
            self.var_results['flux calc'].set(flux_calc)
        # self.clear()

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
        dic['coinc'] = Label(self.root, text='FORC [Hz]', anchor=E, width=11)
        dic['for1'] = Label(self.root, text='FOR 1 [Hz]', anchor=E, width=11)
        dic['for2'] = Label(self.root, text='FOR 2 [Hz]', anchor=E, width=11)
        dic['area1'] = Label(self.root, text=u'area 1 [mm\u00B2]', anchor=E, width=11)
        dic['area2'] = Label(self.root, text=u'area 2 [mm\u00B2]', anchor=E, width=11)
        return dic

    def make_gui(self):
        self.other_labels['main'].grid(columnspan=4, pady=10)
        i = 2
        self.other_labels['rate'].grid(row=1, columnspan=2, pady=8)
        self.other_labels['result'].grid(row=1, column=3, pady=8)
        for label, entry in zip(self.labels.values(), self.entries.values()):
            k = i + 2 if i > 4 else i
            label.grid(row=k)
            entry.grid(row=k, column=1)
            i += 1
        j = 2
        for label, entry in zip(self.names.values(), self.results.values()):
            label.grid(row=j, column=2, rowspan=2, padx=10)
            entry.grid(row=j, column=3, rowspan=2, padx=10)
            j += 2
        self.clear_but.grid(row=5, column=1, pady=10, sticky=N)
        self.other_labels['area'].grid(row=6, columnspan=2, pady=8)
        self.update.grid(row=6, column=3)
        self.close.grid(row=i + 2, column=3, pady=8)


if __name__ == '__main__':
    t = Gui()
    t.root.mainloop()
