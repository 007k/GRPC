import grpc
from concurrent import futures
import time

# import the generated classes
import crud_pb2
import crud_pb2_grpc

# import the original crud.py
import crud

# create a class to define the server functions, derived from
# crud_pb2_grpc.Servicer
class crudServicer(crud_pb2_grpc.crud_operationsServicer):

    def fetchStudentD(self, request, context):
        response = crud_pb2.fetch_student_all()#GeneratedProtocolMessageType
        myfetchdata = crud.fetchStudent()
        # k = 0
        for k in range(len(myfetchdata)):
            lst = crud_pb2.fetch_student()
            lst.name = myfetchdata[k][1]
            lst.dob = str(myfetchdata[k][2])
            lst.student_id = myfetchdata[k][3]
            lst.mobilenumber = myfetchdata[k][5]
            k = k+1;
            response.alldata.extend([lst])
        return response

    def createStudentD(self, request, context):
        response = crud_pb2.success_message()
        pass_data = {'name':request.name, 'dob':request.dob, 'student_id':request.student_id, 'mobilenumber':request.mobilenumber}
        response.msg = crud.createStudent(pass_data)
        return response

    def updateStudentD(self, request, context):
        response = crud_pb2.success_message()
        pass_data = {'name':request.name, 'dob':request.dob, 'student_id':request.student_id, 'mobilenumber':request.mobilenumber}
        response.msg = crud.updateStudent(pass_data)
        return response

    def deleteStudentD(self, request, context):
        response = crud_pb2.success_message()
        response.msg = crud.deleteStudent(request.student_id)
        return response


# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# use the generated function `Servicer_to_server`
# to add the defined class to the server
crud_pb2_grpc.add_crud_operationsServicer_to_server(
        crudServicer(), server)

# listen on port 50051
print('Starting server. Listening on port 3115.')
server.add_insecure_port('[::]:3115')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)