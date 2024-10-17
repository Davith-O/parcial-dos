def calcular_bonificacion(cargo, desempeño, salario_base):
  """Calcula la bonificación de un empleado.

  Args:
    cargo: El cargo del empleado (directivo o operativo).
    desempeño: El nivel de desempeño (alto, medio o bajo).
    salario_base: El salario base del empleado.

  Returns:
    La bonificación calculada.
  """

  if desempeño == "bajo":
    return 0

  if cargo == "directivo":
    if desempeño == "alto":
      return salario_base * 0.2
    else:
      return salario_base * 0.1
  else:  # Cargo operativo
    if desempeño == "alto":
      return salario_base * 0.15
    else:
      return salario_base * 0.05

def calcular_salario_total(cargo, desempeño, salario_base):
  """Calcula el salario total de un empleado.

  Args:
    cargo: El cargo del empleado (directivo o operativo).
    desempeño: El nivel de desempeño (alto, medio o bajo).
    salario_base: El salario base del empleado.

  Returns:
    El salario total del empleado.
  """

  bonificacion = calcular_bonificacion(cargo, desempeño, salario_base)
  salario_total = salario_base + bonificacion
  return salario_total

# Ejemplo de uso:
cargo = "directivo"
desempeño = "alto"
salario_base = 5000

salario_total = calcular_salario_total(cargo, desempeño, salario_base)
print("El salario total es:", salario_total)