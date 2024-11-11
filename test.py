from ribbon import Ribbon
from machine import root
ribbon = Ribbon()
import animation

ribbon.start_animation(animation.change_color)
#ribbon.display(animation.red)
root.mainloop()