from collections import defaultdict
from functools import total_ordering


def parseData(name="task"):
    lines = open(f"{name}.txt").read().splitlines()
    return [tuple(line.split("-")) for line in lines]


def solve1(data):
    network = defaultdict(set)

    for node1, node2 in data:
        network[node1].add(node2)
        network[node2].add(node1)

    cliques = set([])
    for node, neighbours in network.items():
        for n1 in neighbours:
            for n2 in network[n1]:
                if node in network[n2]:
                    if "t" in [node[:1], n1[:1], n2[:1]]:
                        cliques.add(tuple(sorted([node, n1, n2])))

    return len(cliques)

def solve2(data):
    network = defaultdict(set)

    for node1, node2 in data:
        network[node1].add(node2)
        network[node2].add(node1)

    def bron_kerbosch(r, p, x):
        if not p and not x:
            return r
        max_clique = set()
        for v in list(p):
            clique = bron_kerbosch(r | {v}, p & network[v], x & network[v])
            if len(clique) > len(max_clique):
                max_clique = clique
            p.remove(v)
            x.add(v)
        return max_clique

    all_nodes = set(network.keys())
    max_clique = bron_kerbosch(set(), all_nodes, set())
    
    return ",".join(tuple(sorted(max_clique)))




print("🎄 Day 23: LAN Party")
# print("Part 1:", solve1(parseData("task")))
print("Part 2:", solve2(parseData("task")))
