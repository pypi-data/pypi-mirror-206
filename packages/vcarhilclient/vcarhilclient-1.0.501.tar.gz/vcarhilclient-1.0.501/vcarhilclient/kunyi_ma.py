from ctypes import *
from ctypes import wintypes
import os
import pathlib
CDLL(r"C:\Users\windy\Downloads\1.1.0.230330\mrtd\mrtd_w64\bin\jsoncpp.dll")

dll_path = os.path.join(pathlib.Path(__file__).parent, "ma.vcar.dll")
ma_lib = CDLL(dll_path)
from Enums import *


class ma_enviroment():
    def __init__(self):
        self.current_env_p = None
        self.freed = False

    def create(self):
        rc = ma_status_t()
        rc.value = -99
        ma_lib.ma_enviroment_create.argtypes = [POINTER(ma_status_t)]
        ma_lib.ma_enviroment_create.restype = c_void_p
        self.current_env_p = ma_lib.ma_enviroment_create(pointer(rc))
        self.freed = False

        return rc, self.current_env_p

    def free(self):
        if self.current_env_p == None:
            return -99
        ma_lib.ma_enviroment_free.argtypes = [c_void_p]
        ma_lib.ma_enviroment_free.restype = ma_status_t
        rc = ma_lib.ma_enviroment_free(self.current_env_p)
        self.freed = True
        return rc



class ma_model():
    def __init__(self):
        self.model_handel = None
        self.freed = False

    def new_ma_model_instance(self):
        rc = ma_status_t()
        rc.value = -99
        ma_lib.ma_model_instance_new.argtypes = [POINTER(ma_status_t)]
        ma_lib.ma_model_instance_new.restype = c_void_p
        self.model_handel = ma_lib.ma_model_instance_new(pointer(rc))
        self.freed = False
        return rc, self.model_handel

    def init_ma_model_instance(self, name, input_port_num, output_port_num, measurement_num,
                                     calibration_num, event_num, runnable_num):
        bs = name.encode('utf-8')
        mn_pointer = c_char_p(bs)
        ma_lib.ma_model_instance_init.argtypes = [c_void_p, c_char_p, c_uint32, c_uint32, c_uint32, c_uint32,
                                                  c_uint32, c_uint32]
        ma_lib.ma_model_instance_init.restype = ma_status_t
        error_code = ma_lib.ma_model_instance_init(self.model_handel, mn_pointer, input_port_num, output_port_num,
                                                   measurement_num, calibration_num, event_num, runnable_num)

    def create_ma_model_instance(self, name, input_port_num, output_port_num, measurement_num,
                                     calibration_num, event_num, runnable_num):
        bs = name.encode('utf-8')
        mn_pointer = c_char_p(bs)

        rc = ma_status_t()
        rc.value = -99

        ma_lib.ma_model_instance_create.argtypes = [c_char_p, c_uint32, c_uint32, c_uint32, c_uint32,
                                                  c_uint32, c_uint32, POINTER(ma_status_t)]
        ma_lib.ma_model_instance_create.restype = c_void_p
        self.model_handel = ma_lib.ma_model_instance_create(mn_pointer, input_port_num, output_port_num,
                                                   measurement_num, calibration_num, event_num,
                                                            runnable_num, pointer(rc))
        self.freed = False

    def free_ma_model_instance(self):

        ma_lib.ma_model_instance_free.argtypes = [c_void_p]
        ma_lib.ma_model_instance_free.restype = ma_status_t
        error_code = ma_lib.ma_model_instance_free(self.model_handel)
        self.freed = True
        return error_code
























