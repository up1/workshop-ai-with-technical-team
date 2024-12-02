from openai import OpenAI
import sqlite3
import sqlite_vec
import struct
from typing import List



def serialize(vector: List[float]) -> bytes:
    """serializes a list of floats into a compact "raw bytes" format"""
    return struct.pack("%sf" % len(vector), *vector)


sentences = [
    "I love cat",
    "I love dog"
]

# change ':memory:' to a filepath to persist data
db = sqlite3.connect(":memory:")
db.enable_load_extension(True)
sqlite_vec.load(db)
db.enable_load_extension(False)

db.execute(
    """
        CREATE TABLE sentences(
          id INTEGER PRIMARY KEY,
          sentence TEXT
        );
    """
)

with db:
    for i, sentence in enumerate(sentences):
        db.execute("INSERT INTO sentences(id, sentence) VALUES(?, ?)", [i, sentence])

db.execute(
    """
        CREATE VIRTUAL TABLE vec_sentences USING vec0(
          id INTEGER PRIMARY KEY,
          sentence_embedding FLOAT[1536]
        );
    """
)

client = OpenAI()
with db:
    sentence_rows = db.execute("SELECT id, sentence FROM sentences").fetchall()
    response = client.embeddings.create(
        input=[row[1] for row in sentence_rows], model="text-embedding-3-small"
    )
    for (id, _), embedding in zip(sentence_rows, response.data):
        db.execute(
            "INSERT INTO vec_sentences(id, sentence_embedding) VALUES(?, ?)",
            [id, serialize(embedding.embedding)],
        )


query = "cute animals"
query_embedding = (
    client.embeddings.create(input=query, model="text-embedding-3-small")
    .data[0]
    .embedding
)

results = db.execute(
    """
      SELECT
        vec_sentences.id,
        distance,
        sentence
      FROM vec_sentences
      LEFT JOIN sentences ON sentences.id = vec_sentences.id
      WHERE sentence_embedding MATCH ?
        AND k = 3
      ORDER BY distance
    """,
    [serialize(query_embedding)],
).fetchall()

for row in results:
    print(row)