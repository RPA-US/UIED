from os.path import join as pjoin
import os


class Config:

    def __init__(self, cnn_type="custom-v2"):
        # setting CNN (graphic elements) model
        self.image_shape = (64, 64, 3)

        self.project_root = os.path.dirname(os.path.abspath(__file__))[:os.path.dirname(os.path.abspath(__file__)).find("detección")+13]

        # For CNN trained on Generalized Dataset (Wireframes & subset of ReDraw Dataset)
        if cnn_type == "cnn-generalized":
            self.CNN_PATH = 'models/cnn-generalized.h5'
            self.element_class = ['checkbox', 'dash', 'div_rect', 'div_round', 'down_arrow', 'image', 'left_arrow',
                                'radio', 'right_arrow', 'scroll', 'text', 'toggle_switch', 'up_arrow']
            self.class_number = len(self.element_class)

            self.COLOR = {'checkbox': (0, 255, 0), 'dash': (0, 0, 255), 'div_rect': (255, 166, 166),
                        'div_round': (255, 166, 0),
                        'down_arrow': (77, 77, 255), 'image': (166, 0, 255), 'left_arrow': (255, 0, 166),
                        'radio': (166, 166, 166),
                        'right_arrow': (0, 166, 255), 'scroll': (50, 21, 255),
                        'text': (80, 166, 66), 'toggle_switch': (0, 66, 80), 'up_arrow': (88, 66, 0),
                        'Compo':(0, 0, 255), 'Text':(169, 255, 0), 'Block':(80, 166, 66)}

        
        elif cnn_type == "custom-v2":
            self.CNN_PATH = 'models/custom-v2.h5'
            self.element_class = ['button',
                                'checkbox_checked',
                                'checkbox_unchecked',
                                'image',
                                'radio',
                                'scroll',
                                'seekbar',
                                'text',
                                'text_input',
                                'toggle_switch']
            self.class_number = len(self.element_class)

            self.COLOR = {'button': (0, 255, 0), 'checkbox_checked': (0, 0, 255), 'checkbox_unchecked': (255, 166, 166),
                        'image': (255, 166, 0),
                        'radio': (77, 77, 255), 'scroll': (166, 0, 255),
                        'seekbar': (166, 166, 166),
                        'text': (0, 166, 255), 'text_input': (50, 21, 255),
                        'toggle_switch': (80, 166, 66),
                        'Compo':(0, 0, 255), 'Text':(169, 255, 0), 'Block':(80, 166, 66)}
