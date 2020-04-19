from fastapi import APIRouter
from kafka import KafkaConsumer


router = APIRouter()


@router.get("/messages")
async def last_messages():
    try:
        consumer = KafkaConsumer(
            bootstrap_servers="kafka:9092",
            auto_offset_reset="earliest",
            consumer_timeout_ms=500,
        )
        consumer.subscribe(["fuelsave"])
        resp = []
        for msg in consumer:
            resp.append(msg)
            if len(resp) == 10:
                break
        return {"messages": resp}
    finally:
        consumer.close()
