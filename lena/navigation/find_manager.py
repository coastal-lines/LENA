from lena.navigation.template_matching.template_matching import TemplateMatchingElement
from lena.elements.objects.screenshot_element import ImageSourceObject
from lena.navigation.object_detection.base_find_actions import BaseFindActions
from lena.utils import general_helpers, files_helper, debug


class FindManager(TemplateMatchingElement):

    def __init__(self, detection_mode: BaseFindActions):
        super().__init__()
        self.__detection_mode = detection_mode

    def __create_image_source(self, *args):
        if len(args) == 0:
            return ImageSourceObject(general_helpers.do_screenshot())
        else:
            return ImageSourceObject(files_helper.load_image(args[0]))

    def find_all_elements(self, *args):
        image_source = self.__create_image_source(*args)
        self.__detection_mode.find_all_elements(image_source)

        return image_source

    def find_element(self, element_type, *args):
        image_source = self.__create_image_source(*args)
        self.__detection_mode.find_element(image_source, element_type)

        return image_source

    def find_table_and_expand(self, table_index: int = 0):
        if hasattr(self.__detection_mode, 'find_table_and_expand'):
            image_source = self.__create_image_source()
            self.__detection_mode.find_table_and_expand(image_source, table_index)
        else:
            print("Write operation not supported for this mode.")

    def find_table_cell(self, column, row):
        if hasattr(self.__detection_mode, 'find_table_cell'):
            image_source = self.__create_image_source()
            self.__detection_mode.find_table_cell(image_source, column, row)
        else:
            print("Error: expand operations are not supported for current mode. Impossible to find custom cell.")

    def find_listbox_and_expand(self, listbox_index):
        if hasattr(self.__detection_mode, 'find_listbox_and_expand'):
            image_source = self.__create_image_source()
            self.__detection_mode.find_listbox_and_expand(image_source, listbox_index)
        else:
            print("Write operation not supported for this mode.")