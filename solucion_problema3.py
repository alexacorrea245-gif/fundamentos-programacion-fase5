# =====================================================================
# Curso: Fundamentos de Programación (Código: 213022)
# Fase 5 - Evaluación Final POA
# Problema Seleccionado: Problema 3 - Auditoría de Inventario
# Enfoque: Programación Estructurada
# estudiante:Alexa Maria Correa
# =====================================================================

def calcular_cantidad_a_pedir(stock_actual, stock_minimo):
    """
    Módulo (Función) para determinar la cantidad exacta a pedir para un artículo.
    Lógica de negocio:
    - Si Stock Actual < Stock Mínimo -> Cantidad = Mínimo - Actual
    - Si Stock Actual >= Stock Mínimo -> Cantidad = 0
    """
    if stock_actual < stock_minimo:
        cantidad_a_pedir = stock_minimo - stock_actual
    else:
        cantidad_a_pedir = 0
        
    return cantidad_a_pedir


def generar_informe_inventario(inventario_matriz):
    """
    Módulo para recorrer la matriz de artículos, procesar las cantidades
    e imprimir la lista de pedidos requerida.
    """
    print("\n" + "="*50)
    print("        INFORME DE AUDITORÍA Y PEDIDOS")
    print("="*50)
    print(f"{'ARTÍCULO':<25} | {'CANTIDAD A SOLICITAR'}")
    print("-"*50)
    
    # Recorrer la matriz fila por fila (artículo por artículo)
    for articulo in inventario_matriz:
        # Desempaquetar los datos de la fila de la matriz
        codigo = articulo[0]
        nombre = articulo[1]
        stock_actual = articulo[2]
        stock_minimo = articulo[3]
        
        # Llamar al módulo de cálculo para obtener la cantidad exacta
        cantidad_solicitada = calcular_cantidad_a_pedir(stock_actual, stock_minimo)
        
        # Imprimir el resultado formateado en la lista de pedidos
        print(f"{nombre:<25} | {cantidad_solicitada} unidades")
        
    print("="*50 + "\n")


def main():
    """
    Función principal encargada de la inicialización de los datos
    y el control del flujo del programa.
    """
    # Matriz inicial con 5 artículos (Formato: [Código, Nombre, Stock Actual, Stock Mínimo])
    # Se incluyen casos donde el stock es menor, igual y mayor al mínimo para probar la lógica.
    matriz_inventario = [
        ["ART001", "Teclado Mecánico RGB", 12, 15],  # Requiere reabastecimiento (Faltan 3)
        ["ART002", "Mouse Óptico Gamer", 25, 20],    # Stock suficiente (0 a pedir)
        ["ART003", "Monitor 24 Pulgadas FHD", 4, 8],  # Requiere reabastecimiento (Faltan 4)
        ["ART004", "Memoria RAM DDR4 16GB", 30, 30], # Stock exacto (0 a pedir)
        ["ART005", "Disco Duro SSD 1TB", 3, 10]      # Requiere reabastecimiento (Faltan 7)
    ]
    
    # Ejecutar el módulo de generación del informe
    generar_informe_inventario(matriz_inventario)


# Punto de entrada del programa estructurado
if __name__ == "__main__":
    main()