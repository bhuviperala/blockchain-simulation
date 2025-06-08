import random

# Proof of Work
miner = {"id": "MinerA", "power": random.randint(1, 100)}
print(f"PoW - Selected: {miner['id']} with power {miner['power']}")

# Proof of Stake
validators = [
    {"id": "Alice", "stake": random.randint(10, 100)},
    {"id": "Bob", "stake": random.randint(10, 100)},
    {"id": "Charlie", "stake": random.randint(10, 100)}
]
pos_selected = max(validators, key=lambda x: x['stake'])
print(f"PoS - Selected: {pos_selected['id']} with stake {pos_selected['stake']}")

# Delegated Proof of Stake
voters = {"X": "Alice", "Y": "Alice", "Z": "Bob"}
vote_counts = {}
for vote in voters.values():
    vote_counts[vote] = vote_counts.get(vote, 0) + 1
dpos_selected = max(vote_counts, key=vote_counts.get)
print(f"DPoS - Selected: {dpos_selected} by votes: {vote_counts}")
