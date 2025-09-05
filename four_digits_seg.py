import time
from machine import Pin

class Seg4Digit:

    def __init__(self,seg_1,seg_2,seg_3 , seg_4 ,a, b, c, d,e,f,g,dp):
        self.seg_1 = Pin(seg_1,Pin.OUT)
        self.seg_2 = Pin(seg_2,Pin.OUT)
        self.seg_3 = Pin(seg_3,Pin.OUT)
        self.seg_4 = Pin(seg_4,Pin.OUT)
        
        self.seg_list = [self.seg_1,self.seg_2,self.seg_3,self.seg_4]
        
        self.a = Pin(a,Pin.OUT)
        self.b = Pin(b,Pin.OUT)
        self.c = Pin(c,Pin.OUT)
        self.d = Pin(d,Pin.OUT)         
        self.e = Pin(e,Pin.OUT)
        self.f = Pin(f,Pin.OUT)
        self.g = Pin(g,Pin.OUT)         
        self.dp = Pin(dp,Pin.OUT)
        
        self.led_list = [self.a,self.b,self.c,self.d,self.e,self.f,self.g,self.dp]
        
        self.number_dict = {
            #  [a, b, c, d, e, f, g, dp]
            0: [1, 1, 1, 1, 1, 1, 0, 0],
            1: [0, 1, 1, 0, 0, 0, 0, 0],
            2: [1, 1, 0, 1, 1, 0, 1, 0],
            3: [1, 1, 1, 1, 0, 0, 1, 0],
            4: [0, 1, 1, 0, 0, 1, 1, 0],
            5: [1, 0, 1, 1, 0, 1, 1, 0],
            6: [1, 0, 1, 1, 1, 1, 1, 0],
            7: [1, 1, 1, 0, 0, 0, 0, 0],
            8: [1, 1, 1, 1, 1, 1, 1, 0],
            9: [1, 1, 1, 1, 0, 1, 1, 0],
        }
    def clear(self):
        for seg in self.seg_list:
            seg.value(1)
        for led in self.led_list:
            led.value(0)
    def display_number(self,order,number):  
        logic_list = self.number_dict.get(number)
    
        if logic_list and 0 <= order < 4:   
            self.clear()
            self.seg_list[order].value(0)
            
            for i in range(len(logic_list)):
                self.led_list[i].value(logic_list[i])
    

    # 显示函数
    def display_4_number(self, number):
        # 判断参数是否超过 9999
        if number <= 9999:            
            # 初始化每个位置对应的数字列表
            number_list = []
            # 使用循环的方式获取数字列表
            for i in range(4):
                number_list.insert(0, number % 10)
                number //= 10  
        
        for i in range(len(number_list)):
            self.display_number(i, number_list[i])
            time.sleep_ms(5)
            
            