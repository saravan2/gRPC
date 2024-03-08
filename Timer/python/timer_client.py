import grpc
import asyncio
import random
import timer_service_pb2
import timer_service_pb2_grpc
import signal

async def run_rpc_call(status_queue: asyncio.Queue):
    async with grpc.aio.insecure_channel('localhost:50051') as channel:
        try:
            stub = timer_service_pb2_grpc.TimerServiceStub(channel)
            try:
                # Generate a random duration between 10 and 15 seconds
                random_duration = random.randint(10, 15)
                await status_queue.put(f"Timer registration initiated for {random_duration} seconds")
                async for response in stub.RegisterTimer(timer_service_pb2.TimerRequest(duration=random_duration)):
                    await status_queue.put(f"Received from server: {response.message}")
            except grpc.RpcError as e:
                await status_queue.put(f"RPC failed with code {e.code()}: {e.details()}")
        except asyncio.CancelledError:
            print("RPC task cancelled. Closing channel ...")
            await channel.close()
            print("RPC task cancelled. Channel closed. Exiting ...")
            return    
        

async def main_task(status_queue: asyncio.Queue):
    # Start the RPC call task concurrently
    rpc_task = asyncio.create_task(run_rpc_call(status_queue))
    try:
        while True:
            try:
                status_message = status_queue.get_nowait()
                print(status_message)
                if status_message.startswith("Received from server: Timer expired"):
                    print("Timer expiry event received. Exiting...")
                    break
            except asyncio.QueueEmpty:
                pass  # If the queue is empty, do nothing and proceed to the next block

            # Perform other tasks here, executed in every loop iteration

            await asyncio.sleep(1)  # Simulate doing other work with a non-blocking wait
            print("Doing other work while waiting for messages...")
    except asyncio.CancelledError:
        print("Main task was cancelled !")
        return

async def shutdown(status_queue: asyncio.Queue, signal=None):
    """Cleanup tasks tied to the service's shutdown."""
    if signal:
        print(f"Shutdown was called because of exit signal {signal.name}")
    tasks = [t for t in asyncio.all_tasks() if t is not asyncio.current_task()]

    print("Canceling outstanding tasks")
    for task in tasks:
        task.cancel()

    for task in tasks:
        try:
            await task
        except asyncio.CancelledError:
            pass  # Expected, as we're cancelling tasks
        except Exception as e:
            print(f"Error in task: {e}")
    
    print("Shutdown complete.")

def signal_handler(loop, status_queue, signal_received):
    """Signal handler that schedules the shutdown coroutine."""
    print(f"Signal handler received {signal_received.name}")
    asyncio.ensure_future(shutdown(status_queue, signal_received))

async def main():
    status_queue = asyncio.Queue()
    loop = asyncio.get_running_loop()
    for sig in (signal.SIGINT, signal.SIGTERM):
        loop.add_signal_handler(sig, signal_handler, loop, status_queue, sig)
    await main_task(status_queue)

if __name__ == '__main__':
    asyncio.run(main())