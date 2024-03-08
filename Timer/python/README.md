## Notes


gRPC install
```
pip install grpcio grpcio-tools
```

gRPC code generation
```
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. timer_service.proto
```

Server streaming : Server can send multiple messages back to the client over a single RPC call

Client and server are coded with asyncio and gracefully exit upon receiving exit signals.

## Usage

**Start server**
```
python timer_service.py 
Starting async server on [::]:50051
```

**Start Client**
```
python timer_client.py 
Doing other work while waiting for messages...
Timer registration initiated for 12 seconds
Doing other work while waiting for messages...
Received from server: Timer registered for 12 seconds
Doing other work while waiting for messages...
Doing other work while waiting for messages...
Doing other work while waiting for messages...
Doing other work while waiting for messages...
Doing other work while waiting for messages...
Doing other work while waiting for messages...
Doing other work while waiting for messages...
Doing other work while waiting for messages...
Doing other work while waiting for messages...
Doing other work while waiting for messages...
Doing other work while waiting for messages...
Received from server: Timer expired after 12 seconds
Timer expiry event received. Exiting...
```

## Shutdown
Both client and server can gracefully exit upon receiving SIGINT and SIGTERM

```
python timer_client.py 
Doing other work while waiting for messages...
Timer registration initiated for 14 seconds
Doing other work while waiting for messages...
Received from server: Timer registered for 14 seconds
Doing other work while waiting for messages...
Doing other work while waiting for messages...
^CSignal handler received SIGINT
Shutdown was called because of exit signal SIGINT
Canceling outstanding tasks
RPC task cancelled. Closing channel ...
RPC task cancelled. Channel closed. Exiting ...
Main task was cancelled !
Shutdown complete.

python timer_service.py 
Starting async server on [::]:50051
^CReceived shutdown signal, stopping server...
```