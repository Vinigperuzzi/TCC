from pygdbmi.gdbcontroller import GdbController

gdbmi = GdbController()

gdbmi.write('-file-exec-and-symbols my_program')
gdbmi.write('-break-insert main')
gdbmi.write('-break-insert 5')

gdbmi.write('-exec-run')
gdbmi.write('-exec-next')
teste = gdbmi.write('-data-evaluate-expression teste')

# aqui a ideia é ficar chamando as funções do GDB, que já está conectando, e recebendo a resposta ao final
# e fazer a maior boa do universo parseando a parada conforme necessário

print(teste)