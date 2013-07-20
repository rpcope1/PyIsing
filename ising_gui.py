from Tkinter import *
import colorsys

class ising_gui(object):
    MIN_RED = MIN_GREEN = MIN_BLUE = 0x0
    MAX_RED = MAX_GREEN = MAX_BLUE = 0xFF    
    PIXEL_WIDTH = 10

    def __init__(self, grid_x, grid_y):
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.pixels = [(0, 0, 0) for i in range(self.grid_x * self.grid_y)]
        

        #Set up TK
        self.root = Tk()
        self.root.title("Ising Simulation %d x %d" % (self.grid_x, self.grid_y))
        self.root.resizable(0, 0)
        #Set up the frame for holding the Ising Simulation results.
        self.frame = Frame(self.root, bd=5, relief=SUNKEN)
        self.frame.pack(side = TOP)

        self.canvas = Canvas(self.frame,
                             width=self.PIXEL_WIDTH * self.grid_x,
                             height=self.PIXEL_WIDTH * self.grid_y,
                             bd=0, highlightthickness=0)
        self.canvas.pack()

        
        #Put Boxes here...
        self.TString = StringVar()
        self.EString = StringVar()
        self.GString = StringVar()    
        
        self.bframe = Frame(self.root)
        self.TLabel = Label(self.bframe, anchor=N, textvariable = self.TString)
        self.ELabel = Label(self.bframe, anchor=S, textvariable = self.EString)
        self.GLabel = Label(self.bframe, anchor=CENTER, textvariable = self.GString)   
        self.bframe.pack(side = BOTTOM)          
        self.root.update()
    
    def set_pixel(self, x, y, hsv):
        self.pixels[self.grid_x * y + x] = hsv

    def get_pixel(self, x, y):
        return self.pixels[self.grid_x * y + x]

    def set_temperature(self, temp):
        self.TString.set("Temperature: %f" % temp)
        self.TLabel.pack()

    def set_energy(self, energ):
        self.EString.set("Energy: %f" % energ)
        self.ELabel.pack()

    def set_correlation(self, cfunc):
        self.GString.set("Correlation: %f" % cfunc)
        self.GLabel.pack()
    
    def draw(self):
        self.canvas.delete(ALL)
        for x in range(len(self.pixels)):
            x_0 = (x % self.grid_x) * self.PIXEL_WIDTH
            y_0 = (x / self.grid_x) * self.PIXEL_WIDTH
            x_1 = x_0 + self.PIXEL_WIDTH
            y_1 = y_0 + self.PIXEL_WIDTH
            hue = "#%02x%02x%02x" % self._get_rgb(self.pixels[x])
            self.canvas.create_rectangle(x_0, y_0, x_1, y_1, fill=hue)
        self.canvas.update()

    def clear(self):
        for i in range(self.width * self.height):
            self.pixels[i] = (0, 0, 0)

    def _hsv_to_rgb(self, hsv):
        rgb = colorsys.hsv_to_rgb(*hsv)
        red = self.MAX_RED * rgb[0]
        green = self.MAX_GREEN * rgb[1]
        blue = self.MAX_BLUE * rgb[2]
        return (red, green, blue)

    def _get_rgb(self, hsv):
        red, green, blue = self._hsv_to_rgb(hsv)
        red = int(float(red) / (self.MAX_RED - self.MIN_RED) * 0xFF)
        green = int(float(green) / (self.MAX_GREEN - self.MIN_GREEN) * 0xFF)
        blue = int(float(blue) / (self.MAX_BLUE - self.MIN_BLUE) * 0xFF)
        return (red, green, blue)
