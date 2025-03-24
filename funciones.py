def listar_titulos(datos):
    # Opción 1: Muestra los títulos, fecha y etiquetas sin formato de tabla
    for articulo in datos["articulos"]:
        print("Título:", articulo["titulo"])
        print("Fecha de publicación:", articulo["publicadoEn"])
        print("Etiquetas:", ", ".join(articulo["etiquetas"]))
        print()

def listar_titulos_simples(datos):
    # Muestra solo los títulos
    for articulo in datos["articulos"]:
        print("-", articulo["titulo"])

def listar_autores(datos):
    # Muestra la lista de autores
    autores = []
    for articulo in datos["articulos"]:
        if articulo["autor"]["nombre"] not in autores:
            autores.append(articulo["autor"]["nombre"])
    autores.sort()
    for autor in autores:
        print("-", autor)

def total_articulos_por_categoria(datos):
    # Opción 2: Muestra el total de artículos por categoría con formato de tabla
    categorias = {}
    for articulo in datos["articulos"]:
        for categoria in articulo["fuente"]["categorias"]:
            if categoria in categorias:
                categorias[categoria] += 1
            else:
                categorias[categoria] = 1
    
    # Formato de tabla
    print("Categoría".ljust(30) + "Total de artículos")
    print("-" * 50)
    for categoria, total in categorias.items():
        print(categoria.ljust(30) + str(total))

def mostrar_companias(datos, titulo):
    # Opción 3: Muestra las compañías relacionadas con el artículo, formato de tabla
    for articulo in datos["articulos"]:
        if articulo["titulo"].lower() == titulo.lower():
            if "empresas" in articulo:
                print("Compañía".ljust(30) + "Industria")
                print("-" * 50)
                for empresa in articulo["empresas"]:
                    print(empresa["nombre"].ljust(30) + empresa["industria"])
            else:
                print("No hay compañías relacionadas con este artículo.")
            return
    print("Artículo no encontrado.")

def buscar_por_autor(datos, autor):
    # Opción 4: Muestra los artículos por autor en formato tabla
    encontrado = False
    print("Título".ljust(50) + "Fecha de publicación")
    print("-" * 80)
    for articulo in datos["articulos"]:
        if articulo["autor"]["nombre"].lower() == autor.lower():
            print(articulo["titulo"].ljust(50) + articulo["publicadoEn"])
            encontrado = True
    if not encontrado:
        print("No se encontró ningún artículo de este autor.")

def resumen_por_fuente(datos):
    # Opción 5: Resumen por fuente, con formato simple sin tabla
    fuentes = {}
    for articulo in datos["articulos"]:
        fuente = articulo["fuente"]["nombre"]
        if fuente in fuentes:
            fuentes[fuente].append(articulo["titulo"])
        else:
            fuentes[fuente] = [articulo["titulo"]]
    
    # No se usa formato de tabla, se imprime sin alineación
    for fuente, titulos in fuentes.items():
        print(f"\nFuente: {fuente}, Total de artículos: {len(titulos)}")
        for titulo in titulos:
            print(f"- {titulo}")
