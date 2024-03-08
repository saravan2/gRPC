import grpc
import asyncio
from grpc.experimental import aio
import signal
import timer_service_pb2
import timer_service_pb2_grpc

class TimerService(timer_service_pb2_grpc.TimerServiceServicer):

    async def RegisterTimer(self, request, context):
        await context.write(timer_service_pb2.TimerResponse(message=f"Timer registered for {request.duration} seconds"))
        # Wait asynchronously for the duration specified in the request
        await asyncio.sleep(request.duration)
        # Send a notification back to the client
        await context.write(timer_service_pb2.TimerResponse(message=f"Timer expired after {request.duration} seconds"))



async def serve():
    server = aio.server()
    timer_service_pb2_grpc.add_TimerServiceServicer_to_server(TimerService(), server)
    listen_addr = '[::]:50051'
    server.add_insecure_port(listen_addr)
    print(f"Starting async server on {listen_addr}")
    await server.start()

    async def shutdown_signal_handler(server):
        print("Received shutdown signal, stopping server...")
        await server.stop(None)  # Gracefully stop the server
    
    # Register the signal handler for both SIGTERM and SIGINT
    loop = asyncio.get_running_loop()
    for signal_name in (signal.SIGTERM, signal.SIGINT):
        loop.add_signal_handler(signal_name, lambda: asyncio.create_task(shutdown_signal_handler(server)))
        
    await server.wait_for_termination()

if __name__ == '__main__':
    asyncio.run(serve())