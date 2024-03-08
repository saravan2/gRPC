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
