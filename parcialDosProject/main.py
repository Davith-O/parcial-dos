salario_base = int(input("Ingrese el salario base mensual: "))
cargo = input("Ingrese el cargo del empleado: ")
nivel_desempeno = input("Ingrese el nivel de desempeño: ")

if cargo.lower() == "directivo":
    if nivel_desempeno.lower() == "alto":
        boni = salario_base * 0.2
    elif nivel_desempeno.lower() == "medio":
        boni = salario_base * 0.1
    elif nivel_desempeno.lower() == "bajo":
        print("No hay bonificacion")
if cargo.lower() == "operativo":
    if nivel_desempeno.lower() == "alto":
        boni = salario_base * 0.15
    elif nivel_desempeno.lower() == "medio":
        boni = salario_base * 0.05
    elif nivel_desempeno.lower() == "bajo":
        print("No se otorga ninguna bonificacion")

total_recibir = salario_base+boni

print(f"-----Resumen del Pago-----\n Cargo: {cargo.capitalize()}\n Nivel de Desempeño: {nivel_desempeno.capitalize()}\n "
      f"Salario base: ${round(salario_base)}\n Bonificacion: ${round(boni)}\n Total a Recibir: ${round(total_recibir)}\n"
      f"-------------------------")
