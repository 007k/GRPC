import grpc

# import the generated classes
import crud_pb2
import crud_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:3115')

# create a stub (client)
stub = crud_pb2_grpc.crud_operationsStub(channel)

# create a valid request message
# student_id_data = crud_pb2.delete_student(student_id=100)

# make the call
# response = stub.deleteStudentD(student_id_data)
# et voilà
# print(response)