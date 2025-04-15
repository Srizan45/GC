import pathway as pw

def sport_pipeline():
    table = pw.io.kafka.read(
        topic="live-sports",
        servers="localhost:9092",
        format="json"
    )

    # Just save as a snapshot to JSON
    pw.io.json.write(table, "live_output.json")

if __name__ == "__main__":
    sport_pipeline().run()
