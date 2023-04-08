print("¿Quieres saber que tipo de ACL tienes?")
acl = int(input("Ingresar Numero de su ACL: "))

if 1 <= acl <= 99:
    print("La ACL", acl, "corresponde a una Estándar.")
elif 100 <= acl <= 199:
    print("La ACL", acl, "corresponde a una Extendida.")
else:
    print("La ACL", acl, "no corresponde a una ACL.")
