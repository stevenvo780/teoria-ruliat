# Extended RULIAT Graph

## ¿Qué es el RULIAT?

RULIAT (Rule Lineage Tracing) es un método para explorar el espacio de reglas de autómatas celulares. El objetivo es investigar cómo diferentes reglas producen diferentes patrones a lo largo del tiempo y cómo están relacionadas entre sí. Los componentes clave del RULIAT son:

1. **Evolución Temporal**: Examina cómo una regla específica evoluciona con el tiempo, generalmente desde una configuración inicial simple.
2. **Lineaje de Reglas**: Investiga no solo una regla específica sino también sus "antecesores" y "descendientes", es decir, reglas similares.
3. **Representación en Grafos**: Utiliza un grafo para mostrar los estados y las transiciones entre ellos. Cada nodo representa un estado del autómata celular, y cada arista representa una transición bajo una regla específica.
4. **Análisis de Conectividad**: Estudia cómo los diferentes estados están conectados y cómo se puede pasar de un estado a otro a través del grafo.

## Sobre el Script

El script `ruliat_graph.py` implementa un modelo extendido del RULIAT en Python. Utiliza las bibliotecas `numpy`, `networkx` y `matplotlib` para la generación y visualización del grafo RULIAT.

### Operaciones Matemáticas Clave

1. **Conversión de Base**: Las reglas se convierten de su forma decimal a una representación binaria de 8 bits.
2. **Indexación y Slicing de Arrays**: Se utiliza para obtener el vecindario de cada celda en el autómata.
3. **Conversión de Binario a Decimal**: Se convierte el vecindario de cada celda a un número decimal para usarlo como índice en la regla binaria.

### Uso

1. Defina las reglas, el estado inicial y el número de pasos en las variables `rules`, `initial_state` y `steps`.
2. Ejecute el script para generar y visualizar el grafo RULIAT.

### Ejemplo de Código

```python
rules = [30, 90, 110]  # Reglas a explorar
initial_state = np.array([0, 0, 1, 0, 0], dtype=np.int8)  # Estado inicial
steps = 3  # Número de pasos de evolución

# Generar y visualizar el grafo RULIAT
G_extended = generate_ruliat_graph_extended(rules, initial_state, steps)
...
