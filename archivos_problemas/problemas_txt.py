#dos listas, una con nombres otra con apellidos

nombres = ["Nahuel", "Martin", "Agustin", "Tomas", "Gonzalo", "Lucas"]
apellidos = ["Andujar", "Casillo", "Goroso", "Caimini", "Yepes", "Cortes"]

#registrar esta informacion en un txt

with open ("archivos_problemas\\nombres_y_apellidos.txt","w") as arch:
    arch.writelines("Los datos son: \n \n")
    [arch.writelines (f"Nombre: {n} \nApellido: {a}\n------------------\n") for n,a in zip(nombres,apellidos)] 