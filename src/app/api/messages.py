from fastapi import APIRouter
from kafka import KafkaConsumer


router = APIRouter()


@router.get("/messages")
async def last_messages():
    consumer = KafkaConsumer(
        bootstrap_servers="kafka:9092",
        auto_offset_reset="earliest",
        consumer_timeout_ms=500,
    )
    consumer.subscribe(["fuelsave"])
    resp = []
    for msg in consumer:
        resp.append(msg)
    consumer.close()
    return {"messages": resp}
