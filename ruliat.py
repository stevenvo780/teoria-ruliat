import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Función para generar un grafo RULIAT con múltiples reglas de autómatas celulares
def generate_ruliat_graph_extended(rules, initial_state, steps):
    G = nx.DiGraph()

    # Convertir un array de números binarios a un string para usarlo como nombre de nodo
    def state_to_str(state):
        return ''.join(map(str, state))

    # Conjunto para almacenar los estados visitados y evitar duplicación
    visited_states = set()

    # Función recursiva para evolucionar un estado del autómata celular
    def evolve_state(rule, state, step):
        if step == 0:
            return

        # Conversión de la regla decimal a una representación binaria de 8 bits
        # Operación matemática: Conversión de base (Decimal a Binario)
        rule_bin = np.array([int(x)
                            for x in np.binary_repr(rule, 8)], dtype=np.int8)
        num_cells = len(state)
        new_state = np.zeros(num_cells, dtype=np.int8)

        for cell in range(num_cells):
            # Obtener el vecindario del estado actual (celda actual, una a la izquierda, una a la derecha)
            # Operación matemática: Indexación y slicing de arrays
            neighborhood = state[[cell-1, cell, (cell+1) % num_cells]]

            # Convertir el vecindario a un número entero para usarlo como índice en la regla
            # Operación matemática: Conversión de Binario a Decimal
            neighborhood_int = int("".join(neighborhood.astype(str)), 2)

            # Aplicar la regla para encontrar el nuevo estado de la celda
            # Operación matemática: Indexación de array
            new_state[cell] = rule_bin[-(neighborhood_int+1)]

        prev_state_str = state_to_str(state)
        new_state_str = state_to_str(new_state)

        if (prev_state_str, new_state_str) not in visited_states:
            G.add_node(prev_state_str, label=prev_state_str)
            G.add_node(new_state_str, label=new_state_str)
            G.add_edge(prev_state_str, new_state_str, rule=rule)
            visited_states.add((prev_state_str, new_state_str))

        for next_rule in rules:
            evolve_state(next_rule, new_state, step-1)

    for rule in rules:
        evolve_state(rule, initial_state, steps)

    return G


# Parámetros iniciales: conjunto de reglas, estado inicial y número de pasos
rules = [30, 90, 110]
initial_state = np.array([0, 0, 1, 0, 0], dtype=np.int8)
steps = 3

# Generación del grafo RULIAT
G_extended = generate_ruliat_graph_extended(rules, initial_state, steps)

# Visualización del grafo
pos = nx.spring_layout(G_extended, seed=42)
labels = nx.get_edge_attributes(G_extended, 'rule')
nx.draw(G_extended, pos, with_labels=True, labels=nx.get_node_attributes(G_extended, 'label'),
        node_color='lightblue', font_weight='bold', node_size=700, font_size=18)
nx.draw_networkx_edge_labels(G_extended, pos, edge_labels=labels)
plt.title("Extended RULIAT Graph")
plt.show()
