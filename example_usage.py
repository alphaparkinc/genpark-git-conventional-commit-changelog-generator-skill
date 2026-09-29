from client import ConventionalCommitGenerator

diff = """
+ def test_cache_miss():
+     cache = LRUCache(2)
+     assert cache.get("none") is None
"""

msg = ConventionalCommitGenerator.synthesize_commit(diff)
print("Synthesized Commit:", msg)
