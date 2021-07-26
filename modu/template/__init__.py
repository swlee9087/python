from common.menu import print_menu
from modu.template.deflected_plot import TemperatureChangesOnMyBirthday
from modu.template.basic_plot import plot_show, plot_two_list_show, plot_two_list_show2, plot_two_list_show3, \
    plot_two_list_show4, plot_marker_show
if __name__ == '__main__':
    while 1:
        menu = print_menu(['exit', 'plot show', 'plot 2lists show', 'p2ls2', 'p2ls3', 'p2ls4', 'scatter', 'birthday temps'])
        if menu == 0:
            break
        elif menu == 1:
            plot_show()
        elif menu == 2:
            plot_two_list_show()
        elif menu == 3:
            plot_two_list_show2()
        elif menu == 4:
            plot_two_list_show3()
        elif menu == 5:
            plot_two_list_show4()
        elif menu == 6:
            plot_marker_show()
        elif menu == 7:
            TemperatureChangesOnMyBirthday().processing()
