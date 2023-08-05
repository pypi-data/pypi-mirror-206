import math
import re
from utils import Box, Hypotes, Hypoteses, EttaTable, EttaTableCell, Meetiner
from global_variables import regular_int, regular_float

def combinations(k:float=0,n:float=0):
    """
    Функция, считающая число сочетаний из n по k

    Args:
        k (float): аргумент k - количество повторений
        n (float): аргумент n - всего элементов

    Returns:
        float: результат применения формулы числа сочетаний
    """
    if k < 0 or n < 0:
        raise ValueError("ERROR: one or more argument's values are less than 0")
    return math.factorial(n)/(math.factorial(k)*math.factorial(n-k))

def buckets_n_balls_solution(boxes):
    """
    Находит ответ для вопроса 'какова вероятность достать Белый шар из n+1 урны' для задачи о n урнах с белыми и чёрными шарами, когда из каждой урны берут Ki шаров, перекладывают их в n+1 урну.
    Для решения используется теорема гипотез

    Args:
        boxes (list): массив объектов класса Box

    Returns:
        list: [list: массив объектов Hypotes, float: итоговая пероятность искомого события]
    """
    myHyp = Hypoteses(boxes)

    hypot_prob = myHyp.get_from_boxes()

    prob_final = 0
    ready_hipoteses = []
    for i in range(0, len(hypot_prob)):
        ready_hipoteses.append(Hypotes([hypot_prob[i][1], hypot_prob[i][2]], hypot_prob[i][0], i+1))
        prob_final += hypot_prob[i][0]*hypot_prob[i][1]/(hypot_prob[i][1]+hypot_prob[i][2])
    
    return(ready_hipoteses, prob_final)

def buckets_n_balls_terminal():
    """
    Решение задачи о n урнах с белыми и чёрными шарами, когда из каждой урны берут Ki шаров, перекладывают их в n+1 урну.
    """
    boxes = [Box() for _ in range(int(input("Введите количество урн: ")))]

    for i in range(len(boxes)):
        boxes[i].balls[0] = int(input(f"Кол-во Б шаров в {i+1} урне: "))
        print("\033[F                                                                       ", end="\r")
        boxes[i].balls[1] = int(input(f"Кол-во Ч шаров в {i+1} урне: "))
        print("\033[F                                                                       ", end="\r")
    print("Шары заданы.")

    for i in range(len(boxes)):
        boxes[i].grabbing = int(input(f"Сколько шаров берут из {i+1} урны: "))
        print("\033[F                                                                       ", end="\r")
    print("Кол-во взятых шаров задано.")

    result = buckets_n_balls_solution(boxes)

    print("Обозначим событие A - достать Белый шар")

    txt = "P(B) = "
    for hypo in result[0]:
        print(hypo.hypo_text)
        txt += hypo.summary_text + " + "
    
    print(f"Обозначим событие B - достать шар из {len(boxes)+1} урны")
    txt = txt[:-3]
    txt += f"\nP(B) = {result[1]}"
    print(txt)

def buckets_n_balls_request(text: str = None):
    """
    Решение задачи о n урнах с белыми и чёрными шарами, когда из каждой урны берут Ki шаров, перекладывают их в n+1 урну.
    Функция предоставляет ответы на запросы для этой задачи

    Args:
        text (str): текст запроса, который может быть None или вводом пользователя
    
    Returns:
        list: массив строчек ответа
    """
    if text == None:
        return ["""Введите количество урн (число n)
В следующих n строках введите количество белых и чёрных шаров (пара чисел через пробел) в i-ой урне
В последних n строках введите количество шаров, забираемых из i-ой урны"""]
    else:
        try:
            request = [int(parameter) for parameter in re.findall(regular_int, text)]

            answer = []

            box_num = request[0]

            boxes = [Box(request[1+2*i], request[2+2*i], request[1+box_num*2+i]) for i in range(box_num)]

            result = buckets_n_balls_solution(boxes)

            answer.append("Обозначим событие A - достать Белый шар")

            txt = "P(B) = "
            for hypo in result[0]:
                answer.append(hypo.hypo_text)
                txt += hypo.summary_text + " + "
            
            answer.append(f"Обозначим событие B - достать шар из {len(boxes)+1} урны")
            txt = txt[:-3]
            txt += f"\nP(B) = {result[1]}"
            answer.append(txt)
            return answer
        except:
            return ["""Возникла ошибка при обработке введённых данных. Проверьте правильность ввода."""]

def things_complexity_terminal():
    """
    Общее решение задачи о 'невнимательной секретарше' (сколько людей получат свои вещи)
    WARNING: Очень неоптимизированное! Не рекоммендую пытаться решить для количества людей > 11
    """
    humans = int(input("Введите количество человек: "))
    result = things_complexity_solution(humans)
    print("Таблица:")
    for cell in result.cells:
        print(f"E = {cell.etta_value}; P = {cell.probability} ({cell.good_th}/{cell.all_th})")
    for cell in result.cells:
        print(cell.good_th)

def things_complexity_solution(humans:int = 0):
    """
    Решение задачи о 'невнимательной секретарше' (сколько людей получат свои вещи)
    WARNING: Очень неоптимизированное! Не рекоммендую пытаться решить для количества людей > 11

    Args:
        humans (int): кол-во людей

    Returns:
        EttaTable: таблица ячеек таблицы
    """
    #следующей строчкой находим количество всех перестановок
    allPerestan = math.factorial(humans)

    #определяем таблицу
    myTable = EttaTable(cells=[])
    for j in range(0, humans+1):
        myTable.cells.append(EttaTableCell(j, 0, allPerestan))

    #Функция, проходящаяся по всем перестановкам, и записивыающая их в таблицу
    def goThrough(n, layer, used):
        if layer == humans:#раздали все предметы
            myTable.cells[n].good_th += 1
            return
        for ticket in range(0, humans):#раздаем следующий предмет
            if ticket not in used:#он ещё не использован
                if ticket == layer:#если индекс редмета равен индексу человека, то повышаем n
                    goThrough(n+1, layer+1, used+[ticket])
                else:#иначе не трогаем
                    goThrough(n, layer+1, used+[ticket])

    goThrough(0, 0, [])

    #пересчёт вероятностей
    for j in range(0, humans+1):
        myTable.cells[j].reset_probability()
    
    return myTable

def things_complexity_optimized_solution(humans:int = 0):
    """
    Оптимизированное решение задачи о 'невнимательной секретарше' (сколько людей получат свои вещи)
    
    Суть оптимизации:
        На больших значениях n существует закономерность в значениях кол-ва перестановок для СВ равной от 2 до n-2, где СВ обозначает 'какое кол-во людей получили свои вещи'

    Args:
        humans (int): кол-во людей

    Returns:
        EttaTable: таблица ячеек таблицы
    """
    #следующей строчкой находим количество всех перестановок
    allPerestan = math.factorial(humans)

    #определяем таблицу
    myTable = EttaTable(cells=[])
    for j in range(0, humans+1):
        myTable.cells.append(EttaTableCell(j, 0, allPerestan))

    myTable.cells[0].good_th = int(round(math.factorial(humans)/math.e))
    myTable.cells[1].good_th = myTable.cells[0].good_th + (-1)**(humans+1)
    myTable.cells[-1].good_th = 1
    myTable.cells[-2].good_th = 0

    for id in range(2, humans-1):
        myTable.cells[id].good_th = int(round(myTable.cells[id-1].good_th / id))

    #пересчёт вероятностей
    for j in range(0, humans+1):
        myTable.cells[j].reset_probability()
    
    return myTable

def things_complexity_request(text: str = None):
    """
    Решение задачи о 'невнимательной секретарше' (сколько людей получат свои вещи)
    WARNING: Очень неоптимизированное! Не рекоммендую пытаться решить для количества людей > 11

    Args:
        text (str): текст запроса, который может быть None или вводом пользователя
    
    Returns:
        list: массив строчек ответа
    """
    if text == None:
        return ["""Введите количество человек (число n)"""]
    else:
        try:
            request = [int(parameter) for parameter in re.findall(regular_int, text)]
            if len(request) == 1:
                answer = []

                humans_num = request[0]

                result = things_complexity_solution(humans_num)

                answer.append("Таблица:")

                for cell in result.cells:
                    answer.append(f"E = {cell.etta_value}; P = {cell.probability} ({cell.good_th}/{cell.all_th})")
                return answer
            else:
                return ["""Возникла ошибка при обработке введённых данных. Проверьте правильность ввода."""]
        except:
            return ["""Возникла ошибка при обработке введённых данных. Проверьте правильность ввода."""]

def things_complexity_optimized_request(text, maximum_full:int = 11):
    """
    Оптимизированное решение задачи о 'невнимательной секретарше' (сколько людей получат свои вещи)
    WARNING: т.к. для n > maximum_full используется приблизительный подсчёт кол-ва перестановок, значения могут быть весьма неточными, если поставить maximum_full слишком низким

    Суть оптимизации:
        На больших значениях n существует закономерность в значениях кол-ва перестановок для СВ равной от 2 до n-2, где СВ обозначает 'какое кол-во людей получили свои вещи'

    Args:
        text (str): текст запроса, который может быть None или вводом пользователя
        maximum_full (int) = 11: максимальное количсетво людей, для которых значения СВ будут считаться полностью. для запросов, где пользователь указывает n>maximum_full, функция посчитает приблизительные значения
    
    Returns:
        list: массив строчек ответа
    """
    if text == None:
        return ["""Введите количество человек (число n)"""]
    else:
        try:
            request = [int(parameter) for parameter in re.findall(regular_int, text)]
            if len(request) == 1:
                answer = []

                humans_num = request[0]
                if humans_num <= maximum_full:
                    result = things_complexity_solution(humans_num)
                else:
                    result = things_complexity_optimized_solution(humans_num)

                answer.append("Таблица:")
                k=0
                for cell in result.cells:
                    if k <= 1 or k >= humans_num-2:
                        answer.append(f"E = {cell.etta_value}; P = {cell.probability} ({cell.good_th}/{cell.all_th})")
                    else:
                        answer.append(f"E = {cell.etta_value}; P ≈ {cell.probability} ({cell.good_th}/{cell.all_th})")
                    k += 1
                return answer
            else:
                return ["""Возникла ошибка при обработке введённых данных. Проверьте правильность ввода."""]
        except:
            return ["""Возникла ошибка при обработке введённых данных. Проверьте правильность ввода."""]

def geometric_meeting_terminal():
    """
    Общее решение задачи о встрече двух участников
    """
    ln = float(input("Введите отрезок меры: "))
    fM = Meetiner(float(input("Введите начальный момент, когда может появиться участник первый (-1 для расширения на полный отрезок): ")), 
    float(input("Введите конечный момент, когда может появиться участник первый (-1 для расширения на полный отрезок): ")), 
    float(input("Введите, сколько времени будет ждать участник первый: ")))

    sM = Meetiner(float(input("Введите начальный момент, когда может появиться участник второй (-1 для расширения на полный отрезок): ")), 
    float(input("Введите конечный момент, когда может появиться участник второй (-1 для расширения на полный отрезок): ")), 
    float(input("Введите, сколько времени будет ждать участник второй: ")))

    print("Обозначим за A - участники встретятся")
    print(f"P(A) = {geometric_meeting_solution(ln, fM, sM)}")

def geometric_meeting_solution(length:float = 0, firstAim:Meetiner=None, secondAim:Meetiner=None):
    """
    Решение задачи о встрече двух участников

    Args:
        length (float): длина участка меры, на которой могут встретиться участники
        firstAim (Meetiner): первый участник
        secondAim (Meetiner): второй участник

    Returns:
        float: вероятность встречи первого и второго участника
    """
    square = ( length)**2
    square -= firstAim.calculate_square(length, secondAim.waiting_time)
    square -= secondAim.calculate_square(length, firstAim.waiting_time)

    return square/(length**2)

def geometric_meeting_request(text: str = None):
    """
    Решение задачи о встрече двух участников

    Args:
        text (str): текст запроса, который может быть None или вводом пользователя
    
    Returns:
        list: массив строчек ответа
    """
    if text == None:
        return ["""Введите отрезок меры
Введите НАЧАЛЬНЫЙ и КОНЕЧНЫЙ моменты, когда может появиться участник ПЕРВЫЙ (-1 для расширения на полный отрезок)
Введите, сколько времени будет ждать участник ПЕРВЫЙ
Введите НАЧАЛЬНЫЙ и КОНЕЧНЫЙ моменты, когда может появиться участник ВТОРОЙ (-1 для расширения на полный отрезок)
Введите, сколько времени будет ждать участник ВТОРОЙ"""]
    else:
        try:
            request = [float(parameter) for parameter in re.findall(regular_float, text)]
            if len(request) == 7:
                answer = []

                ln = request[0]
                fM = Meetiner(request[1], request[2], request[3])
                sM = Meetiner(request[4], request[5], request[6])

                result = geometric_meeting_solution(ln, fM, sM)

                answer.append("Обозначим за A - участники встретятся")
                answer.append(f"P(A) = {result}")

                return answer
            else:
                return ["""Возникла ошибка при обработке введённых данных. Проверьте правильность ввода."""]
        except:
            return ["""Возникла ошибка при обработке введённых данных. Проверьте правильность ввода."""]

def find_math_prediction_solution(table: EttaTable = None, degree: float = 1, ignore_errors: bool = False):
    """
    Нахождение МО по таблице значений случайных величин

    Args:
        table (EttaTable): таблица значений случайных величин
    
    Returns:
        string: Математическое ожидание||'ошибка распределения'
    """
    if table == None:
        return "Wrong Table"
    else:
        matP = 0
        total_probability = 0
        for cell in table.cells:
            matP += (cell.etta_value**degree)*cell.probability
            total_probability += cell.probability
        if total_probability != 1 and not ignore_errors:
            return "Ошибка распределения (error code: 1)"
        return str(matP)

def find_math_prediction_terminal():
    """
    Нахождение МО по таблице значений случайных величин
    """
    n = int(input("Введите количество значений в таблице: "))
    table = EttaTable()
    for i in range(0, n):
        v, p = map(float, input(f"введите пару чисел (значение, вероятность) для {i+1}-го значения").split())
        table.cells.append(EttaTableCell(etta_value=v, probability=p))
    result = find_math_prediction_solution(table)
    if "ошибка" not in result.lower():
        print(f"Mx = ⁱ⁼¹∑ⁿ(xi * pi) = {result}")
    else:
        print(result)

def find_math_prediction_request(text: str = None):
    """
    Нахождение МО по таблице значений случайных величин

    Args:
        text (str): текст запроса, который может быть None или вводом пользователя
    
    Returns:
        list: массив строчек ответа
    """
    if text == None:
        return ["""Введите количество значений таблицы (число n)
В следующих n строчках введите пары чисел: значение СВ, вероятность (любой разделитель, кроме точки)"""]
    else:
        try:
            request = [float(parameter) for parameter in re.findall(regular_float, text)]

            n = int(request[0])
            table = EttaTable()

            for i in range(0, n):
                table.cells.append(EttaTableCell(etta_value=request[1+i*2], probability=request[2+i*2]))

            answer = []

            result = find_math_prediction_solution(table)
            if "ошибка" not in result.lower():
                answer.append(f"Mx = ⁱ⁼¹∑ⁿ(xi * pi) = {find_math_prediction_solution(table)}")
            else:
                answer.append(result)

            return answer
        except:
            return ["""Возникла ошибка при обработке введённых данных. Проверьте правильность ввода."""]

def find_dispersion_solution(table: EttaTable):
    """
    Функция, считающая дисперсию для таблицы СВ

    Args:
        table (EttaTable): таблица СВ

    Returns:
        string: дисперсия СВ/ошибка
    """
    if table != None:
        summ = 0
        math_prediction = find_math_prediction_solution(table, 1)
        if "ошибка" not in math_prediction.lower():
            for cell in table.cells:
                summ += (cell.etta_value - float(math_prediction))**2 * cell.probability
            return str(summ)
        else:
            return "Ошибка при вычислении мат. ожидания. Проверьте коррекность введённых данных. (error code: 1)"

def find_dispersion_terminal():
    """
    Функция, считающая дисперсию для таблицы СВ
    """
    n = int(input("Введите количество значений в таблице: "))
    table = EttaTable()
    for i in range(0, n):
        v, p = map(float, input(f"введите пару чисел (значение, вероятность) для {i+1}-го значения").split())
        table.cells.append(EttaTableCell(etta_value=v, probability=p))
    result = find_dispersion_solution(table)
    if "ошибка" not in result.lower():
        print(f"Dx = ⁱ⁼¹∑ⁿ( (xi - M(X))² pi ) = {result}")
    else:
        print(result)

def find_dispersion_request(text: str = None):
    """
    Нахождение дисперси СВ по таблице значений СВ

    Args:
        text (str): текст запроса, который может быть None или вводом пользователя
    
    Returns:
        list: массив строчек ответа
    """
    if text == None:
        return ["""Введите количество значений таблицы (число n)
В следующих n строчках введите пары чисел: значение СВ, вероятность (любой разделитель, кроме точки)"""]
    else:
        try:
            request = [float(parameter) for parameter in re.findall(regular_float, text)]

            n = int(request[0])
            table = EttaTable()

            for i in range(0, n):
                table.cells.append(EttaTableCell(etta_value=request[1+i*2], probability=request[2+i*2]))

            answer = []

            result = find_dispersion_solution(table)
            if "ошибка" not in result.lower():
                answer.append(f"Dx = ⁱ⁼¹∑ⁿ( (xi - M(X))² pi ) = {result}")
            else:
                answer.append(result)

            return answer
        except:
            return ["""Возникла ошибка при обработке введённых данных. Проверьте правильность ввода."""]

def table_analysis_solution(table: EttaTable):
    """
    Находит Мx и Dx для таблицы значений СВ

    Args:
        table (EttaTable): таблица значений СВ

    Returns:
        list: [float, float] - массив со значениями Mx и Dx
    """
    mat_prediction = find_math_prediction_solution(table)
    dispersion = find_dispersion_solution(table)

    return [mat_prediction, dispersion]

def table_analysis_terminal():
    """
    Функция, считающая дисперсию и математическое ожидание для таблицы СВ
    """
    n = int(input("Введите количество значений в таблице: "))
    table = EttaTable()
    for i in range(0, n):
        v, p = map(float, input(f"введите пару чисел (значение, вероятность) для {i+1}-го значения: ").split())
        table.cells.append(EttaTableCell(etta_value=v, probability=max(p,0)))
        
    result = table_analysis_solution(table)

    if "ошибка" not in result[0].lower() and "ошибка" not in result[1].lower():
        print(f"Mx = ⁱ⁼¹∑ⁿ(xi * pi) = {result[0]}\nDx = ⁱ⁼¹∑ⁿ( (xi - M(X))² pi ) = {result[1]}")
    else:
        print("Возникла ошибка при вычислении. Проверьте коррекность введённых данных.")
        print("Дополнительная информация об ошибке:")
        print(result[0])
        print(result[1])

def table_analysis_request(text: str = None):
    """
    Нахождение дисперси и математического ожидания СВ по таблице значений СВ

    Args:
        text (str): текст запроса, который может быть None или вводом пользователя
    
    Returns:
        list: массив строчек ответа
    """
    if text == None:
        return ["""Введите количество значений таблицы (число n)
В следующих n строчках введите пары чисел: значение СВ, вероятность (любой разделитель, кроме точки)"""]
    else:
        try:
            request = [float(parameter) for parameter in re.findall(regular_float, text)]
            print(request)
            n = int(request[0])
            table = EttaTable()

            for i in range(0, n):
                table.cells.append(EttaTableCell(etta_value=request[1+i*2], probability=max(request[2+i*2],0)))
                print(table.cells[i].probability, table.cells[i].etta_value)

            answer = []
            result = table_analysis_solution(table)
            
            if "ошибка" not in result[0].lower() and "ошибка" not in result[1].lower():
                answer.append(f"Mx = ⁱ⁼¹∑ⁿ(xi * pi) = {result[0]}")
                answer.append(f"Dx = ⁱ⁼¹∑ⁿ( (xi - M(X))² pi ) = {result[1]}")
            else:
                answer.append("Возникла ошибка при вычислении. Проверьте коррекность введённых данных.")
                answer.append("Дополнительная информация об ошибке:")
                answer.append(result[0])
                answer.append(result[1])
            return answer
        except:
            return ["""Возникла ошибка при обработке введённых данных. Проверьте правильность ввода."""]
