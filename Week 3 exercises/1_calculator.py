from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Надсилаємо ідентифікаційний номер кожному іншому процесу
for i in range(size):
    if i != rank:
        data = rank
        comm.send(data, dest=i)

# Отримуємо інформацію про ідентифікаційні номера від кожного іншого процесу
for i in range(size):
    if i != rank:
        received_data = comm.recv(source=i)
        print(f"Process {rank} received message from process {i} with data {received_data}")
