import enum


# class Status(enum.Enum):
#     OK = 0
#     Online = 1
#     Connected = 3
#     Rejected = 3
#     NotAutorized = 4
#     Anozer = 4

# print(Status.OK.name)

# for status in Status:
#     print(f"{status.name} : {status.value}")


...


status = enum.Enum('Status', ['ok', 'online'])
for s in status:
    print(f"{s} : {s.value}")