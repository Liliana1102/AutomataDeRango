import tkinter as tk

class Automata:
    def __init__(self):
        self.states = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12','q13','914'}
        self.alphabet = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                         'A', 'B', 'C', 'D', 'E', 'F', 'G','H', 'I', 'J',
                         'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
                         'U', 'V', 'W', 'X', 'Y', 'Z', '-'}
        
        self.transitions = {
            'q0': {'T': 'q1', 'U': 'q5'},
            'q1': {'N': 'q2', 'O': 'q2', 'P': 'q2', 'Q': 'q2', 'R' : 'q2', 'S': 'q2', 'T': 'q2', 'U': 'q2', 'V': 'q2', 'W' : 'q2', 
                   'X': 'q2', 'Y': 'q2', 'Z': 'q2'},
            'q2': {'A': 'q3', 'B': 'q3', 'C': 'q3', 'D': 'q3', 'E' : 'q3', 'F': 'q3', 'G': 'q3', 'H': 'q3', 'I': 'q3', 'J' : 'q3', 
                   'K': 'q3', 'L': 'q3', 'M': 'q3', 'N': 'q3', 'O': 'q3', 'P': 'q3', 'Q': 'q3', 'R': 'q3', 'S': 'q3', 'T': 'q3',
                   'U': 'q3', 'V': 'q3', 'W': 'q3', 'X': 'q3', 'Y': 'q3', 'Z': 'q3'},
            'q3': {'-': 'q4'},
            'q4': {'0': 'q8' ,'1': 'q11', '2': 'q11', '3': 'q11', '4': 'q11', '5': 'q11', '6': 'q11', '7': 'q11', '8': 'q11', '9' : 'q11'},
            'q5': {'J': 'q6' ,'K': 'q6', 'L': 'q6', 'M': 'q6', 'N': 'q6', 'O': 'q6', 'P': 'q6', 'Q': 'q6', 'R': 'q6', 'S' : 'q6', 'T': 'q6',
                   'U': 'q6', 'V': 'q6', 'W': 'q6', 'X': 'q6', 'Y': 'q6', 'Z': 'q6'},
            'q6': {'A': 'q7', 'B': 'q7', 'C': 'q7', 'D': 'q7', 'E' : 'q7', 'F': 'q7', 'G': 'q7', 'H': 'q7', 'I': 'q7', 'J' : 'q7', 
                   'K': 'q7', 'L': 'q7', 'M': 'q7', 'N': 'q7', 'O': 'q7', 'P': 'q7', 'Q': 'q7', 'R': 'q7', 'S': 'q7', 'T': 'q7',
                   'U': 'q7', 'V': 'q7', 'W': 'q7', 'X': 'q7', 'Y': 'q7', 'Z': 'q7'},
            'q7': {'-': 'q4'},
            'q8': {'0': 'q9', '1': 'q12', '2': 'q12', '3': 'q12', '4': 'q12', '5': 'q12', '6': 'q12', '7': 'q12', '8': 'q12', '9': 'q12'},
            'q9': {'1': 'q10', '2': 'q10', '3': 'q10', '4': 'q10', '5': 'q10', '6': 'q10', '7': 'q10', '8': 'q10', '9': 'q10'},
            'q10': {'-': 'q13'},
            'q11': {'0': 'q12','1': 'q12', '2': 'q12', '3': 'q12', '4': 'q12', '5': 'q12', '6': 'q12', '7': 'q12', '8': 'q12', '9' : 'q12'},
            'q12': {'0': 'q10', '1': 'q10', '2': 'q10', '3': 'q10', '4': 'q10', '5': 'q10', '6': 'q10', '7': 'q10', '8': 'q10', '9' : 'q10'},
            'q13': {'A': 'q14', 'B': 'q14', 'C': 'q14', 'D': 'q14', 'E' : 'q14', 'F': 'q14', 'G': 'q14', 'H': 'q14', 'I': 'q14', 'J' : 'q14', 
                   'K': 'q14', 'L': 'q14', 'M': 'q14', 'N': 'q14', 'O': 'q14', 'P': 'q14', 'Q': 'q14', 'R': 'q14', 'S': 'q14', 'T': 'q14',
                   'U': 'q14', 'V': 'q14', 'W': 'q14', 'X': 'q14', 'Y': 'q14', 'Z': 'q14'},
            'q14': {},
        }   
        self.start_state = 'q0'
        self.accept_states = {'q14'}
        
    def validar(self, input_string):
        current_state = self.start_state
        visited_stats = [current_state]
        for symbol in input_string:
            if symbol not in self.alphabet:
                return False  # C no v
            if current_state not in self.states:
                return False  # E no v
            current_state = self.transitions[current_state].get(symbol, None)
            visited_stats.append(current_state)
            if current_state is None:
                return False  # No hay transicion
        if current_state in self.accept_states:
            return visited_stats
        return False

    
automata = Automata()

def verificarCadena():
    input_string = entr.get()
    result = automata.validar(input_string)
    if result:
        resultado.config(text=f"Cadena valida: {input_string}")
        showRoute(result)
    else:
        resultado.config(text=f"Cadena no valida: {input_string}")
        showRoute([])

def showRoute(visited_states):
    route_text = "\n".join(visited_states)
    route_label.config(text=f"Recorrido:\n{route_text}")


vent = tk.Tk()
vent.title("Ventana de Pruebas")
vent.geometry("400x400")
vent.configure(background='pink')

etiq = tk.Label(vent, text="Escribe una cadena:", bg="maroon1", font="Helvetica 15 bold")
etiq.pack()
etiq.pack(fill=tk.X)

entr = tk.Entry(vent)
entr.pack(padx=40,pady=40)

btn = tk.Button(vent, text="Verificar", bg="SpringGreen2", font=" Helvetica 10 bold", command=verificarCadena)
btn.pack()

resultado = tk.Label(vent, text="", bg="pink", font=" Helvetica 10 bold")
resultado.pack(padx=20,pady=20)

route_label = tk.Label(vent, text="Recorrido del autómata:", bg="pink", font=" Helvetica 10 bold")
route_label.pack()

vent.mainloop()