import jaco2

class robotControl:
    def init_robot():
        jaco2.init_robot()
    
    def close_robot():
        jaco2.close_robot

    def init_fingers():
        jaco2.init_fingers()

    def send_basic_trajectory():
        jaco2.send_basic_trajectory()
    
    def move_home():
        jaco2.move_home()
    
    def set_type_velocity():
        jaco2.set_type_velocity()
    
    def set_type_position():
        jaco2.set_type_position()
    
    def get_general_informations():
        return(jaco2.get_general_informations())



