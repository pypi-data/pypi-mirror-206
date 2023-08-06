from solutions import combinations

class Box():
    """
    Класс урны (коробки) для задачи об урнах

    Args:
        white (int): кол-во белых шаров (не является параметром)
        black (int): кол-во черных шаров (не является параметром)
        grabbing (int): кол-во шаров, забираемых из коробки
    
    Parameters:
        balls (list): массив длиной 2, хранящий информация о количестве Б и Ч шаров ([Б, Ч])

    Methods:
        None
    """
    def __init__(self, white:int=0, black:int=0, grabbing:int=0):
        self.balls = [white, black]
        self.grabbing = grabbing

class Hypotes():
    """
    Класс гипотезы для задачи об урнах

    Args:
        balls (list): массив, длиной 2, обозначающий количество белых и чёрных шаров ([Б, Ч])
        probability (float): вероятность наступления гипотезы
        id (int): порядковый номер гипотезы
    
    Parameters:
        depend_probability (float): вероятность достать Б шар из урны с шарами self.balls
        hypo_text (str): строка формата 'H(id): nБ mЧ; P(H(id)) = p; P(A|H(id)) = p`'
        summary_text (str): строка, использующаяся для составления строки для уравнения суммы вероятностей гипотез

    Methods:
        None
    """
    def __init__(self, balls=None, probability=0, id=0):
        if balls == None:
            balls = [0,0]
        self.balls = balls
        self.probability = probability
        self.depend_probability = balls[0]/sum(balls)
        self.id = id
        self.hypo_text = f"H{self.id}: {self.balls[0]} Б, {self.balls[1]} Ч; P(H{self.id}) = {self.probability}; P(A|H{self.id}) = {self.depend_probability}"
        self.summary_text = f"P(A|H{self.id})P(H{self.id})"

class Hypoteses():
    """
    Класс, использующийся только для решения задачи об урнах. Бесполезен вне решения.

    Methods:
        check_correctly
        get_whites_n_blacks_from_boxes
        get_from_boxes
        get_zn
    """
    def __init__(self, boxes):
        self.U = boxes
        self.P = 0
        self.main_z = 1

    def check_correctly(self, mnoz, whites, totalWhite):#проверяет, что все предоставленные слагаемые
                                                        #содержат требуемое по условию количество шаров
        new_mnoz = []
        for i in range(0, len(mnoz)):
            if whites[i] == totalWhite:
                new_mnoz.append(mnoz[i])
        return(new_mnoz)
    
    def get_whites_n_blacks_from_boxes(self, wGrab=0, id=0, whites=None, mnoz=None, totalW=0):#посчитать для взятия "wGrab" белых шаров из
                                                                            #оставшихся урн, включая урну с индексом "id"
        if whites == None:
            whites = []
        if mnoz == None:
            mnoz = []
        if id >= len(self.U):
            return self.check_correctly(mnoz, whites, totalW)
        
        grabbing = self.U[id].grabbing#сколько всего берём шаров из урны

        mx_kW = self.U[id].balls[0]#сколько всего Б шаров
        mx_kB = self.U[id].balls[1]#сколько всего Ч шаров

        mn_kW = grabbing - mx_kB#сколько минимум Б шаров потребуется
        kW = max(mn_kW, 0)#старт Б шаров
        kB = min(mx_kB, grabbing)#старт Ч шаров

        mx_kW = max(min([mx_kW, grabbing]), 0)#максимум можно взять из этой урны Б шаров

        if mnoz == []:#если множество слагаемых гипотезы пусто
            while kW <= mx_kW:#перебираем все возможные варианты взятия шаров из этой урны
                mnoz.append(1)
                whites.append(kW)
                mnoz[-1] *= combinations(kW, self.U[id].balls[0])*combinations(kB, self.U[id].balls[1])
                kW += 1
                kB -= 1
        else:#если множество слагаемых гипотезы не пусто
            new_mnoz = []
            new_whites = []
            while kW <= mx_kW:#перебираем все возможные варианты взятия шаров из этой урны
                editor = combinations(kW, self.U[id].balls[0])*combinations(kB, self.U[id].balls[1])
                for i in range(0, len(mnoz)):#каждое из существующих слагаемых умножаем на результат
                                            #перемножения перестановок Kw из Nw и Kb из Nb шаров
                    new_mnoz.append(mnoz[i]*editor)
                    new_whites.append(whites[i] + kW)
                kW += 1
                kB -= 1
            mnoz = new_mnoz
            whites = new_whites
        return self.get_whites_n_blacks_from_boxes(wGrab-kW, id+1, whites, mnoz, totalW)

    def get_from_boxes(self):#решает задачу через теорему гипотез
        grabGlob = 0#сколько всего берём шаров из урн
        whiteGlob, blackGlob = 0, 0
        for box in self.U:
            grabGlob += box.grabbing
            whiteGlob += box.balls[0]
            blackGlob += box.balls[1]
        
        if grabGlob > whiteGlob+blackGlob:
            return

        revealing_after_B = max(grabGlob-blackGlob, 0)

        gW = max(0, revealing_after_B)#от скольки белых шаров может находиться в n+1 урне (куда их все складывают)
        gW_end = min(whiteGlob, grabGlob)#до скольки белых шаров может находиться в n+1 урне

        hypoteses_P_array = []
        while gW <= gW_end:#генерируем гипотезы для всех возможных количеств Белых и Черных шаров
            hypoteses_P_array.append([sum(self.get_whites_n_blacks_from_boxes(gW, 0, [], [], gW))/self.get_zn(), gW, grabGlob-gW])
            gW += 1
        return hypoteses_P_array#массив вероятностей для всех гипотез

    def get_zn(self):#получить общий знаменатель для формулы вероятности гипотезы
        if self.main_z == 1:
            for i in range(len(self.U)):
                self.main_z *= combinations(self.U[i].grabbing, sum(self.U[i].balls))
        return self.main_z

class EttaTableCell():
    """
    Ячейка таблицы Етта, со значением и вероятностью

    Args:
        etta_value (int): значение СВ "Етта"
        good_th (int): количество удачных исходов
        all_th (int): количество всех исходов
        probability (float): вероятность

    Methods:
        reset_probability
    """
    def __init__(self, etta_value:int=0, good_th:int=1, all_th:int=1, probability:float=None):
        self.etta_value = etta_value
        self.good_th = good_th
        self.all_th = all_th
        self.probability = probability
        if self.probability == None:
            self.reset_probability()

    def reset_probability(self):
        self.probability = self.good_th/self.all_th

class EttaTable():
    """
    Таблица значений Етта

    Args:
        cells (): массив ячеек
    """
    def __init__(self, cells=None):
        self.cells = cells
        if self.cells == None:
            self.cells=[]

class Meetiner():
    """
    Класс, использующийся для решения задач типа встречи двух целей

    Args:
        start_time (float): начальный момент, относительно нулевой координаты, когда может появиться участник
        end_time (float): конечный момент, относительно нулевой координаты, когда может появиться участник
        waitind_time (float): кол-во меры, в течении которой участник ждёт
    
    Methods:
        calculate_square
    """
    def __init__(self, start_time:float=0, end_time:float='inf', waiting_time:float=1):
        if start_time >= 0:
            self.start_time = start_time
        else:
            self.start_time = 0
        if end_time >= 0:
            self.end_time = end_time
        else:
            self.end_time = float('inf')
        if waiting_time >= 0:
            self.waiting_time = waiting_time
        else:
            self.waiting_time = 1

    def calculate_square(self, maxEnd:float, waiter_time):
        return ((min(self.end_time, maxEnd) - self.start_time - waiter_time)**2)/2
