import tkinter as tk

root = tk.Tk()
root.title('AtomBrowser')
canvas1 = tk.Canvas(root, width=400, height=300)
canvas1.pack()

entry1 = tk.Entry(root)

canvas1.create_window(200, 140, window=entry1)
def AtomeBrowser():
    sym = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K',
           'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb',
           'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs',
           'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta',
           'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa',
           'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt',
           'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og']
    masa = ['1,007 94 g/mol', '4,002 602 g/mol', '6,941 g/mol', '9,012 182 g/mol', '10,811 g/mol', '12,011 g/mol',
            '14,006 74 g/mol', '15,999 4 g/mol', '18,998 403 2 g/mol', '20,179 7 g/mol', '22,989 768 g/mol',
            '24,305 g/mol', '26,981 539 g/mol', '28,085 5 g/mol', '30,973 762 g/mol', '32,066 g/mol', '35,452 7 g/mol',
            '39,948 g/mol', '39,098 3 g/mol', '40,078 g/mol', '44,955 91 g/mol', '47,88 g/mol', '50,941 5 g/mol',
            '51,996 1 g/mol', '54,938 05 g/mol', '55,847 g/mol', '58,933 2 g/mol', '58,69 g/mol', '63,546 g/mol',
            '65,39 g/mol', '69,723 g/mol', '72,61 g/mol', '74,921 59 g/mol', '78,96 g/mol', '79,904 g/mol',
            '83,8 g/mol', '85,467 8 g/mol', '87,62 g/mol', '88,905 85 g/mol', '91,224 g/mol', '92,906 38 g/mol',
            '95,94 g/mol', '98,906 3 g/mol', '101,07 g/mol', '102,905 5 g/mol', '106,42 g/mol', '107,868 2 g/mol',
            '112,411 g/mol', '114,82 g/mol', '118,71 g/mol', '121,75 g/mol', '127,6 g/mol', '126,904 47 g/mol',
            '131,29 g/mol', '132,905 43 g/mol', '137,327 g/mol', '138,905 5 g/mol', '140,115 g/mol', '140,907 65 g/mol',
            '144,24 g/mol', '146,915 1 g/mol', '150,36 g/mol', '151,965 g/mol', '157,25 g/mol', '158,925 34 g/mol',
            '162,5 g/mol', '164,930 32 g/mol', '167,26 g/mol', '168,934 21 g/mol', '173,04 g/mol', '174,967 g/mol',
            '178,49 g/mol', '180,947 9 g/mol', '183,85 g/mol', '186,207 g/mol', '190,2 g/mol', '192,22 g/mol',
            '195,08 g/mol', '196,966 54 g/mol', '200,59 g/mol', '204,383 3 g/mol', '207,2 g/mol', '208,980 37 g/mol',
            '208,982 4 g/mol', '209,987 1 g/mol', '222,017 6 g/mol', '223,019 7 g/mol', '226,025 4 g/mol',
            '227,027 8 g/mol', '232,038 1 g/mol', '231,035 9 g/mol', '238,028 9 g/mol', '237,048 2 g/mol',
            '244,064 2 g/mol', '243,061 4 g/mol', '247,070 3 g/mol', '247,070 3 g/mol', '251,079 6 g/mol',
            '252,082 9 g/mol', '257,095 1 g/mol', '258,098 6 g/mol', '259,100 9 g/mol', '260,105 3 g/mol',
            '261,108 7 g/mol', '262,113 8 g/mol', '263,118 2 g/mol', '262,122 9 g/mol', '265 g/mol', '266 g/mol',
            '269 g/mol', '272 g/mol', '277 g/mol', '286 g/mol']
    masv = ['0,084 g/l', '0,17 g/l', '0,53 g/cm3', '1,85 g/cm3', '2,46 g/cm3', '3,51 g/cm3', '1,17 g/l', '1,33 g/l',
            '1,58 g/l', '0,84 g/l', '0,97 g/cm3', '1,74 g/cm3', '2,70 g/cm3', '2,33 g/cm3', '1,82 g/cm3', '2,06 g/cm3',
            '2,95 g/l', '1,66 g/l', '0,86 g/cm3', '1,54 g/cm3', '2,99 g/cm3', '4,51 g/cm3', '6,09 g/cm3', '7,14 g/cm3',
            '7,44 g/cm3', '7,87 g/cm3', '8,89 g/cm3', '8,91 g/cm3', '8,92 g/cm3', '7,14 g/cm3', '5,91 g/cm3',
            '5,32 g/cm3', '5,72 g/cm3', '4,82 g/cm3', '3,14 g/cm3', '3,48 g/l', '1,53 g/cm3', '2,63 g/cm3',
            '4,47 g/cm3', '6,51 g/cm3', '8,58 g/cm3', '10,28 g/cm3', '11,49 g/cm3', '12,45 g/cm3', '12,41 g/cm3',
            '12,02 g/cm3', '10,49 g/cm3', '8,64 g/cm3', '7,31 g/cm3', '7,29 g/cm3', '6,69 g/cm3', '6,25 g/cm3',
            '4,94 g/cm3', '4,49 g/l', '1,90 g/cm3', '3,65 g/cm3', '6,16 g/cm3', '6,77 g/cm3', '6,48 g/cm3',
            '7,00 g/cm3', '7,22 g/cm3', '7,54 g/cm3', '5,25 g/cm3', '7,89 g/cm3', '8,25 g/cm3', '8,56 g/cm3',
            '8,78 g/cm3', '9,05 g/cm3', '9,32 g/cm3', '6,97 g/cm3', '9,84 g/cm3', '13,31 g/cm3', '16,68 g/cm3',
            '19,26 g/cm3', '21,03 g/cm3', '22,61 g/cm3', '22,65 g/cm3', '21,45 g/cm3', '19,32 g/cm3', '13,55 g/cm3',
            '11,85 g/cm3', '11,34 g/cm3', '9,80 g/cm3', '9,20 g/cm3', '9,23 g/l', '5,50 g/cm3', '10,07 g/cm3',
            '11,72 g/cm3', '15,37 g/cm3', '18,97 g/cm3', '20,48 g/cm3', '19,74 g/cm3', '13,67 g/cm3', '13,51 g/cm3',
            '13,25 g/cm3', '15,1 g/cm3', '16 g/cm3']
    date = ['1766', '1895', '1817', '1797', '1808', 'inconnue', '1772', '1774', '1886', '1898', '1807', '1755', '1825',
            '1824', '1669', 'inconnue', '1774', '1894', '1807', '1808', '1879', '1791', '1801', '1797', '1774',
            'inconnue', '1735', '1751', 'inconnue', 'inconnue', '1875', '1886', 'v. 1250', '1817', '1826', '1898',
            '1861', '1790', '1794', '1789', '1801', '1778', '1937', '1844', '1803', '1803', 'inconnue', '1817', '1863',
            'inconnue', 'inconnue', '1782', '1811', '1898', '1860', '1808', '1839', '1803', '1895', '1895', '1945',
            '1879', '1901', '1880', '1843', '1886', '1879', '1842', '1879', '1878', '1907', '1923', '1802', '1783',
            '1925', '1803', '1803', '1557', 'inconnue', 'inconnue', '1861', 'inconnue', '1540', '1898', '1940', '1900',
            '1939', '1898', '1899', '1829', '1917', '1789', '1940', '1940', '1944', '1944', '1949', '1950', '1952',
            '1952', '1955', '1958/66', '1961/71', '1964/69', '1967/70', '1974', '1976/81', '1984', '1982', '1994',
            '1994', '1996', '2004', '2004', '2010', '2004', '2010', '2006']
    name = ['Hydrogène', 'Hélium', 'Lithium', 'Béryllium', 'Bore', 'Carbone', 'Azote', 'Oxygène', 'Fluor', 'Néon',
            'Sodium', 'Magnésium', 'Aluminium', 'Silicium', 'Phosphore', 'Soufre', 'Chlore', 'Argon', 'Potassium',
            'Calcium', 'Scandium', 'Titane', 'Vanadium', 'Chrome', 'Manganèse', 'Fer', 'Cobalt', 'Nickel', 'Cuivre',
            'Zinc', 'Gallium', 'Germanium', 'Arsenic', 'Sélénium', 'Brome', 'Krypton', 'Rubidium', 'Strontium',
            'Yttrium', 'Zirconium', 'Niobium', 'Molybdène', 'Technétium', 'Ruthénium', 'Rhodium', 'Palladium', 'Argent',
            'Cadmium', 'Indium', 'Étain', 'Antimoine', 'Tellure', 'Iode', 'Xénon', 'Césium', 'Baryum', 'Lanthane',
            'Cérium', 'Praséodyme', 'Néodyme', 'Prométhium', 'Samarium', 'Europium', 'Gadolinium', 'Terbium',
            'Dysprosium', 'Holmium', 'Erbium', 'Thulium', 'Ytterbium', 'Lutécium', 'Hafnium', 'Tantale', 'Tungstène',
            'Rhénium', 'Osmium', 'Iridium', 'Platine', 'Or', 'Mercure', 'Thallium', 'Plomb', 'Bismuth', 'Polonium',
            'Astate', 'Radon', 'Francium', 'Radium', 'Actinium', 'Thorium', 'Protactinium', 'Uranium', 'Neptunium',
            'Plutonium', 'Américium', 'Curium', 'Berkélium', 'Californium', 'Einsteinium', 'Fermium', 'Mendélévium',
            'Nobélium', 'Lawrencium', 'Rutherfordium', 'Dubnium', 'Seaborgium', 'Bohrium', 'Hassium', 'Meitnérium',
            'Darmstadtium', 'Roentgenium', 'Copernicium', 'Nihonium', 'Flérovium', 'Moscovium', 'Livermorium',
            'Tennesse', 'Oganesson']
    Z = ['1', '2', '3', 'z4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
         '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38',
         '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56',
         '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74',
         '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92',
         '93', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109',
         '110', '111', '112', '113', '114', '115', '116', '117', '118']
    liste_orbitales = ((1, 's', 2), (2, 's', 2), (2, 'p', 6), (3, 's', 2), (3, 'p', 6),
                       (4, 's', 2), (3, 'd', 10), (4, 'p', 6), (5, 's', 2), (4, 'd', 10), (5, 'p', 6),
                       (6, 's', 2), (4, 'f', 14), (5, 'd', 10), (6, 'p', 6),
                       (7, 's', 2), (5, 'f', 14), (6, 'd', 10), (7, 'p', 6))

    l = []
    for a in masv:
        p = masv.index(a)
        b = date[p]
        e = masa[p]
        d = sym[p]
        nn = Z[p]
        j = ('its Z : ') + nn + ('\nits symbole : ') + d + ('\ndiscovred in : ') + b + ('\nits atomique mass : ') + a + ('\nits volimique mass : ') + e
        l.append(j)

    d = dict(zip(name, l))

    x1 = entry1.get()
    x = d[x1.capitalize()]

    label1 = tk.Label(root, text=x, fg = 'red')
    canvas1.create_window(200, 230, window=label1)
l1 = tk.Label(root, text='-----------------------------------------------------------------------------------------', fg ='black', width =60, height =3)
canvas1.create_window(200, 28, window=l1)
l2 = tk.Label(root, text='Write the name of the atom that you are locking for', fg = 'black', width = 40, height =3)
canvas1.create_window(200, 104, window=l2)
l3 = tk.Label(root, text='---------------------------------------By Oth---------------------------------------', fg ='black', width =60, height = 2)
canvas1.create_window(200, 290,window=l3)              
button1 = tk.Button(text='𝚜𝚎𝚊𝚛𝚌𝚑 🔍', command=AtomeBrowser)
canvas1.create_window(200, 180, window=button1)
label3 = tk.Label()

root.mainloop()




